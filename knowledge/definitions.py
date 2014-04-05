"""
knowledge: definitions.py

Contains callable functions to different ask different
internet sources for information.

Available sources:
- wikipedia

Future sources:
- wolfram
"""
import sys
import wikipedia


def get_definitions(wordlist, source):
    """
    Public: (List, String) -> List

    Gets all definitions of words in wordlist from source.
    Calls the corresponding function from SOURCES.
    """
    if source in SOURCES:
        source_content = SOURCES[source](wordlist)
    else:
        sys.exit("EXIT: %s is not available" % source)


def ask_wikipedia(wordlist):
    """
    Internal: (List) -> List

    Sends requests to wikipedia to retreive definitions.
    """
    content = wikipedia.send_requests(wordlist)
    print content


# Functions
SOURCES = {
    'wikipedia' : ask_wikipedia,
}
