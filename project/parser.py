
from project.sentence import *

class ParserError(Exception):
    """ Returns ParserError """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Parser(object):

    def parse_sentence(self, word_list):
        """ Finds subject, verb and object in list and returns Sentence. """

        try:
            subj = self.parse_subject(word_list)
            verb = self.parse_verb(word_list)
            obj = self.parse_object(word_list)

            return Sentence(subj, verb, obj)

        except ParserError as e:
            print e.value

        return None


    def parse_verb(self, word_list):
        """ Check we have a verb """

        self.skip(word_list, 'stop')

        if self.peek(word_list) == 'verb':
            return self.match(word_list, 'verb')

        else:
            raise ParserError(
                'Expected a verb. Got a %s.' % self.peek(word_list)
            )


    def parse_object(self, word_list):
        """ Check we have an object; either noun or direction. """

        self.skip(word_list, 'stop')

        next_word = self.peek(word_list)

        if next_word == 'noun':
            return self.match(word_list, 'noun')

        elif next_word == 'direction':
            return self.match(word_list, 'direction')

        else:
            raise ParserError(
                'Expected a noun or direction. Got a %s.' % next_word
            )


    def parse_subject(self, word_list):
        """ Check for the subject noun or handle the player verb. """

        self.skip(word_list, 'stop')

        next_word = self.peek(word_list)

        if next_word == 'noun':
            return self.match(word_list, 'noun')

        elif next_word == 'verb':
            return ('noun', 'player')

        else:
            raise ParserError('Expected a verb. Got a %s.' % next_word)

    def parse_number(self, word_list):
        """ Check for a number """

        self.skip(word_list, 'stop')

        next_word = self.peek(word_list)

        if next_word == 'number':
            return self.match(word_list, 'number')

        else:
            raise ParserError('Expected a number. Got a %s' % next_word)
            

    def peek(self, word_list):
        """ Allows us to 'peek' at what the next word in the list is. """

        if word_list:
            word = word_list[0]
            return word[0]
        else:
            return None


    def match(self, word_list, expecting):
        """ Confirm we have right word type, remove from list and return it. """

        if word_list:

            word = word_list.pop(0)

            if word[0] == expecting:
                return word
            else:
                return None
        else:
            return None


    def skip(self, word_list, word_type):
        """ Skip words that aren't useful to us, such as 'at' and 'the'. """

        while self.peek(word_list) == word_type:
            self.match(word_list, word_type)

