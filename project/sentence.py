
class Sentence(object):

    def __init__(self, subject, verb, obj):
        """ Structure for our sentences """

        # Sentence.subject
        # This is the subject of any sentence, but could default to "player" 
        # most of the time since a sentence of, "run north" is implying 
        # "player run north". This will be a noun.
        self.subject = subject[1]

        # Sentence.verb
        # This is the action of the sentence. In "run north" it would be "run". 
        # This will be a verb.
        self.verb = verb[1]

        # Sentence.object
        # This is another noun that refers to what the verb is done on. In our 
        # game we separate out directions which would also be objects. In 
        # "run north" the word "north" would be the object. In "hit bear" the 
        # word "bear" would be the object.
        self.object = obj[1]
