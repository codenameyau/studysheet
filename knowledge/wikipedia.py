"""
knowledge: wikipedia.py

Module for handling API requests to wikipedia
"""
import requests
import json

API_ROOT = 'https://en.wikipedia.org/w/api.php'


def send_requests(wordlist):
    """
    Public: (List) -> Dictionary

    Sends requests to WikiMedia API. If requests is successful,
    returns a Dictionary from the response JSON content.

    Example:
    >> send_requests(['red', 'green', 'blue'])
    """
    url = pack_url(_normalize_titiles(wordlist))
    req = requests.get(url)
    if req.status_code == 200:
        return json.loads(req.content)


def get_first_paragraph(json_content):
    """
    Public: (Dictionary) -> List

    Parses JSON to extract the first paragraph for each entry.
    """
    pass


def _normalize_titiles(wordlist):
    """
    Private: (List) -> List

    Builds up a string from words in wordlist and
    seperates each word with a '|' for titles query.
    """
    # Removes trailing '|'
    return '|'.join(wordlist)[:-1]


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

