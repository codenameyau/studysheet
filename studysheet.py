"""
StudySheet - Automated Study Sheets

This is a sample command-line program that uses
the knowledge module to create study sheets.

Available Sources:
1. wikipedia
2. wolfram
"""
from knowledge import definitions


def main():
    """
    Reads content of a wordlist and generates a document
    containing definitions of concepts in 'studysheet-docs/'
    """
    FILENAME = 'wordlists/wiki-list.txt'
    # FILENAME = 'wordlists/wolfram-list.txt'
    with open(FILENAME) as f:
        wordlist = f.read().rstrip().split('\n')
        definitions.create_studysheet_doc(wordlist, 'wikipedia', 'simple')


if __name__ == '__main__':
    main()
