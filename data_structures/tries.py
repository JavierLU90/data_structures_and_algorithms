class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
    
    def add(self, word):
        current = self.root
        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]
        current[self.end_symbol] = True


'''
TRIES

Tries are one of my favorite data structures, I've used them often in the past for natural language processing tasks. 
In Python, a trie is easily implemented as a nested tree of dictionaries where each key is a character that maps to the next character in a word. 

For example, the words:
    hello
    help
    hi

Would be represented as:
{
	"h": {
		"e": {
			"l": {
				"l": {
					"o": {
						"*": True
					}
				},
				"p": {
					"*": True
				}
			}
		},
		"i": {
			"*": True
		}
	}
}

The * character (paired with True instead of a dictionary) is used to indicate the end of a word.

A trie is also often referred to as a "prefix tree" because it can be used to efficiently find all of the words that start with a given prefix.


'''