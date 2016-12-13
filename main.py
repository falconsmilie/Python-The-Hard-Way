from project.parser import *
from project.lexicon import *

parser = Parser()
lexicon = Lexicon()

lists = [
	lexicon.scan('go to the west'),
	lexicon.scan('kill the bear'),
	lexicon.scan('eat the bear'),
	lexicon.scan('bear princess'),
]

for i in range(len(lists)):
	sentence = parser.parse_sentence(lists[i])
	print sentence.subject
	print sentence.verb
	print sentence.object
	print
