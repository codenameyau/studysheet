"""
StudySheet - Simple study sheets

Available Sources:
1. wikipedia
2. wolfram

Future Milestones:
1. Integrate with WikiMedia API
2. Integrate with WolframAlpha API
3. Save results as a pdf through PyTeX
4. Parse and include images in pdfs
"""
from knowledge import definitions


def main():
    """
    Reads content of a wordlist and generates a document
    containing definitions of concepts in 'studysheet-docs/'
    """
    FILENAME = 'wordlists/wiki-list.txt'
    # FILENAME = 'wordlists/wolfram-list.txt'
    wordlist = []
    with open(FILENAME) as f:
        wordlist = f.read().split('\n')
        definitions.create_studysheet(wordlist, 'wikipedia')


if __name__ == '__main__':
    main()
