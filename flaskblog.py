from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c997ee3b0c2f462ac8a8916dde6ca11c'

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
