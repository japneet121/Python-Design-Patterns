'''
Proxy design pattern is used when we don't want to use a class directly rather we want to provide an external interface to interact with this class.
This can be important when we have to perform some actions before and after the interaction with class
'''

class BrowserRequest:

    def __init__(self):
        print("This is browser request")

    def send_request(self):
        print("Sending request from Browser")


class RequestProxy:
    def __init__(self):
        print("This is Proxy class")
        self.br=BrowserRequest()

    def send_request(self):
        print("sending request from proxy")
        print("-------------Checking VPN status----------")
        self.br.send_request()
        print("--------Teardown the connection----------")

    
rp=RequestProxy()
rp.send_request()