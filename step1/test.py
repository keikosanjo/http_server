import unittest
from lucky_server_method import Method

class TestMethod(unittest.TestCase):
    """test class of lucky_server_method.py
    """

    def test_get(self):
        """ test method for get
        """
        print("test case1 : hello")
        msg1 =  "hello"
        expected1 = '''HTTP/1.0 200 OK
Content-Type: text/html; charset=UTF-8
Server: lucky_server
Content-Length: 5

hello'''
        method1 = Method(msg1)
        actual1 = method1.get()
        self.assertEqual(expected1, actual1)

        print("test case2: hogehoge")
        msg2 = "hogehoge"
        expected2 = '''HTTP/1.0 200 OK
Content-Type: text/html; charset=UTF-8
Server: lucky_server
Content-Length: 8

hogehoge'''
        method2 = Method(msg2)
        actual2 = method2.get()
        self.assertEqual(expected2, actual2)

        print("test case3: hello world!")
        msg3 = "hello world!"
        expected3 = '''HTTP/1.0 200 OK
Content-Type: text/html; charset=UTF-8
Server: lucky_server
Content-Length: 12

hello world!'''
        method3 = Method(msg3)
        actual3 = method3.get()
        self.assertEqual(expected3, actual3)

if __name__ == "__main__":
    unittest.main()
