from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#kasnije dodaj podake za email
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['EMAIL_USERNAME'] = 'your_email@gmail.com'
app.config['EMAIL_PASSWORD'] = 'your_email_password'

#privremena baza korisnika
users = {}

# generise random kod za verifikaciju
def generate_verification_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# salje email za verifikaciju
def send_verification_email(email, verification_code):
    msg = MIMEMultipart()
    msg['From'] = app.config['EMAIL_USERNAME']
    msg['To'] = email
    msg['Subject'] = 'verifikujete vaš email'

    message = f'vaš verifikacioni kod je: {verification_code}'
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(app.config['EMAIL_USERNAME'], app.config['EMAIL_PASSWORD'])
    server.send_message(msg)
    server.quit()

# Sign up
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = generate_password_hash(data.get('password'))
    email = data.get('email')

    if username in users:
        return jsonify({'message': 'Korisnik već postoji!'}), 400

    verification_code = generate_verification_code()
    users[username] = {'password': password, 'email': email, 'verified': False, 'verification_code': verification_code}
    send_verification_email(email, verification_code)

    return jsonify({'message': 'Nalog je kreiran! Molimo verifikujte email.'}), 201

# Verifikacija
@app.route('/verify_email', methods=['POST'])
def verify_email():
    data = request.get_json()
    username = data.get('username')
    verification_code = data.get('verification_code')

    if username not in users:
        return jsonify({'message': 'Korisnik ne postoji!'}), 404

    if users[username]['verification_code'] == verification_code:
        users[username]['verified'] = True
        return jsonify({'message': 'Email uspešno verifikovan!'}), 200
    else:
        return jsonify({'message': 'Pogrešan kod!'}), 401

# Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username not in users or not check_password_hash(users.get(username)['password'], password):
        return jsonify({'message': 'Pogrešan username ili password!'}), 401

    if not users[username]['verified']:
        return jsonify({'message': 'Molimo verifikujte email!'}), 401

    token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
    return jsonify({'token': token.decode('UTF-8')}), 200

# Logout
@app.route('/logout', methods=['POST'])
@token_required
def logout():
    token = request.headers.get('x-access-token')
    data = jwt.decode(token, app.config['SECRET_KEY'])
    username = data['username']

    if username not in users:
        return jsonify({'message': 'Korisnik ne postoji!'}), 404

    # Perform logout action here, if needed
    return jsonify({'message': 'Korisnik je uspesno odjavljen!'}), 200

# Protected endpoint
@app.route('/protected', methods=['GET'])
@token_required
def protected():
    return jsonify({'message': 'This is a protected endpoint!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
