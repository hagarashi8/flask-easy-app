from flask import Flask, render_template, request
from json import load

def try_creds(users, name, password):
    if name in users.keys():
        if users[name] == password:
            return True
    return False

if __name__ == '__main__':
    users = dict()

    with open("users.json") as usersfile:
        users = load(usersfile)
    app = Flask(__name__)
    print(users)

    @app.route('/')
    @app.route('/index')
    def index():
        return render_template("index.html")


    @app.route('/', methods=['post'])
    def form():
        if request.method == 'POST':
            username = request.form.get('username').strip()
            password = request.form.get('password').strip()
            if try_creds(users, username, password):
                return render_template('index.html', ans="Access granted")
        return render_template('index.html', ans="Access denied")


    app.run()

