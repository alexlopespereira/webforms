from eve import Eve
from flask import send_from_directory, request
from schemas import all_schemas
app = Eve(__name__, static_folder="jsonform")

@app.route('/')
def index():
    return send_from_directory("jsonform", 'example.html')

@app.route('/create_form', methods=["POST"])
def create_form():
    print(request.json)
    return send_from_directory("jsonform", 'generator.html')

app.run()
