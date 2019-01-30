from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c997ee3b0c2f462ac8a8916dde6ca11c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db =SQLAlchemy(app)


class user(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default ='default.jpg')
    password = db.Column(db.String(60), nullable = False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}'',)"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Colum() 

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}'',)"
     

posts = [
    {
        'author':'Shams Ul Zaman',
        'title':' Post One',
        'content':'first post contant',
        'date_posted':'April 20, 2015',

    },
    {
        'author':'Jane',
        'title':' Post Two',
        'content':'second post contant',
        'date_posted':'April 21, 2015',

    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')


@app.route("/register", methods=['Get','Post'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='registration', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='registration', form = form)

if __name__ == '__main__':
    app.run(debug=True)
