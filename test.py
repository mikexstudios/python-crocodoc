import unittest
import crocodoc
import os #for environ
import time #for sleep (to rate limit)

#NOTE: If you receive errors during testing, it may result from crocodoc limiting
#free users to two simultaneous conversions at once.
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

    def test_delete(self):
        #Upload a single file first
        uploaded = self.crocodoc.upload(self.sample_pdf_url)
        #Then delete it
        r = self.crocodoc.delete(uploaded['uuid'])
        self.assertTrue(r)

    def test_share(self):
        #Upload a single file first
        uploaded = self.crocodoc.upload(self.sample_pdf_url)
        #Get new shortId
        r = self.crocodoc.share(uploaded['uuid'])
        self.assertTrue('shortId' in r)

    def test_get_session(self):
        #Upload a single file first
        uploaded = self.crocodoc.upload(self.sample_pdf_url)
        #Get sessionId
        r = self.crocodoc.get_session(uploaded['uuid'])
        self.assertTrue('sessionId' in r)

    def test_embeddable_viewer_url(self):
        shortId = 'y1O7rK'
        target_url = 'http://crocodoc.com/%s?embedded=true' % shortId

        r = crocodoc.Crocodoc.embeddable_viewer_url(shortId)
        self.assertEqual(r, target_url)

    def test_session_based_viewer_url(self):
        sessionId = 'fgH9qWEwnsJUeB0'
        target_url = 'https://crocodoc.com/view/?sessionId=%s' % sessionId

        r = crocodoc.Crocodoc.session_based_viewer_url(sessionId)
        self.assertEqual(r, target_url)


if __name__ == '__main__':
    #API Key needs to be set before unittests can be run.
    try:
        os.environ['CROCODOC_API_KEY']
    except KeyError:
        exit('Please set environment variable CROCODOC_API_KEY to your API key'
             'before running tests.')

    unittest.main()
