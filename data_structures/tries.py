class Trie:
    def search_level(self, current_level, current_prefix, words):
        '''This recursive function collects all complete words starting from the current trie level. 
        It takes the current dictionary level, the accumulated prefix so far, 
        and the collection of words found.'''
        if self.end_symbol in current_level:
            words.append(current_prefix)
        for letter in sorted(current_level.keys()):
            if letter != self.end_symbol:
                extended_prefix = current_prefix + letter
                self.search_level(current_level[letter], extended_prefix, words)
        return words

    def words_with_prefix(self, prefix):
        '''This finds all words in the trie that begin with a given prefix.'''
        collected_words = []
        current_level = self.root
        for letter in prefix:
            if letter not in current_level:
                return []
            current_level = current_level[letter]
        return self.search_level(current_level, prefix, collected_words)
    
    def exists(self, word):
        '''It takes a word as input, and should return True if the word exists in the trie, 
        and False if it doesn't.'''
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return self.end_symbol in current

    def find_matches(self, document):
        ''' It takes an entire document string as input and returns a set() 
        of all the words from the trie that occur in the document.'''
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                char = document[j]
                if char not in level:
                    break
                level = level[char]
                if self.end_symbol in level:
                    substring = document[i:j+1]
                    matches.add(substring)
        return matches
    
    def advanced_find_matches(self, document, variations):
        ''' It takes an entire document and a dictionary of character variations as input, 
        and should return a set() of all the words in the trie that exist in the document 
        as continuous substrings, even if the word had a variation character instead of the original.'''
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch in variations:
                    ch = variations[ch]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches
    
    def longest_common_prefix(self):
        '''It returns the longest common prefix among the words in the trie.'''
        current = self.root
        prefix = ""
        while True:
            children = list(current.keys())
            if self.end_symbol in children:
                break
            if len(children) == 1:
                char = children[0]
                prefix += char
                current = current[char]
            else:
                break
        return prefix

    def add(self, word):
        '''It takes a word as input, and should add it to the trie.'''
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"


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