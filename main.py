
# NLTK imports
import nltk
from nltk.tree import TreePrettyPrinter

# SPACY imports
import spacy

def print_language(language: str):
    """
    Print '*' character with language name
    :param language: the language which will be print
    """
    if language == 'en':
        print('*'*20 + '  ENGLISH  ' + '*'*20)
    elif language == 'fr':
        print('*' * 20 + '  FRENCH  ' + '*' * 20)
    elif language == 'de':
        print('*' * 20 + '  GERMAN  ' + '*' * 20)
    elif language == 'it':
        print('*'*20 + '  ITALIAN  ' + '*'*20)

def extract_sentences(language: str):
    """
    Extract sentences of the specified language from the corresponding file
    :param language: the current language
    :return: a list of sentences
    """

    # open file
    file_open = open(f'{language}_sentences.txt','r')
    # read the first row
    row = file_open.readline()
    sentences = []

    # until the row is not empty
    while row != '':
        # add the sentences to the list, removing return carriage
        sentences.append(row.replace('\n',''))
        # read the next line from the file
        row = file_open.readline()

    return sentences

def select_package(language: str):
    """
    Return the spacy language model to load depending on selected language
    :param language: the current language
    :return: the corresponding language package
    """
    if language == 'en':
        return 'en_core_web_sm'
    elif language == 'de':
        return 'de_core_news_sm'
    elif language == 'fr':
        return 'fr_core_news_sm'
    elif language == 'it':
        return 'it_core_news_sm'

def tree_generation(sentence: str, grammar: str):
    """
    Create POS-Tagging and generate the Syntatic Tree
    :param sentence: the current sentence
    :param grammar: the predefined grammar for the current language
    :return:
    """
    new_grammar = grammar
    pos_sentence = []
    print(sentence)

    # for each word in sentence
    for t in sentence:
        # append the word to a list
        pos_sentence.append(t.text)
        # add the new POS-Tag to the predefined grammar
        new_grammar += f'{t.pos_} -> "{t.text}"\n'
    # create the parser object from the new grammar
    result = nltk.ChartParser(nltk.CFG.fromstring(new_grammar))
    # extract the syntatic tree
    trees = list(result.parse(pos_sentence))
    # print the syntatic tree
    print(TreePrettyPrinter(trees[0]).text())



if __name__ == "__main__":

    # list of languges
    languages = ['en','de','fr','it']

    # english-german predefined grammar
    en_de_grammar = """
                    S -> NP VP PUNCT | NP VP | PUNCT NP VP PUNCT
                    NP -> NOUN | DET NP | ADJ NP
                    VP -> VP NP | VERB | VP ADV | VP PUNCT 
                    """

    # french-italian predefined grammar
    fr_it_grammar = """
                S -> NP VP PUNCT | NP VP | PUNCT NP VP PUNCT
                NP -> NOUN | DET NP | NP ADJ  
                VP -> VP NP | VERB | VP ADV | VP PUNCT 
                """

    # for each language
    for lan in languages:
        # print the header containing tha language name
        print_language(lan)
        # read sentences from specific language file
        sentences = extract_sentences(lan)
        # select spacy language model
        package = select_package(lan)
        # load spacy language model
        language_package = spacy.load(package)
        # for each sentence read from the file
        for s in sentences:
            # wrap the phrase in spacy language object
            sentence = language_package(s)
            # depending on language call 'tree_generation' function giving the right grammar
            if lan == 'en' or lan == 'de':
                tree_generation(sentence, en_de_grammar)
            else:
                tree_generation(sentence, fr_it_grammar)

