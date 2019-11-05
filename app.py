#import flask
from flask import Flask, render_template

#declare an app instance
app = Flask(__name__)

#declare routes
@app.route('/')
def home():
    return 'Hello World'

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return str(num1 + num2)

@app.route('/profile/<username>')
def profile(username):
    return render_template('index.html', username=username)


if __name__ == '__main__':
    app.run()