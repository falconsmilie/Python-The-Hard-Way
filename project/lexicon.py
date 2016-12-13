
class Lexicon(object):

    def scan(self, input_words):
        """ Scan a list of words and determine what 'type' they are """

        input_word_list = input_words.split(' ')

        scanresult = []

        for test_word in input_word_list:

            type_of_word = self.analyse_word(test_word.lower())

            if (type_of_word == 'number'):
                # test_word is initially a string
                test_word = int(test_word)

            scanresult.append((type_of_word, test_word))

        return scanresult


    def analyse_word(self, word):
        """ Tests 'type' of word and returns the type """

        rules = {
            'direction': ['north','south', 'east', 'west'],
            'verb': ['go', 'stop', 'eat', 'kill'],
            'stop': ['the', 'in', 'of', 'from', 'at', 'it', 'to'],
            'noun': ['door', 'bear', 'princess', 'cabinet'],
        }

        word_type = 'error'

        if self.is_number(word):
            word_type = 'number'

        for rule, rule_list in rules.items():
            if word in rule_list:
                word_type = rule
                break

        return word_type


    def is_number(self, s):
        """ Determines if the value is an int """
        try:
            return int(s)
        except ValueError:
            return None