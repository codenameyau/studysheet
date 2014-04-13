"""
knowledge: wolfram.py

Contains methods to query data from WolframAlpha.
Please edit 'apikeys.py' to include your API key!
"""
from apikeys import WOLFRAM
import truthseeker
import xmltodict
import grequests

API_BASE = "http://api.wolframalpha.com/v2/query"


def send_requests(wordlist):
    """
    Public: (List) -> List

    Sends asynchronous requests to WolframAlpha's api
    through grequests. Packs individual url queries.
    """
    # Packs requests
    urls = []
    for task in wordlist:
        urls.append(truthseeker.pack_url(API_BASE, {
            'input'  : task.replace(' ', '%20'),
            'format' : 'plaintext',
            'appid'  : WOLFRAM
        }))

    # Send asynchronous requests
    reqs = grequests.map((grequests.get(url) for url in urls))

    # Create list of dictionary for answers
    answers = []
    for res in reqs:
        if res.status_code == 200:
            xmldata = xmltodict.parse(res.content)['queryresult']
            try:
                title = wordlist[len(answers)]
                answers.append(_parse_content(xmldata))
                print "[+] Found: %s" % title
            except KeyError:
                print "[-] Missing: %s" % title
    return answers


def _parse_content(data):
    pass
