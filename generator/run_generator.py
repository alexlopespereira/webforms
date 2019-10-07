import json
import os

import requests
from flask import Flask, url_for
from flask import request, flash, render_template
from werkzeug.utils import redirect
from static.schemas import all_schemas

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


def create_xml(srcfile, destfile, formkey):
    context = {
        'formkey': formkey
    }
    with open(destfile, 'w') as f:
        html = render_template(srcfile, context=context)
        f.write(html)


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
    print(request.json)
    write_schema(python_schemas_file, APP_PATH + "/static/assets/"+servico+".js", request.json)
    template = render_template('generator.html', messages=['You were successfully logged in'])

    write_schema(python_schemas_file, APP_PATH + "/static/assets/"+servico+".form", request.json)
    url = 'http://flowable-all-in-one-app:8080/flowable-task/form-api/form-repository/deployments/'
    files = {'file': open(APP_PATH + "/static/assets/"+servico+".form", 'rb')}
    data = {'deploymentKey': servico, 'deploymentName': servico}
    r = requests.post(url, files=files, data=data, auth=('admin', 'test'))

    url = 'http://flowable-all-in-one-app:8080/flowable-task/process-api/process-repository/deployments/'
    srcfile = APP_PATH + "/static/assets/{0}.bpmn20.xml".format(v1)
    destfile = APP_PATH + "/static/assets/{0}.bpmn20_{1}.xml".format(v1, servico)
    create_xml(srcfile, destfile, servico)
    files = {'file': destfile}
    data = {'deploymentKey': 'proc_modelo', 'deploymentName': 'proc_modelo'}
    r = requests.post(url, files=files, data=data, auth=('admin', 'test'))
    print("Creating process. Status: {0}".format(r.response))

    url = 'http://flowable-all-in-one-app:8080/flowable-task/app-api/app-repository/deployments/'
    files = {'file': open(APP_PATH + "/static/assets/App1.zip", 'rb')}
    data = {'deploymentKey': servico, 'deploymentName': servico}
    r = requests.post(url, files=files, data=data, auth=('admin', 'test'))

    return template


app2.run(host="0.0.0.0", port=8089)
