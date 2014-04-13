"""
knowledge: truthseeker.py

Module that packs and sends requests
"""

def pack_url(api_root, query):
    """
    Internal: (String, Dictionary) -> String

    Creates a URL for GET requests.
    """
    query_string = ''
    for key, value in query.iteritems():
        if not query_string:
            query_string += '?%s=%s' % (key, value)
        else:
            query_string += '&%s=%s' % (key, value)
    return api_root + query_string
