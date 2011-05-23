from bolacha import Bolacha
from urlparse import urljoin
import json

def process_json(fn):
    def wrapper(*args, **kwargs):
        response = fn(*args, **kwargs)
        return json.loads(response['body'])
    return wrapper

class Crocodoc():
    API_URL = 'https://crocodoc.com/api/v1' #no trailing slash
    API_TOKEN = ''

    def __init__(self, api_token):
        self.API_TOKEN = api_token
        self.conn = Bolacha()

    def _merge_params(self, params, whitelist):
        pass
    
    @process_json
    def upload_url(self, url, **options):
        '''Upload and convert a file referenced by URL.'''

        options['token'] = self.API_TOKEN
        options['url'] = url
        
        return self.conn.get(urljoin(self.API_URL, 'document/upload'), 
                body = options)

    @process_json
    def upload_file(self, file, **options):
        '''Upload and convert a file uploaded via a POST request.'''

        options['token'] = self.API_TOKEN
        options['file'] = file

        return self.conn.post(urljoin(self.API_URL, 'document/upload'), 
                args = options)
        
    def status():
        pass

    def delete():
        pass

    def download():
        pass

    def share():
        pass

    def get_session():
        pass

    # Helper methods:

    def embeddable_viewer_url():
        pass

    def session_based_viewer_url():
        pass
