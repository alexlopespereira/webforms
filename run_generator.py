import json
from flask import Flask
from flask import request, flash, render_template
from schemas import all_schemas

app2 = Flask(__name__)
app2.config['SECRET_KEY'] = "test"

python_schemas_file = "./curr_schema.py"
javascript_schemas_file = "./templates/assets/schema_form.js"


def write_file(filename, data):
    with open(filename, 'w') as writer:
        writer.writelines(data)


def write_schema(python_file, javascript_file, selected):
    newschema = dict((k, all_schemas[k]) for k in selected)
    schema_str = "schema = " + json.dumps(newschema)
    js_schema_str = "schema: " + json.dumps(newschema)
    write_file(python_file, schema_str.replace('true', 'True').replace('false', 'False'))
    javascript_str = """$('form').jsonForm({{ {0} }});""".format(js_schema_str)
    write_file(javascript_file, javascript_str)


@app2.route('/', methods=["POST"])
def create_form():
    print(request.json)
    write_schema(python_schemas_file, javascript_schemas_file, request.json)
    flash('You were successfully logged in')
    # return redirect(url_for('create_form'))
    # return send_from_directory("templates", 'generator.html', messages=['You were successfully logged in'])
    return render_template('generator.html')

app2.run(port=8080)