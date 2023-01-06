import re
import os


# Mad Libs


def Mad_libs():
    mad_text = open('./madlib.txt', 'r')
    mad_libs = mad_text.read()
    print(mad_libs)

    adjective_regex = re.compile('ADJECTIVE')
    noun_regex = re.compile('NOUN')
    verb_regex = re.compile('VERB')

    while adjective_regex.search(mad_libs) is not None:
        adjective = input('Enter an adjective:')
        mad_libs = adjective_regex.sub(adjective, mad_libs, 1)
    while noun_regex.search(mad_libs) is not None:
        noun = input('Enter a noun:')
        mad_libs = noun_regex.sub(noun, mad_libs, 1)
    while verb_regex.search(mad_libs) is not None:
        verb = input('Enter a verb:')
        mad_libs = verb_regex.sub(verb, mad_libs, 1)
    while noun_regex.search(mad_libs) is not None:
        noun = input('Enter a noun:')
        mad_libs = noun_regex.sub(noun, mad_libs, 2)

    print(mad_libs)


def regex_search():
    files = []
    for file in os.listdir('.'):
        if file.endswith('.txt'):
            files.append(file)

    input = input('Input supplied regular expression\n')
    search_regex = re.compile(input, re.I)

    file_list = []

    for fileName in files:
        open_file = open(fileName)
        read_file = open_file.read()
        if search_regex.search(read_file):
            file_list.append(fileName)
    print('Word:', file_list)


if __name__ == '__main__':
    Mad_libs()
