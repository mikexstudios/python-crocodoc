import unittest
import crocodoc
import os #for environ
import time #for sleep (to rate limit)

RATE_LIMIT_TIME = 5 #sec

class TestCrocodoc(unittest.TestCase):
    sample_pdf_url = 'http://www.irs.gov/pub/irs-pdf/i1040ez.pdf'

    def setUp(self):
        self.crocodoc = crocodoc.Crocodoc(os.environ['CROCODOC_API_KEY'])

    def tearDown(self):
        #TODO: Delete uploaded file.

        time.sleep(RATE_LIMIT_TIME) #sec, rate limits API requests


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

    def test_status_multiple(self):
        #Upload multiple files
        multiple = []
        #crocodoc rate limits to 2 simultaneous conversions
        for i in range(2):
            multiple.append(self.crocodoc.upload(self.sample_pdf_url))

        #Check the status on each file by querying all of the uuids at once
        uuids = [uploaded['uuid'] for uploaded in multiple]

        r = self.crocodoc.status(uuids)
        self.assertTrue(len(r) == len(multiple))
        for status in r:
            self.assertTrue('status' in status)
            self.assertTrue('viewable' in status)
            self.assertTrue('uuid' in status)



if __name__ == '__main__':
    #API Key needs to be set before unittests can be run.
    try:
        os.environ['CROCODOC_API_KEY']
    except KeyError:
        exit('Please set environment variable CROCODOC_API_KEY to your API key'
             'before running tests.')

    unittest.main()
