from flask import Flask, render_template, request, redirect, url_for, session, flash
from jinja2 import Environment, FileSystemLoader
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Suraj'  # Really Important line
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'


@app.route('/')
def home():
    from models import User
    print("In Home")
    if 'emailId' in session:
        print(session['emailId'] + " in session")

    if 'emailId' in session:
        user = User.query.filter_by(email=session['emailId']).first_or_404()
        print(user.email)
        userTags1 = []
        userTags = user.tags.all()
        for tags in userTags:
            userTags1.append(tags.tag_name)
            print(tags.tag_name)
        return render_template('signed_in.html', Name=user.firstName+" "+user.lastName, userTags1=userTags1)

    return render_template('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    from models import db, User
    from models import Tags

    x = False
    users = User.query.all()
    for user in users:
        email = user.email
        if email == request.form['email']:
            x = True
    if not x:
        session['emailId'] = request.form['email']
        user = User(request.form['password1'], request.form['firstName'], request.form['lastName'],
                    request.form['email'], request.form['password2'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('message', namesignup=user.firstName+" "+user.lastName))
    else:
        return render_template('index.html', error="Email already exists")


@app.route('/message/<namesignup>')
def message(namesignup):
    from models import User, db, Tags, CsTags, ElecTags, MusicTags, GamingTags
    users = User.query.all()
    cstags = CsTags.query.all()
    electags = ElecTags.query.all()
    musictags = MusicTags.query.all()
    gamingtags = GamingTags.query.all()
    for tag in cstags:
        print(tag.tag_name)
    emails = []
    for x in users:
        emails.append(x.email)

    return render_template('logged_in.html', email=emails, namesignup=namesignup, cstags=cstags,
                           electags=electags, gamingtags=gamingtags, musictags=musictags)


@app.route('/addTags', methods=['POST'])
def addTags():
    from models import User, Tags, db
    user = User.query.filter_by(email=session.get('emailId')).first_or_404()
    print(user.email)
    tag = request.form['done_btn1']

    print(tag.split(","))
    tags = tag.split(",")
    for tag in tags:
        db.session.add(Tags(tag_name=tag, user=user))
    db.session.commit()
    userTags1 = user.tags.all()

    for usertags in userTags1:
        print(usertags.tag_name + ", ")

    people = []
    for user1 in User.query.all():
        if user1.email != user.email:
            people.append(user1)

    return render_template('tagsAdded.html', user=user, tagsAdded=userTags1, people=people)


@app.route('/signin', methods=['POST'])
def signin():
    from models import User, db

    emailsignin = request.form['emailsignin']
    passwordsignin = request.form['passwordsignin']
    user = User.query.filter_by(email=emailsignin).first_or_404()
    print(user.email)
    userTags1 = []
    if user.password1 == passwordsignin:
        session['emailId'] = emailsignin
        userTags = user.tags.all()
        for tags in userTags:
            userTags1.append(tags.tag_name)
            print(tags.tag_name)
        return render_template('signed_in.html', Name=user.firstName+" "+user.lastName, userTags1=userTags1)
    else:
        error = "Incorrect Password!"
        return render_template('index.html', error=error)


@app.route('/signout', methods=['POST'])
def signout():
    print("in signout method")
    session.pop('emailId', None)
    print("user removed")
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(port=8000)  # 192.168.200.54
