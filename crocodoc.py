from bolacha import Bolacha, multipart
import urlparse
import json

def process_json(fn):
    def wrapper(*args, **kwargs):
        response, content = fn(*args, **kwargs)
        return json.loads(content)
    return wrapper

class Crocodoc():
    API_URL = 'https://crocodoc.com/api/v1/' #need trailing slash
    API_TOKEN = ''

    def __init__(self, api_token):
        self.API_TOKEN = api_token
        self.conn = Bolacha()

    def _merge_params(self, params, whitelist):
        pass
    
    @process_json
    def upload(self, url_or_file, **options):
        '''
        Upload and convert a file referenced by URL or uploaded via a POST
        request.
        '''
        options['token'] = self.API_TOKEN

        #Check if we have a url or file
        if multipart.is_file(url_or_file):
            options['file'] = url_or_file
            return self.conn.post(
                    urlparse.urljoin(self.API_URL, 'document/upload'), 
                    body = options)

        #Otherwise, we just have a url
        options['url'] = url_or_file
        return self.conn.get(
                urlparse.urljoin(self.API_URL, 'document/upload'), 
                body = options
                )
        
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
