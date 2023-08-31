from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

# @app.route('/homepage', methods = ['POST'])
# def homepage():
#     return render_template('homepage.html')

@app.route('/submitted', methods = ['POST'])
def submitted():
    print(request.form)
    username = request.form.get("username")
    password = request.form.get("password")

    print(username)
    print(password)

    for k, v in database.users_database.items():
        if k == username and v == password:
             return render_template('homepage.html')
        else:
            return render_template('error.html')

@app.route('/logout', methods =['POST'])
def  logout():
    # if request.method == 'post':
    return render_template('logout.html')


if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')

