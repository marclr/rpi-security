import requests


class Webcontrol:
    def __init__(self, configuration):
        self.ip = configuration.ip
        self.port = configuration.port
        self.url = 'http://' + self.ip + ':' + self.port

    def execute(self, type, cmd):
        # TODO: Add parameter to pass the camera number
        req = self.url + '/0/' + type + '/' + cmd
        response = requests.get(req)
        response_code = response.status_code
        response_text = response.text
        return response_code, response_text
