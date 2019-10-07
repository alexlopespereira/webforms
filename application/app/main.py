import json
import requests

from eve import Eve
from flask import request, flash, render_template

app = Eve(__name__, static_url_path='', static_folder="static")

app.config['SECRET_KEY'] = "test"

@app.route('/<form_name>', methods = ['POST', 'GET'])
def index(form_name):
    if request.method == 'GET':
        form_name = form_name
        return render_template('index.html', form_name=form_name)
    else:
        print(request.form)

        for field, data in request.form.items():
            print(field, data)

        url = "http://flowable-all-in-one-app:8080/flowable-task/process-api/runtime/process-instances"

        payload = "{\n    \"processDefinitionKey\": \"processModel1\",\n    \"startFormVariables\": [\n        {\n            \"name\": \"nome\",\n            \"type\": \"string\",\n            \"value\": \"joao\"\n        },\n        {\n            \"name\": \"telefone\",\n            \"type\": \"string\",\n            \"value\": \"1234\"\n        }\n    ]\n}"
        headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.17.1",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "6efe2193-f658-4b33-91ce-7e2a3b5ce242,e638d989-1c35-4912-b5e0-60e8973845f7",
            'Host': "flowable-all-in-one-app2:8080",
            'Accept-Encoding': "gzip, deflate",
            'Content-Length': "299",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("POST", url, data=payload, headers=headers,
                                    auth=('admin', 'test'))

        print(response.text)

        return render_template('index.html', form_name=form_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8088)
