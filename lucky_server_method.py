class Method:
    def __init__(self, msg):
        self.msg = msg;
    
    def get(self):
        response = '''HTTP/1.0 200 OK
Content-Type: text/html; charset=UTF-8
Server: lucky_server
Content-Length: ''' + str(len(self.msg)) + '''

''' + self.msg
        return(response)
