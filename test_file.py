import unittest
import helloworld
import json

class test_suite(unittest.TestCase):


def lambda_handler(event, context):
    def test_helloworld(self):
        o = helloworld.MyClass()
        val=o.HelloWorld()
        self.assertEqual("Hello World", val)


if __name__ == '__main__':
    unittest.main()