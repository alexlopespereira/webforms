import json
import os
import requests

APP_PATH = os.environ.get('APP_PATH') or '/app'

def create_form_template():
    if not os.path.exists(APP_PATH + "/static/assets/forms"):
        os.mkdir(dir)

    with open(APP_PATH + "/static/assets/{0}.form".format("Form"), 'w') as f:
        f.write(
        """{
            "key": "{{ formkey }}",
            "name": "This is a",
            "fields": [
            {% block body %}
                {% for field in fields%}
                {
                    "id": "{{ field }}",
                    "name": "{{ field }}",
                    "type": "text",
                    "required": false,
                    "placeholder": "empty"
                },
                {% endfor %}
            {% endblock %}
            ]
        }"""
        )
        f.close()
    print("Creating form template")