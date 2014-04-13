"""
StudySheet - Simple study sheets

Future Milestones:
1. Integrate with WikiMedia API
2. Integrate with WolframAlpha API
3. Save results as a pdf through PyTeX
4. Parse and include images in pdfs
"""
from knowledge import definitions


def main():
    """
    Reads content of 'wordlist.txt' and generates a file
    containing definitions of concepts in 'output/'
    """
    # FILENAME = 'wordlist.txt'
    FILENAME = 'wolfram-wordlist.txt'
    wordlist = []
    with open(FILENAME) as f:
        wordlist = f.read().split('\n')
        definitions.create_studysheet(wordlist, 'wolfram')


if __name__ == '__main__':
    main()
