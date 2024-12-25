from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simulate handling form data
        username = request.form.get('username')
        password = request.form.get('password')
        # Add simple logic for testing
        if username == "testuser" and password == "testpass":
            return "Login successful!"
        return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True, port=80)
