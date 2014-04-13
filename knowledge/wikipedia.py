"""
knowledge: wikipedia.py

Module for handling wikipedia requests and responses
"""
from bs4 import BeautifulSoup
import truthseeker
import requests
import json
import re

API_ROOT = 'https://en.wikipedia.org/w/api.php'


def send_requests(wordlist):
    """
    Public: (List) -> Dictionary | None

    Sends request to WikiMedia API. If requests is successful,
    returns a Dictionary from the response JSON content.

    Example:
    >> send_requests(['red', 'green', 'blue'])
    """
    query = {
        'action'    : 'query',
        'format'    : 'json',
        'titles'    : '|'.join(wordlist),
        'prop'      : 'revisions',
        'rvprop'    : 'content',
        'rvsection' : '0',
        'rvparse'   : 'true'
    }
    url = truthseeker.pack_url(API_ROOT, query)
    req = requests.get(url)
    if req.status_code == 200:
        return json.loads(req.content)


def get_first_paragraph(json_content):
    """
    Public: (Dictionary) -> List

    Parses JSON to extract the first paragraph for each entry.
    """
    pages = json_content['query']['pages']
    parsed_entries = []
    for entry in pages:
        content = pages[entry]
        data = {}
        try:
            data['title'] = content['title']
            data['content'] = _clean_paragraph(content['revisions'][0]['*'])
            print "[+] Found: %s" % content['title']
        except KeyError:
            print "[-] Missing: %s" % content['title']
            continue
        parsed_entries.append(data)
    return parsed_entries


def _clean_paragraph(html):
    """
    Private: (String) -> String

    Finds first paragraph, strips html tags and citations.
    Paragraph is returned with unicode characters.
    """
    soup = BeautifulSoup(html)
    paragraphs = soup.find_all('p', limit=3)
    for entry in paragraphs:
        if len(entry) > 5:
            return re.sub(r'\[\d+\]', '', entry.get_text())
