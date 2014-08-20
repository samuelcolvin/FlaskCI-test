"""
This file exists to demonstrate the functionality of 
FlaskCI.
"""
import unittest
import time

class Test(unittest.TestCase):

    def test_bar(self):
        print '<h1>This should be escaped</h1>'
        print 'test bar, successful'

    def test_bra(self):
        print 'this should be slow...'
        time.sleep(10)
        print 'finished slow thing'

    def test_foo(self):
        print 'test foo: fails'
        #raise Exception('foo error')


if __name__ == '__main__':
    unittest.main()
