"""
Created on 20 July 2020

@Author: Jay Oza
"""

from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Jay Oza',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 20, 2020'
    },
    {
        'author': 'Parth Jadvani',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 21, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)