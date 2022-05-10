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
        #TODO
        i = 0
        ptr = self
        while i < len(word):
            #print(i, len(word))
            if word[i] in ptr.root.children:
                ptr = ptr.root.children[word[i]]
                i += 1
                if i == len(word):
                    return ptr
            elif len(ptr.root.children.keys()) == 0:
                return None
            else:
                ##print('toto')
                for key in ptr.root.children:
                    w = ptr.root.children[key].search(word)
                    #print(w, key)
                    if w != None:
                        #print(key)
                        return w
                break
        
        return None
        
    
    def insert(self, word):
        #TODO
        i = len(word)-1
        ptr = self
       
        while (i >= 0):
            look_up = ptr.search(slice(word, 0, i))
            if look_up != None:
                ptr = look_up
                break
            i-= 1
        #return None
        i = i +1 
        while i < len(word):
            ptr.root.children[word[i]] = Trie()
            ptr = ptr.root.children[word[i]]
            i+=1
        
  
        return ptr
        
    def collectAllWords(self, node=None, word="", words=[]):
        #TODO
        pass

    def autocomplete(self, prefix):
        currentNode = self.search(prefix)
        if not currentNode:
            return None
        return self.collectAllWords(currentNode)
