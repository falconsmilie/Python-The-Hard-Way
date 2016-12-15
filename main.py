from project.parser import *
from project.lexicon import *

parser = Parser()
lexicon = Lexicon()

lists = [
	lexicon.scan('go to the west'),
	lexicon.scan('kill the bear'),
	lexicon.scan('bear princess'),
	lexicon.scan('eat the bear'),
]

for i in range(len(lists)):
	sentence = parser.parse_sentence(lists[i])
	if sentence:
		print sentence.subject
		print sentence.verb
		print sentence.object
		print
	else:
		print 'Try again'
		print
