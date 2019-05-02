from eve import Eve
from flask import send_from_directory, request

app = Eve(__name__, static_folder="jsonform")

@app.route('/')
def index():
    return send_from_directory("jsonform", 'example.html')

@app.route('/create_form', methods=["POST"])
def create_form():
    form = request.form.to_dict()
    print(form)
    return send_from_directory("jsonform", 'generator.html')

app.run()
