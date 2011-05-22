import unittest
import crocodoc
import os #for environ

class TestCrocodoc(unittest.TestCase):
    def setUp(self):
        self.crocodoc = crocodoc.Crocodoc(os.environ['CROCODOC_API_KEY'])

    def tearDown(self):
        pass

    def test_upload_url(self):
        r = self.crocodoc.upload_url('http://www.dcaa.mil/chap6.pdf')
        self.assertTrue('shortId' in r)
        self.assertTrue('uuid' in r)


if __name__ == '__main__':
    #API Key needs to be set before unittests can be run.
    try:
        os.environ['CROCODOC_API_KEY']
    except KeyError:
        exit('Please set environment variable CROCODOC_API_KEY to your API key'
             'before running tests.')

    unittest.main()
