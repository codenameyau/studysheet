"""
StudySheet - Simple study sheets

Future Milestones:
1. Integrate with WolframAlpha API
2. Save results as a pdf through PyTeX
3. Caching results
"""
from studytools import definitions


def main():
    """
    Reads content of 'wordlist.txt' and generates a file
    containing definitions of concepts in 'output/'
    """
    FILENAME = 'wordlist.txt'
    wordlist = []
    with open(FILENAME) as f:
        wordlist = f.read().split('\n')
    concepts = definitions.get_definitions(wordlist, 'wikipedia')
    print concepts


if __name__ == '__main__':
    main()
