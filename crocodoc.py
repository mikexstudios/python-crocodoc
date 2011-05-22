from restkit import Resource

class Crocodoc(Resource):
    API_URL = 'https://crocodoc.com/api/v1' #no trailing slash
    API_TOKEN = ''

    def __init__(self, api_token, **kwargs):
        self.API_TOKEN = api_token
        super(Crocodoc, self).__init__(self.API_URL, **kwargs)

    def upload_url(url, title = None, async = False, private = False):
        '''Upload and convert a file referenced by URL.'''
        #NOTE: We may not want to pass params that are default.
        r = self.get('document/upload', params_dict = {
                'url': url,
                'title': title, #may need to check if this is blank or not
                'async': async,
                'private': private,
            })
        return r

    def upload_file(file, title = None, async = False, private = False):
        '''Upload and convert a file uploaded via a POST request.'''
        pass
        
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
