"""
This file exists to demonstrate the functionality of 
ci-donkey.
"""
import unittest
import time
from pprint import pprint
import random
import string

class Test(unittest.TestCase):

    def test_bar(self):
        print '<h1>This should be escaped</h1>'
        print 'test bar, successful'

    def test_bra(self):
        print 'this should be slow...'
        time.sleep(10)
        print 'finished slow thing'

    def test_foo(self):
        print 'test foo:'
        big_list = [''.join(random.choice(string.ascii_lowercase) for i in range(50))
            for _ in range(100)]
        pprint(big_list)
        # raise Exception('foo error')


if __name__ == '__main__':
    unittest.main()
