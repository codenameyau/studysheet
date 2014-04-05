"""
StudySheet - Simple study sheets

Future Milestones:
1. Integrate with WolframAlpha API
2. Add script arguments for filename
3. Save results as a pdf through PyTeX
4. Caching results
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


if __name__ == '__main__':
    main()
