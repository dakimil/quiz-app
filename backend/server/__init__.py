from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

users = {
    'user1': {'password': generate_password_hash('password1'), 'logged_in': False},
    'user2': {'password': generate_password_hash('password2'), 'logged_in': False}
}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(*args, **kwargs)

    return decorated

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = generate_password_hash(data.get('password'))

    if username in users:
        return jsonify({'message': 'User already exists!'}), 400

    users[username] = {'password': password, 'logged_in': False}
    return jsonify({'message': 'User created successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username not in users or not check_password_hash(users.get(username)['password'], password):
        return jsonify({'message': 'Invalid username or password!'}), 401

    token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
    users[username]['logged_in'] = True
    return jsonify({'token': token.decode('UTF-8')}), 200

@app.route('/logout', methods=['POST'])
@token_required
def logout():
    token = request.headers.get('x-access-token')
    data = jwt.decode(token, app.config['SECRET_KEY'])
    username = data['username']

    if username not in users:
        return jsonify({'message': 'User not found!'}), 404

    users[username]['logged_in'] = False
    return jsonify({'message': 'User logged out successfully!'}), 200

@app.route('/protected', methods=['GET'])
@token_required
def protected():
    return jsonify({'message': 'This is a protected endpoint!'}), 200

if __name__ == '__main__':
    app.run(debug=True)