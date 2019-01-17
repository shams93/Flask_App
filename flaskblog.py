from flask import Flask, render_template
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
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
