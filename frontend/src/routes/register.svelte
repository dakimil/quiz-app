<div style="display: flex; flex-direction: column; heigh: 100vh; align-items: center; justify-content: center;">
    <h2>Register</h2>
    <p>Email</p>
    <input type="email" name="email" use:validators={[required, email]} />
    <p>Password</p>
    <input type="password" name="password" use:validators={[required]} />
    <p>Confirm password</p>
    <input type="password" name="password1" use:validators={[required]} />

    <button style="margin-top: 10px;" diabled={!$form.valid}>Register</button>
</div>