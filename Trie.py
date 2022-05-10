from Node import *

class Trie:
    def __init__(self):
        self.root = Node()

    def search(self, word):
        #TODO
        i = 0
        ptr = self
        while i < len(word):
            print(i, len(word))
            if word[i] in ptr.root.children:
                ptr = ptr.root.children[word[i]]
                i += 1
                if i == len(word):
                    return ptr
            elif len(ptr.root.children.keys()) == 0:
                return None
            else:
                print('toto')
                for key in ptr.root.children:
                    w = ptr.root.children[key].search(word)
                    print(w, key)
                    if w != None:
                        print(key)
                        return w
                break
        
        return None
        
    
    def insert(self, word):
        #TODO
        i = 0
        ptr = self
        while (True):
            found = ptr.search(word[i])
            print('wesh')
            if found != -1:
                ptr = found
                i += 1
            else:
                break

        return ptr
        ptr = self.root
        while i < len(word):
            if word[i] in ptr.children:
                ptr = ptr.children[word[i]]
                i+=1
            else:
                #ptr.children[word[i]] = Node()
                #i += 1
                break
        
        while i < len(word):
            ptr.children[word[i]] =  Node()
            ptr = ptr.children[word[i]]
            i += 1

        return self
        
    def collectAllWords(self, node=None, word="", words=[]):
        #TODO
        pass

    def autocomplete(self, prefix):
        currentNode = self.search(prefix)
        if not currentNode:
            return None
        return self.collectAllWords(currentNode)
