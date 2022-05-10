from Node import *
# begin et end inclus
def slice(str, begin, end):
    newstr = ''
    for i in range (begin, end +1):
        newstr += str[i]
    return newstr

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
        i = len(word)-1
        ptr = self
       
        while (i >= 0):
            look_up = ptr.search(slice(word, 0, i))
            if look_up != None:
                ptr = look_up
                break
            i-= 1
        i = i +1 
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
        return self.collectAllWords(currentNode, '', [])
