import json

from eve import Eve
from flask import request, flash, render_template

app = Eve(__name__, static_url_path='', static_folder="static")

app.config['SECRET_KEY'] = "test"

@app.route('/<form_name>')
def index(form_name):
    form_name = form_name
    return render_template('index.html', form_name=form_name)


@app.route('/send_form/<form_name>', methods=["POST"])
def create_form(form_name):
    print(request)
    template = render_template('index.html', messages=['You were successfully'])
    return template


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8088)
