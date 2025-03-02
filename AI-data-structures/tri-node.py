#tries are useful for word-based AI

class TrieNode:
    def __init__(self):
        #Initialized with an empty dictionary for children and an end-of-word flag
        self.children = {}
        self.is_end_of_word = False #Boolean to mark end of word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        #insert word
        node = self.root
        for char in word: #iterate over each char in the word
            if char not in node.children: 
                node.children[char] = TrieNode() #create a new trie node
            node = node.children[char] #move to next
        node.is_end_of_word = True #mark the last node as the end of word
    
    def search(self, word):
        #search for word in tri
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word # return if it is a complete word
    
    def starts_with(self, prefix):
        #check if the word in the trie starts with the given prefix
        node = root.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True # prefix found
        

