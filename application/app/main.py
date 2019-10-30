import json
import requests

from eve import Eve
from flask import request, flash, render_template

app = Eve(__name__, static_url_path='', static_folder="static")

app.config['SECRET_KEY'] = "test"


def create_data(data, servico):
    context = {
        'data': data,
        'processid': 'process'+servico
    }

    html = render_template('Form.json', context=context)
    print("Creating data")
    print(html)
    return(html)
    
@app.route('/<form_name>', methods = ['POST', 'GET'])
def index(form_name):
    if request.method == 'GET' and form_name != "list":
        form_name = form_name
        return render_template('index.html', form_name=form_name)

    elif request.method == 'GET' and form_name == "list":
        process_list = get_process()
        return render_template('list.html', process_list=process_list)

    else:
        print(request.form.items())
        print(request.form)
        
        url = "http://flowable-all-in-one-app:8080/flowable-task/process-api/runtime/process-instances"

        payload = create_data(request.form.items(), form_name)
        
        headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache"
            }

        response = requests.request("POST", url, data=payload, headers=headers, auth=('admin', 'test'))

        print(response.text)

        return render_template('index.html', form_name=form_name)

def get_process():
    url = 'http://flowable-all-in-one-app:8080/flowable-task/process-api/runtime/process-instances'
    r = requests.get(url, auth=('admin', 'test'))
    process_list = r.json()

    print("Getting processes. Status: {0}".format(r.status_code))

    return process_list
