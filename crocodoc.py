from restkit import Resource
import json

class Crocodoc(Resource):
    API_URL = 'https://crocodoc.com/api/v1' #no trailing slash
    API_TOKEN = ''

    def __init__(self, api_token, **kwargs):
        self.API_TOKEN = api_token
        super(Crocodoc, self).__init__(self.API_URL, **kwargs)

    def _merge_params(self, params, whitelist):
        pass
    
    def request(self, *args, **kwargs):
        '''
        Override request method to have all requests return JSON.
        '''
        response = super(Crocodoc, self).request(*args, **kwargs)
        return json.loads(response.body_string())

    def upload_url(self, url, **options):
        '''Upload and convert a file referenced by URL.'''

        options['token'] = self.API_TOKEN
        options['url'] = url
        return self.get('document/upload', params_dict = options)

    def upload_file(self, file, **options):
        '''Upload and convert a file uploaded via a POST request.'''

        options['token'] = self.API_TOKEN
        options['file'] = file.name
        return self.post('document/upload', params_dict = options)
        
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
