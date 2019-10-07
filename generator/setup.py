import json
import os

import requests
from flask import Flask, url_for
from flask import request, flash, render_template
from werkzeug.utils import redirect

APP_PATH = os.environ.get('APP_PATH') or '/app'

def write_file(filename, data):
    with open(filename, 'w') as writer:
        writer.writelines(data)


def create_process():
    url = 'http://flowable-all-in-one-app:8080/flowable-task/process-api/process-repository/deployments/'
    files = {'file': open(APP_PATH + "/static/assets/Process_Model_1.bpmn20.xml", 'rb')}
    data = {'deploymentKey': 'proc_modelo', 'deploymentName': 'proc_modelo'}
    r = requests.post(url, files=files, data=data, auth=('admin', 'test'))
    print("Creating process. Status: {0}".format(r.response))



app2.run(host="0.0.0.0", port=8089)
