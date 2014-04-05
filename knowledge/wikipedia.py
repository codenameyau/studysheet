"""
knowledge: wikipedia.py

Module for handling API requests to wikipedia
"""
import requests

API_ROOT = 'https://en.wikipedia.org/w/api.php'


def send_requests(wordlist):
    """
    Public: (List) -> List

    Sends requests to WikiMedia API.

    Example:
    >>> send_requests(['red', 'green', 'blue'])
    >>> [{'word' : 'red', 'definition' : 'color'}, ...]
    """
    url = pack_url(normalize_titiles(wordlist))
    print url
    # requests.get(url)
    # print requests.status_code


def normalize_titiles(wordlist):
    """
    Internal: (List) -> List

    Normalizes the article titles from API specification:
    https://www.mediawiki.org/wiki/API:Query#Title_normalization
    """
    pass


def pack_url(titles):
    """
    Internal: (String) -> String

    Creates a URL for api request to WikiMedia.
    """
    query = {
        'format' : 'json',
        'action' : 'query',
        'titles' : titles,
        'prop'   : 'revisions',
        'rvprop' : 'content'
    }

    # Build URL for API request
    query_string = ''
    for key, value in query.iteritems():
        if key:
            if not query_string:
                query_string += '?%s=%s' % (key, value)
            else:
                query_string += '&%s=%s' % (key, value)
    return API_ROOT + query_string


