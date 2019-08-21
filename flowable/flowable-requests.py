import requests


def post_process_instance():
    dictToSend = {'{ "processDefinitionKey":"holidayRequest", "variables": [ { "name":"employee", "value": "John Doe" }, { "name":"nrOfHolidays", "value": 7 }]}'}
    res = requests.post('http://localhost:8080/flowable-rest/service/runtime/process-instances', json=dictToSend, auth=('admin', 'test'))
    print 'response from server:',res.text
    dictFromServer = res.json()


def post_get_tasks():
    dictToSend = {'{ "candidateGroup" : "managers" }'}
    res = requests.post('http://localhost:8080/flowable-rest/service/query/tasks', json=dictToSend, auth=('admin', 'test'))
    print 'response from server:',res.text
    dictFromServer = res.json()

def post_get_tasks():
    dictToSend = {'{ "action" : "complete", "variables" : [ { "name" : "approved", "value" : true} ]  }'}
    res = requests.post('http://localhost:8080/flowable-rest/service/runtime/tasks/25', json=dictToSend, auth=('admin', 'test'))
    print 'response from server:',res.text
    dictFromServer = res.json()
