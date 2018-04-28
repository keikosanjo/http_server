class Method:
    def __init__(self, msg):
        self.msg = msg;
    
    def get(self):
        status_line = "HTTP/1.0 200 OK"
        header = '''Content-Type: text/html; charset=UTF-8
Server: lucky_server
Content-Length: ''' + str(len(self.msg)) + '''

'''
        body = self.msg
        response = status_line + "\n" + header + "\n" + body
        return(response)
