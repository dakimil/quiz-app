<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(to bottom, #8e44ad, #3498db); 
            color: #fff; 
        }
        nav {
            background-color:#6c3490; 
            padding: 10px 0;
            width: 100%;
            box-sizing: border-box;
            display: flex;
            justify-content: center; 
        }
        nav h1 {
            margin: 0;
            padding: 0;
            font-size: 24px;
        }
        .register-form {
            display: flex;
            flex-direction: column;
            height: 100vh;
            align-items: center;
            justify-content: center;
            padding: 20px;
            box-sizing: border-box;
        }
        .register-form input {
            margin-bottom: 10px;
            padding: 5px;
            width: 30%;
            box-sizing: border-box;
        }
        .register-form button {
            padding: 10px;
            width: 30%;
            box-sizing: border-box;
            background-color: #3459db; 
            color: #fff;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <nav>
        <h1>Register</h1>
    </nav>
    <div class="register-form">
        <p>Email</p>
        <input type="email" name="email" use:validators={[required, email]} />
        <p>Password</p>
        <input type="password" name="password" use:validators={[required]} />
        <p>Confirm password</p>
        <input type="password" name="password1" use:validators={[required]} />
        <button disabled={!$form.valid}>Register</button>
    </div>
</body>
</html>
