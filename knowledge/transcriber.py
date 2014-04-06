"""
knowledge: transcriber.py

Module for transcribing and organizing information and
images into word and PDF documents.
"""
import sys
import docx


def generate_doc(content, source):
    """
    Public: (List, String) -> None

    Creates a word document, formatted based on source.
    """
    if source in WORD_FORMATTING:
        WORD_FORMATTING[source](content)
    else:
        sys.exit('Formatting for %s is missing' % source)


def _format_wikipedia_doc(content):
    """
    Private: (List) -> None

    Generates document with custom wikipedia formatting.
    """
    document = docx.Document()
    print content


WORD_FORMATTING = {
    'wikipedia' : _format_wikipedia_doc
}
