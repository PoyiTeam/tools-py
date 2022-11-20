"""
run this script with unittest
$ python -m unittest ${script_name}
"""

import unittest


class TestStringMethods(unittest.TestCase):

    lst_test = ['hello test', 'hello world']

    def test_upper(self):
        for string in self.lst_test:
            self.assertEqual(string, string.upper())

    def test_isupper(self):
        for string in self.lst_test:
            self.assertTrue(string.isupper())
            self.assertFalse(string.isupper())

    def test_split(self):
        for string in self.lst_test:
            self.assertEqual(string.split(), ['hello', 'test'])
            # check that s.split fails when the separator is not a string
            with self.assertRaises(TypeError):
                string.split(2)


if __name__ == '__main__':
    # add test function one by one
    # suite1 = unittest.TestSuite()
    # suite1.addTest(TestStringMethods('test_upper'))
    # suite1.addTest(TestStringMethods('test_isupper'))
    # suite1.addTest(TestStringMethods('test_split'))

    # add test function by list
    tests = ['test_upper', 'test_isupper', 'test_split']
    suite2 = unittest.TestSuite(map(TestStringMethods, tests))

    # add all test function in test class
    # suite3 = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)

    unittest.main(verbosity=2)
