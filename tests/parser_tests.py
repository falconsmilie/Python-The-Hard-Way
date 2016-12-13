from nose.tools import *
from ex48.lexicon import *
from ex48.parser import *
from ex48.sentence import *
from copy import deepcopy

# Parser Tests #

lexicon = Lexicon()
parser = Parser()

test_list = {
    'direction': lexicon.scan('south'),
    'noun': lexicon.scan('door'),
    'error': lexicon.scan('blah'),
    'verb': lexicon.scan('eat'),
    'verb': lexicon.scan('go to the east'),
    'stop': lexicon.scan('the bear is fat'),
    'number': lexicon.scan('1234')
}

def test_peek():
    test_list_copy = deepcopy(test_list)

    for test_type, word_type_pair in test_list_copy.items():
        assert_equal(parser.peek(word_type_pair), test_type)

def test_match():
    test_list_copy = deepcopy(test_list)

    for test_type, word_type_pair in test_list_copy.items():
        expects = (test_type, word_type_pair[0][1])
        assert_equal(parser.match(word_type_pair, test_type), expects)

def test_skip():
    test_list_copy = deepcopy(test_list)

    expected_list = {
        'direction': lexicon.scan('south'),
        'noun': lexicon.scan('door'),
        'error': lexicon.scan('blah'),
        'verb': lexicon.scan('eat'),
        'verb': lexicon.scan('go to the east'),
        'stop': lexicon.scan('bear is fat'),
        'number': lexicon.scan('1234')
    }

    for test_type, word_type_pair in test_list_copy.items():
        parser.skip(word_type_pair, 'stop')
        assert_equal(word_type_pair, expected_list[test_type])

def test_parse_verb():
    test_list_verb = [
        lexicon.scan('in the eat'),
        lexicon.scan('go to the princess'),
        lexicon.scan('to the kill'),
        lexicon.scan('stop'),
    ]

    expected_list = [
        lexicon.scan('eat'),
        lexicon.scan('go'),
        lexicon.scan('kill'),
        lexicon.scan('stop'),
    ]

    for i in range(len(test_list_verb)):
        assert_equal(parser.parse_verb(test_list_verb[i]), expected_list[i][0])

    fail_list = [
        lexicon.scan('north'),
        lexicon.scan('forget the princess'),
        lexicon.scan('murder the bear'),
        lexicon.scan('find the gold'),
    ]

    for i in range(len(fail_list)):
        assert_raises(ParserError, parser.parse_verb, fail_list[i])

