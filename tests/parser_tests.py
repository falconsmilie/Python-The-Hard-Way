from nose.tools import *
from ex48.lexicon import *
from ex48.parser import *
from ex48.sentence import *

# Parser Tests #

lexicon = Lexicon()
parser = Parser()

test_list = {
    'direction': lexicon.scan('south'),
    'noun': lexicon.scan('door'),
    'error': lexicon.scan('blah'),
    'verb': lexicon.scan('eat'),
}

def test_peek():
    for test_type, word_type_pair in test_list.items():
        assert_equal(parser.peek(word_type_pair), test_type)
