import unittest
from lucky_server_method import Method

class TestMethod(unittest.TestCase):
    """test class of lucky_server_method.py
    """

    def test_get_statusline(self):
        """ test method for get
        """
        print("test case1 : hello")
        expected1 = "HTTP/1.0 200 OK"
        msg1 = "hello"
        method1 = Method(msg1)
        response1 = method1.get().splitlines()
        actual1 = response1[0]
        self.assertEqual(expected1, actual1)

    def test_get_header(self):
        print("test case2: hogehoge")
        expected2 = "Content-Type: text/html; charset=UTF-8"
        msg2 = "hogehoge"
        method2 = Method(msg2)
        response2 = method2.get().splitlines()
        actual2 = response2[1]
        self.assertEqual(expected2, actual2)

    def test_get_msg(self):
        print("test case3: hello world!")
        expected3 = None
        msg3 = "hello world!"
        method3 = Method(msg3)
        response3 = method3.get().splitlines()
        actual3 = response3[6]
        self.assertNotEqual(expected3, actual3)

if __name__ == "__main__":
    unittest.main()
