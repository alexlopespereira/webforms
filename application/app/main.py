import json

from eve import Eve
from flask import request, flash, render_template

app = Eve(__name__, static_folder="static")

app.config['SECRET_KEY'] = "test"

@app.route('/<form_name>')
def index(form_name):
    form_name = form_name + '.js'
    return render_template('example.html', value=form_name)
