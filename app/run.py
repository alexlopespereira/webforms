import json

from eve import Eve
from flask import request, flash, render_template

app = Eve(__name__, static_folder="templates")

app.config['SECRET_KEY'] = "test"



@app.route('/')
def index():
    # return send_from_directory("templates", 'example.html')
    return render_template('example.html')




app.run()
