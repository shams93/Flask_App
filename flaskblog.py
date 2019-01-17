from flask import Flask, render_template, url_for
app = Flask(__name__)

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
@app.route("/registration")
@app.route("/register")
def register():
    return render_template('register.html', title='registration')

if __name__ == '__main__':
    app.run(debug=True)
