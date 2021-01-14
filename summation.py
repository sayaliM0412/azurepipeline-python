import unittest
 
   
class MyClass(unittest.TestCase):
   
   
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
        print("something")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 5")


# Create an object from the class
o = MyClass()

# Now we can work with the object
o.test_sum()

# if __name__ == '__main__':
#     unittest.main()