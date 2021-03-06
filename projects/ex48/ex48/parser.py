#loop

#match diff types of tuples in SVO setup
def match(word_list, expecting):
	if word_list:
		word = word_list.pop(0)

		if word[0] == expecting:
			return word
		else:
			return None
	else:
		return None


#peek at potential tuple to make decisions
# ”look at the next element in our tuple list, and then match to take one off and work with it.
def peek(word_list):
	if word_list:
		word = word_list[0]
		return word[0]
	else:
		return None


#skip things we dont care about like stop words
def skip(word_list, word_type):
	while peek(word_list) == word_type:
		match(word_list, word_type)


#sentence object to put results in

class Sentence(object):
	def __init__(self, subject, verb, obj):
		self.subject = subject[1] #this will be a noun
		self.verb = verb[1] #this will be a verb
		self.object = obj[1] #this will be another noun


class ParserError(Exception):
	pass


def parse_verb(word_list):
	skip(word_list, 'stop')

	if peek(word_list) == 'verb':
		return match(word_list, 'verb')
	else:
		raise ParserError("expected a verb next")

def parse_object(word_list):
	skip(word_list, 'stop')
	
	next_word = peek(word_list)
	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'direction':
		return match(word_list, 'direction')
	else:
		raise ParserError("expected a noun or direction next")

def parse_subject(word_list):
	skip(word_list, 'stop')
	next_word = peek(word_list)

	if next_word == 'noun':
		return match(word_list, 'noun')
	elif next_word == 'verb':
		return ('noun', 'player')
	else:
		raise ParserError("expected a verb next")

def parse_sentence(word_list):
	subj = parse_subject(word_list)
	verb = parse_verb(word_list)
	obj = parse_object(word_list)

	return Sentence(subj, verb, obj)
