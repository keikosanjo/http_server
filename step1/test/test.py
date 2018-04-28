import unittest
from ../lucky_server_method import Method

class TestMethod(unittest.TestCase):
    """test class of lucky_server_method.py
    """

    def test_get(self):
        """ test method for get
        """
        msg =  "hello"
        expected = '''HTTP/1.0 200 OK
Content-Type: text/html; charset=UTF-8
Server: lucky_server
Content
