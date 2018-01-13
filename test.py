from random import randint
import webbrowser
from flask import Flask, render_template

app = Flask(__name__)

length = randint(6,12)
some_list = []
for i in xrange(length):
    some_list.append(randint(50, 550))

webbrowser.open('http://127.0.0.1:5000/')

@app.route('/')
def index():
    return render_template('index.html', title='Test Data', data=some_list)
