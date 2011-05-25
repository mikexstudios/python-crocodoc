import unittest
import crocodoc
import os #for environ

class TestCrocodoc(unittest.TestCase):
    sample_pdf_url = 'http://www.irs.gov/pub/irs-pdf/i1040ez.pdf'

    def setUp(self):
        self.crocodoc = crocodoc.Crocodoc(os.environ['CROCODOC_API_KEY'])

    def tearDown(self):
        #TODO: Delete uploaded file.
        pass

    def test_upload_url(self):
        r = self.crocodoc.upload(self.sample_pdf_url)
        self.assertTrue('shortId' in r)
        self.assertTrue('uuid' in r)

    def test_upload_file(self):
        with open('test.pdf', 'r') as f:
            r = self.crocodoc.upload(f)
        self.assertTrue('shortId' in r)
        self.assertTrue('uuid' in r)

    def test_status_single(self):
        #Upload a single file first
        uploaded = self.crocodoc.upload(self.sample_pdf_url)
        r = self.crocodoc.status(uploaded['uuid'])

        self.assertTrue('status' in r)
        self.assertTrue('viewable' in r)
        self.assertTrue('uuid' in r)



if __name__ == '__main__':
    #API Key needs to be set before unittests can be run.
    try:
        os.environ['CROCODOC_API_KEY']
    except KeyError:
        exit('Please set environment variable CROCODOC_API_KEY to your API key'
             'before running tests.')

    unittest.main()
