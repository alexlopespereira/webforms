import json

from eve import Eve
from flask import request, flash, render_template

app = Eve(__name__, static_url_path='', static_folder="static")

app.config['SECRET_KEY'] = "test"

@app.route('/<form_name>')
def index(form_name):
    form_name = form_name
    return render_template('index.html', form_name=form_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8088)