from Node import *

class Trie:
    def __init__(self):
        self.root = Node()

    def search(self, word):
        i = 0
        ptr = self
        while i < len(word):
            if word[i] in ptr.root.children:
                ptr = ptr.root.children[word[i]]
                i += 1
                if i == len(word):
                    return ptr
            elif len(ptr.root.children.keys()) == 0:
                return None
            else:
                for key in ptr.root.children:
                    w = ptr.root.children[key].search(word)
                    if w != None:
                        return w
                break
        
        return None
        
    
    def insert(self, word):
        i = 0
        ptr = self
       
        while (i < len(word)):
            if word[i] in ptr.root.children:
                ptr = ptr.root.children[word[i]]
                i+=1
            else:
                break

        while i < len(word):
            ptr.root.children[word[i]] = Trie()
            ptr = ptr.root.children[word[i]]
            i+=1
        ptr.end = '*'
        
  
        return ptr
        
    def collectAllWords(self, node=None, word="", words=[]):
        #TODO
        ptr = node
        if ptr == None:
            ptr = self
        if hasattr(ptr, 'end'):
            words.append(word)
        if len( ptr.root.children) == 0:
            return words
        else:
            for key in ptr.root.children:
                next = ptr.root.children[key]
                words = next.collectAllWords(None, word + key, words)
        return words

    def autocomplete(self, prefix):
        currentNode = self.search(prefix)
        if not currentNode:
            return None
        return self.collectAllWords(currentNode, prefix, [])
