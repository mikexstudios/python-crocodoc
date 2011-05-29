from bolacha import Bolacha, multipart
import urlparse
import json
import types #for str, unicode type
from exceptions import NotImplementedError

def process_json(fn):
    def wrapper(*args, **kwargs):
        headers, content = fn(*args, **kwargs)
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
        
    @process_json
    def status(self, uuids):
        '''
        Given a single or list of uuids, checks the conversion status of the
        document(s).
        '''
        is_single = False #flag to indicate if we have a single uuid
        options = { 'token': self.API_TOKEN }

        #If we have a string, make it into a list
        if isinstance(uuids, types.StringTypes):
            uuids = [uuids, ]
            is_single = True

        #Convert our list of uuids into a comma-deliminated list of uuids
        options['uuids'] = ','.join(uuids)

        headers, content = self.conn.get(
                urlparse.urljoin(self.API_URL, 'document/status'), 
                body = options
                )
        #If only a single uuid was queried, then modify the response content
        #by removing the '[' and ']' that denote a list.
        if is_single:
            return headers, content[1:-1]
        return headers, content


    @process_json
    def delete(self, uuid):
        '''Given a single uuid, deletes the uploaded file.'''
        options = { 
                'token': self.API_TOKEN,
                'uuid': uuid
                }

        return self.conn.get(
                urlparse.urljoin(self.API_URL, 'document/delete'), 
                body = options
                )


    # TODO: Currently not implemented because raw file should be saved to
    #       filesystem.
    def download(self, uuid, **options):
        options['token'] = self.API_TOKEN
        raise NotImplementedError

    # TODO: Since we know share will only return a shortID, we should just pull
    #       that out and return the shortID value directly.
    @process_json
    def share(self, uuid, **options):
        '''
        Given a uuid, creates a new "short ID" that can be used to share a 
        document.
        '''
        options['token'] = self.API_TOKEN
        options['uuid'] = uuid

        return self.conn.get(
                urlparse.urljoin(self.API_URL, 'document/share'), 
                body = options
                )

    # TODO: Since we know this will only return a sessionId, we should just pull
    #       that out and return the sessionId value directly.
    @process_json
    def get_session(self, uuid, **options):
        '''
        Given a uuid, creates a session ID for session-based document viewing.
        Each session ID may only be used once.
        '''
        options['token'] = self.API_TOKEN
        options['uuid'] = uuid

        return self.conn.get(
                urlparse.urljoin(self.API_URL, 'session/get'), 
                body = options
                )

    # Helper methods:

    def embeddable_viewer_url(self, shortId):
        '''Given a shortId, returns the embeddable URL.'''
        return 'http://crocodoc.com/%s?embedded=true' % shortId

    def session_based_viewer_url(self, sessionId):
        '''Given a sessionId, returns the session-based viewing URL.'''
        return 'https://crocodoc.com/view/?sessionId=%s' % sessionId
