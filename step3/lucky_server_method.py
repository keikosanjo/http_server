class Method:
    def __init__(self, url, msg):
        self.url = url;
        self.msg = msg;
    
    def get(self):
        url_list = self.url.split(".")
        url_type = url_list[1]
        if url_type == "html":
            status_line = "HTTP/1.0 200 OK"
            header = '''Content-Type: text/html; charset=UTF-8
Server: lucky_server
Content-Length: ''' + str(len(self.msg)) + '''

'''
            body = self.msg
            response = status_line + "\n" + header + "\n" + body
            return(response)
        if url_type == "css":
            status_line = "HTTP/1.0 200 OK"
            header = '''Content-Type: text/css; charset=UTF-8
Server: lucky_server
Content-Length: ''' + str(len(self.msg)) + '''

'''
            body = self.msg
            response = status_line + "\n" + header + "\n" + body
            return(response)
