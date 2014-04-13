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
import wolfram
import transcriber


def create_studysheet(wordlist, source):
    """
    Public: (List, String) -> List

    Gets all definitions of words in wordlist from source.
    Calls the corresponding function from SOURCES.
    """
    if source in SOURCES:
        content = SOURCES[source](wordlist)
        transcriber.generate_doc(content, source)
    else:
        sys.exit("EXIT: %s is not available" % source)


def ask_wikipedia(wordlist):
    """
    Internal: (List) -> List

    Sends requests to wikipedia to retrieve definitions.
    """
    json_content = wikipedia.send_requests(wordlist)
    return wikipedia.get_first_paragraph(json_content)


def ask_wolfram(wordlist):
    """
    Internal: (List) -> List

    Sends requests to WolframAlpha to ask for definitions
    """
    pass


# Functions
SOURCES = {
    'wikipedia' : ask_wikipedia,
    'wolfram'   : ask_wolfram,
}
