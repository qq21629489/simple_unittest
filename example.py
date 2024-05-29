from tests import *

suite1 = unittest.TestSuite()
suite1.addTest(TestVector('test_init'))
suite1.addTest(TestVector('test_add'))
suite1.addTest(TestVector('test_skip'))

# same as 
tests = ['test_init', 'test_add', 'test_skip']
suite2 = unittest.TestSuite(map(TestVector, tests))

# auto load all test case
suite3 = unittest.TestLoader().loadTestsFromTestCase(TestVector)

# combine suites
suite4 = unittest.TestSuite([suite1, suite2])

# run test
# about verbosity, check: https://blog.csdn.net/zhangvalue/article/details/102901185
unittest.TextTestRunner(verbosity=2).run(suite1)