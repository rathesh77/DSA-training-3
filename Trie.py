from Node import *

class Trie:
    def __init__(self):
        self.root = Node()

    # fonction de recherche d'un mot dans l'arbre
    def search(self, word):
        i = 0
        ptr = self
        # on parcours l'arbre en profondeur tant que chaque objet Trie 
        # comporte le n-eme caractere de word
        while i < len(word) and word[i] in ptr.root.children:
            ptr = ptr.root.children[word[i]]
            if i == len(word) - 1:
                return ptr
            i += 1
                
        return None
    # fonction d'insertion d'un mot dans l'arbre
    def insert(self, word):
        i = 0
        ptr = self
        # on cherche s'il existe deja un debut de notre chaine "word"
        # par exemple si on veut inserer "TOTO" mais on a deja la chaine "TO" stocké dans l'arbre,
        # on commence à partir du noeud "O"
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
        # On marque la fin de la chaine
        ptr.end = '*'
        return ptr
     
    def collectAllWords(self, node=None, word="", words=None):
        #TODO
        if words == None:
            words = []
        ptr = node
        if ptr == None:
            ptr = self
        #Si on est arrivé à une profondeur avec le flag end, on ajoute le mot à notre tableau
        if hasattr(ptr, 'end'):
            words.append(word)
        # S'il ne reste plus de profondeur restant, c'est à dire aucun caractere à parcourir, on retourne 
        # le tableau des mots
        if len( ptr.root.children) == 0:
            return words
        # sinon, on parcours les noeuds enfants en recurant
        else:
            for key in ptr.root.children:
                next = ptr.root.children[key]
                words = next.collectAllWords(None, word + key, words)
        return words

    def autocomplete(self, prefix):
        currentNode = self.search(prefix)
        if not currentNode:
            return None
        return self.collectAllWords(currentNode, prefix)
