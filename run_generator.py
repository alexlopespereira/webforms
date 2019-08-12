import json
from flask import Flask, url_for
from flask import request, flash, render_template
from werkzeug.utils import redirect

from static.schemas import all_schemas

app2 = Flask(__name__, static_url_path='/static')
app2.config['SECRET_KEY'] = "test"

python_schemas_file = "./app/curr_schema.py"
javascript_schemas_file = "./app/static/assets/schema_form.js"


def write_file(filename, data):
    with open(filename, 'w') as writer:
        writer.writelines(data)


def write_schema(python_file, javascript_file, selected):
    newschema = dict((k, all_schemas[k]) for k in selected)
    schema_str = "schema = " + json.dumps(newschema)
    js_schema_str = "schema: " + json.dumps(newschema)
    # write_file(python_file, schema_str.replace('true', 'True').replace('false', 'False'))
    javascript_str = """$('form').jsonForm({{ {0} }});""".format(js_schema_str)
    write_file(javascript_file, javascript_str)


@app2.route('/')
def index():
    # return render_template('generator.html')
    template = render_template('generator.html')
    return template

@app2.route('/create_form', methods=["POST"])
def create_form():
    print(request.json)
    write_schema(python_schemas_file, javascript_schemas_file, request.json)
    # flash(u'Sua nova aplicacao foi criada. Reinicie o servidor e atualize o browser.')
    # return redirect(url_for('index'))
    # return send_from_directory("templates", 'generator.html', messages=['You were successfully logged in'])
    template = render_template('generator.html', messages=['You were successfully logged in'])
    return template

app2.run(host="0.0.0.0", port=8088)