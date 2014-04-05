"""
StudySheet: definitions.py

Contains callable functions to different ask different
internet sources for information.

Available sources:
- wikipedia
- wolfram
"""
import sys
import wikipedia


def get_definitions(wordlist, source):
    """
    Gets all definitions of words in wordlist from source.
    """
    if source in SOURCES:
        # Call corresponding function in SOURCES
        source_requests = SOURCES[source](wordlist)
    else:
        sys.exit("EXIT: %s is not available" % source)


def ask_wikipedia(wordlist):
    """
    Gathers requests from wikipedia. Packs all words into
    a single request.

    Returns: List
    """
    content = wikipedia.send_requests(wordlist)
    print content


# Functions
SOURCES = {
    'wikipedia' : ask_wikipedia,
}
