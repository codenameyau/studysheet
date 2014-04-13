"""
knowledge: wolfram.py

Contains methods to query data from WolframAlpha.
Please edit 'apikeys.py' to include your API key!
"""
import xmltodict
import grequests


def send_requests(wordlist):
    """
    Public: (List) -> List

    Sends asynchronous requests to WolframAlpha's API
    and returns a List of dictionaries from responses.
    """
    print wordlist
