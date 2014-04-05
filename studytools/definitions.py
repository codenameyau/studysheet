"""
StudySheet: definitions.py

Contains callable functions to different ask different
internet sources for information.

Available sources:
- wikipedia
- wolfram
"""

def get_definitions(wordlist, source):
    """
    Gets all definitions of words in wordlist from source.
    Sends requests asynchronously through grequests.
    """
    if source in SOURCES:
        ask_source = SOURCES[source]()

def ask_wikipedia():
    """
    Gathers requests from wikipedia.
    """
    print "Hello from wikipedia"


SOURCES = {
    'wikipedia' : ask_wikipedia,
}
