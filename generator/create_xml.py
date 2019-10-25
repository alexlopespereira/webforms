import json
import os
import requests

from flask import Flask, url_for
from flask import request, flash, render_template
from werkzeug.utils import redirect


APP_PATH = os.environ.get('APP_PATH') or '/app'

def create_xml_form(srcfile, destfile, fields, servico):
    context = {
        'formkey': servico,
        'fields': fields
    }
    with open(destfile, 'w') as f:
        html = render_template(srcfile, context=context)
        f.write(html)
    print("Creating form xml")

def create_form(servico, fields):
    url = 'http://flowable-all-in-one-app:8080/flowable-task/process-api/process-repository/deployments/'
    srcfile = APP_PATH + "/static/assets/{0}.form".format("Form")
    destfile = APP_PATH + "/static/assets/forms/{0}.form".format(servico)
    create_xml_form(srcfile, destfile, fields, servico)
    files = {'file': destfile}
    data = {'deploymentKey': servico, 'deploymentName': servico}
    r = requests.post(url, files=files, data=data, auth=('admin', 'test'))
    print("Creating form. Status: {0}".format(r.response))


#------------------------------------------------------------------------------------------------
def create_xml_process(srcfile, destfile, formkey):
    context = {
        'formkey': formkey
    }
    with open(destfile, 'w') as f:
        html = render_template(srcfile, context=context)
        f.write(html)
    print("Creating process xml")

def create_process(v1, servico):
    url = 'http://flowable-all-in-one-app:8080/flowable-task/process-api/process-repository/deployments/'
    srcfile = APP_PATH + "/static/assets/{0}.bpmn20.xml".format(v1)
    destfile = APP_PATH + "/static/assets/{0}.bpmn20_{1}.xml".format(v1, servico)
    create_xml_process(srcfile, destfile, servico)
    files = {'file': destfile}
    data = {'deploymentKey': servico, 'deploymentName': servico}
    r = requests.post(url, files=files, data=data, auth=('admin', 'test'))
    print("Creating process. Status: {0}".format(r.response))


#------------------------------------------------------------------------------------------------
def create_xml_app(srcfile, destfile, formkey):
    context = {
        'formkey': formkey
    }
    with open(destfile, 'w') as f:
        html = render_template(srcfile, context=context)
        f.write(html)
    print("Creating app xml")


def create_app(servico):
    url = 'http://flowable-all-in-one-app:8080/flowable-task/app-api/app-repository/deployments/'
    files = {'file': open(APP_PATH + "/static/assets/App1.zip", 'rb')}
    srcfile = APP_PATH + "/static/assets/{0}.json".format(v1)
    destfile = APP_PATH + "/static/assets/{0}.bpmn20_{1}.json".format(v1, servico)

    data = {'deploymentKey': servico, 'deploymentName': servico}
    create_xml_process(srcfile, destfile, servico)
    
    r = requests.post(url, files=files, data=data, auth=('admin', 'test'))
    print("Creating process. Status: {0}".format(r.response))
