import settings

from BeautifulSoup import BeautifulSoup


class PrettifyMiddleware(object):
    """HTML code prettification middleware."""
    def process_response(self, request, response):
        if settings.PRETTIFY and response['Content-Type'].split(';', 1)[0] == 'text/html':
            response.content = BeautifulSoup(response.content).prettify()
        return response
