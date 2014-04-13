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
            xmldata  = xmltodict.parse(res.content)['queryresult']
            question = wordlist[len(answers)]
            try:
                title   = xmldata['pod'][0]['subpod']['plaintext']
                content = xmldata['pod'][1]['subpod']['plaintext']
                answers.append({
                    'title'   : title,
                    'content' : content
                })
                print "[+] Found: %s" % question
            except KeyError:
                print "[-] Missing: %s" % question
    return answers

