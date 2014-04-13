"""
knowledge: transcriber.py

Module for transcribing and organizing information and
images into word and PDF documents.
"""
import time
import sys
import os
import docx


# Directory to output documents
OUTPUT_DIR = 'studysheets/'


def generate_doc(content, source, format):
    """
    Public: (List, String) -> None

    Creates a word document, formatted based on source.
    """
    _check_dir_exists()
    if format in WORD_FORMATTING:
        WORD_FORMATTING[format](content, source)
    else:
        sys.exit('Formatting for %s is missing' % format)


def _check_dir_exists():
    """
    Private: None -> None

    Checks if OUTPUT_DIR exists, if not create it.
    """
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print "Creating new folder: %s" % OUTPUT_DIR


def _save_document(document, source):
    """
    Private: (String) -> None

    Saves document and attaches time to filename.
    """
    timenow = time.strftime("-%b-%d-%Y-%H:%M")
    docname = OUTPUT_DIR + source + timenow + '.docx'
    document.save(docname)
    print "Saved document in: %s" % docname


def _format_simple(content, source):
    """
    Private: (List) -> None

    Generates document with simple formatting with a
    title heading and a paragraph for each content.
    """
    document = docx.Document()
    for entry in content:
        document.add_heading(entry['title'], 1)
        document.add_paragraph(entry['content'])
    _save_document(document, source)


WORD_FORMATTING = {
    'simple' : _format_simple,
}
