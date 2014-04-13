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


def create_studysheet_doc(wordlist, source, docformat='simple'):
    """
    Public: (List, String, String) -> None

    Creates a study sheet document from wordlist by requesting
    data from source. Outputs content in desired format.

    Example:
    >> create_studysheet(['love', 'bug'], 'wikipedia', 'simple')
    """
    if source in SOURCES:
        content = SOURCES[source](wordlist)
        transcriber.generate_doc(content, source, docformat)
    else:
        sys.exit("EXIT: %s is not available" % source)


def ask_wikipedia(wordlist):
    """
    Internal: (List) -> List

    Sends requests to wikipedia to retrieve definitions.
    """
    content = wikipedia.send_requests(wordlist)
    return wikipedia.get_first_paragraph(content)


def ask_wolfram(wordlist):
    """
    Internal: (List) -> List

    Sends requests to WolframAlpha to ask for questions.
    """
    return wolfram.send_requests(wordlist)


# Functions
SOURCES = {
    'wikipedia' : ask_wikipedia,
    'wolfram'   : ask_wolfram,
}
