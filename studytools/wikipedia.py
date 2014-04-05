"""
Module for handling API requests to wikipedia
"""
import requests

API_ROOT = 'https://en.wikipedia.org/w/api.php'


def send_requests(wordlist):
    """
    Sends requests to WikiMedia API. Asynchronous
    calls are not needed because API allows multiple
    articles to be requested at once.
    """
    url = pack_url(normalize_titiles(wordlist))
    print url
    # requests.get(url)
    # print requests.status_code


def normalize_titiles():
    """
    Normalizes the article titles from API specification:
    https://www.mediawiki.org/wiki/API:Query

    Parameters:
    - wordlist: List

    Returns: String
    """
    pass


def pack_url(titles):
    """
    Creates a URL for api request to WikiMedia.

    Parameters:
    - titles: String (ex. 'Blue|Green|Red')

    Returns: String
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


