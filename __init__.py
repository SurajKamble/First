from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Suraj'  # Really Important line
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    from models import db, User

    user = User(request.form['username'], request.form['password'], request.form['firstName'], request.form['lastName'],
                request.form['email'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('message', username=user.username))


@app.route('/message/<username>')
def message(username):
    from models import User
    users = User.query.all()
    usernames = []
    for x in users:
        usernames.append(x.username)
    user = User.query.filter_by(username=username).first()
    return render_template('logged_in.html', username=usernames)

if __name__ == '__main__':
    app.run()