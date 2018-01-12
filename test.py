from random import randint
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    length = randint(6,12)
    some_list = []
    for i in range(length):
        some_list.append(randint(50, 550))
    
    return render_template('index.html', title='Test Data', data=some_list)
