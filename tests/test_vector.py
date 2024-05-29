import unittest
import sys
from vector import Vector

'''
1. test filename(.py) must start with 'test_'
2. test class inherits unittest.TestCase and test class name should start/endup with 'Test'
3. a test class can contain multiple test methods and test method name must start with 'test_'
4. assert methods: https://docs.python.org/zh-tw/3/library/unittest.html#test-cases
5. should not use assertTrue for every test, this may skip some information(ex: variable value) when test fail
'''

class TestVector(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('test class start')
        # cls._connection = ...
    
    @classmethod
    def tearDownClass(cls) -> None:
        print('test class end')
        # cls._connection.destroy() ...
    
    def setUp(self):
        print('test start')
        
    def tearDown(self):
        print('test end')
    
    def test_init(self):
        v = Vector(1, 2)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)
        
        with self.assertRaises(ValueError):
            v = Vector('1', '2')
    
    def test_add(self):
        v1 = Vector(1, 2)
        v2 = Vector(2, 3)
        v3 = v1.add(v2)
        self.assertEqual(v3.x, 3)
        self.assertEqual(v3.y, 5)
    
    @unittest.skipIf(sys.version_info > (3, 7), 'only suport in 3.7 or ealriler')
    def test_skip(self):
        v = Vector(1, 2)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)