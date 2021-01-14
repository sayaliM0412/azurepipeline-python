import unittest


# Create the class
class MyClass(unittest.TestCase):

    def MyFunc(self):
        return "Hello World"

# Create an object from the class
o = MyClass()

# Now we can work with the object
print(o.MyFunc())


def test_mock():
    print("success")
    assert True


if __name__ == '__main__':
    unittest.main()
