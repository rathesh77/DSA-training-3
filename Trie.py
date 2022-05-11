from Node import *

class Trie:
    def __init__(self):
        self.root = Node()

    # fonction de recherche d'un mot dans l'arbre
    def search(self, word):
        i = 0
        # on souhaite avoir un pointeur qui va pointer vers chaque Tri au fur et à mesure qu'on descend dans l'arbre
        ptr = self
        # On veut verifier la presence de chaque lettre de notre mot, dans ce même ordre, dans l'arbre
        # la variable "i" stock la lettre courante et sera incrementé à chaque iteration
        while i < len(word):
            # si la lettre courante fait partie des lettres "enfants" du tri courant
            if word[i] in ptr.root.children:
                # on deplace le pointeur sur le tri associé à la lettre courante
                ptr = ptr.root.children[word[i]]
                # on passe à la lettre prochaine
                i += 1
                # si on est arrivé à derniere lettre du mot, on retourne l'arbre courant
                if i == len(word):
                    return ptr
            # sinon, s'il ne reste plus de lettres dans le tri courant, on retourne None (ou NULL) car on peut deduire que le mot
            # n'est pas stocké dans l'arbre
            elif len(ptr.root.children.keys()) == 0:
                return None
            # autrement, on repete le processus pour tous les noeuds enfants restants
            else:
                for key in ptr.root.children:
                    w = ptr.root.children[key].search(word)
                    if w != None:
                        return w
                break
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
