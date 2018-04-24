#coding:utf-8
import unittest
class C(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_01(self):
        """

            fljkldsjlj
        :return:
        """
        print(self.failUnless("111"))
if __name__ == '__main__':
    unittest.main(verbosity=2)