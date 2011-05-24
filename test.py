import unittest
import crocodoc
import os #for environ

class TestCrocodoc(unittest.TestCase):
    def setUp(self):
        self.crocodoc = crocodoc.Crocodoc(os.environ['CROCODOC_API_KEY'])

    def tearDown(self):
        #TODO: Delete uploaded file.
        pass

    def test_upload_url(self):
        r = self.crocodoc.upload('http://www.dcaa.mil/chap6.pdf')
        self.assertTrue('shortId' in r)
        self.assertTrue('uuid' in r)

    def test_upload_file(self):
        with open('test.pdf', 'r') as f:
            r = self.crocodoc.upload(f)
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
