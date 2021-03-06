"""Even More Pracices (on Function Returns).

### Usage

```
import ex25
sentence = 'All good things come to those who wait.'
words = ex25.break_words(sentence)
words
sorted_words = ex25.sort_words(words)
sorted_words
```
"""
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sort the words."""
	return sorted(words)

def print_first_word(words):
	"""Print the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Print the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Take in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Print the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sort the words then print the first and last ones."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)


