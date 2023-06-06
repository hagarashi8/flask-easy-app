from flask import Flask, render_template, request
from json import load
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
            print("Lol")
            if username in users.keys():
                print("Kek")
                if users[username] == password:
                    print("Cheburek")
                    return render_template('index.html', ans="Access granted")
        return render_template('index.html', ans="Access denied")


    app.run()

