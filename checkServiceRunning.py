import psutil
import requests
import json

def getService(name):
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        print(str(ex))
    return service

service = getService('serviceName')

print(service)

if service:
    print("Service found")
else:
    print("Service not found")

muleApplications = ['APICALL', 'APICALL']
muleResponseCodes = []

if service and service['status'] == 'running':
    print("Service is running")
else:
    for application in muleApplications:
        payload = requests.get(application).json()
        print('Got response from {}'.format(application))
        muleResponseCodes.append(payload)
        print(payload)
