import json
import os

import requests
from flask import Flask, url_for
from flask import request, flash, render_template
from werkzeug.utils import redirect
from static.schemas import all_schemas
import create_xml


app2 = Flask(__name__, static_url_path='/static')
app2.config['SECRET_KEY'] = "test"
APP_PATH = os.environ.get('APP_PATH') or '/app'

python_schemas_file = "./app/curr_schema.py"


def write_file(filename, data):
    with open(filename, 'w') as writer:
        writer.writelines(data)

def write_schema(python_file, javascript_file, selected):
    newschema = dict((k, all_schemas[k]) for k in selected)
    schema_str = "schema =  " + json.dumps(newschema)
    js_schema_str = "schema: " + json.dumps(newschema)
    # write_file(python_file, schema_str.replace('true', 'True').replace('false', 'False'))
    javascript_str = """$('form').jsonForm({{ {0} }});""".format(js_schema_str)
    write_file(javascript_file, javascript_str)

@app2.route('/')
def index():
    # return render_template('generator.html')
    template = render_template('generator.html')
    return template

@app2.route('/create_form/<servico>', methods=["POST"])
def create_form(servico):
    print(type(request.json))
    v1 = request.json.pop(0)
    v2 = request.json.pop(0)
    v3 = request.json.pop(0)
    print([v1, v2, v3])
    fields = request.json

    write_schema(python_schemas_file, APP_PATH + "/static/assets/"+servico+".js", request.json)
    template = render_template('generator.html', messages=['You were successfully'])

    create_xml.create_form(servico, fields)
    #create_process(v1, servico)
    #create_app(servico)

    return template

app2.run(host="0.0.0.0", port=8089)
