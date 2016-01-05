from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Suraj'  # Really Important line
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'


@app.route('/')
def home():
    print("In Home")
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
    db.session.commit()

    emails = []
    for x in users:
        emails.append(x.email)
    return render_template('logged_in.html', email=emails, namesignup=namesignup, cstags=cstags,
                           electags=electags, gamingtags=gamingtags, musictags=musictags)


@app.route('/signin', methods=['POST'])
def signin():
    from models import User

    emailsignin = request.form['emailsignin']
    passwordsignin = request.form['passwordsignin']
    user1 = User.query.filter_by(email=emailsignin).first_or_404()
    userTags1 = []
    if user1.password1 == passwordsignin:
        userTags = user1.tags.all()
        for tags in userTags:
            userTags1.append(tags.tag_name)
            print(tags.tag_name)
        return render_template('signed_in.html', Name=user1.firstName+" "+user1.lastName, userTags1=userTags1)
    else:
        error = "Incorrect Password!"
        return render_template('index.html', error=error)


@app.route('/message', methods=['POST'])
def addTags():
    from models import User, Tags, db
    user = User.query.filter_by(email=session.get('emailId')).first_or_404()
    tag = request.form['tag_btn']
    tags = Tags(tag_name=tag, user=user)
    db.session.add(tags)
    db.session.commit()
    userTags = user.tags.all()

    for usertags in userTags:
        print(usertags.tag_name)


'''
@app.route('/message1/<emailsignin>')
def message1(emailsignin, passwordsignin):
    from models import User
    user1 = User.query.filter_by(email=emailsignin).first_or_404()

    if user1.passwordsignin == passwordsignin:
        return render_template('signed_in.html', firstName=user1.firstName)
'''

if __name__ == '__main__':
    app.run()