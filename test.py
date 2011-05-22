import unittest
import crocodoc
import os #for environ

class TestCrocodoc(unittest.TestCase):
    def setUp(self):
        c = crocodoc.Crocodoc(os.environ['CROCODOC_API_KEY'])

    def tearDown(self):
        pass

    def test_upload_url(self):
        c.upload_url('http://www.dcaa.mil/chap6.pdf')


if __name__ == '__main__':
    #API Key needs to be set before unittests can be run.
    try:
        os.environ['CROCODOC_API_KEY']
    except KeyError:
        exit('Please set environment variable CROCODOC_API_KEY to your API key'
             'before running tests.')

    unittest.main()
