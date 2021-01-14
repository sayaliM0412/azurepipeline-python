import unittest
import helloworld
import summation

def suite():
    t1 = unittest.TestLoader().loadTestsFromTestCase(helloworld)
    t2 = unittest.TestLoader().loadTestsFromTestCase(summation)
    test_suite = unittest.TestSuite([t1,t2])
    unittest.TextTestRunner(verbosity=2).run(test_suite)
