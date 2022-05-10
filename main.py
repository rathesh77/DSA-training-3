from Trie import *
from Node import * 


T = Trie()

#T.insert('salut les amis')
T.root.children['a'] = Trie()
T.root.children['a'].root.children['b'] = Trie()
T.root.children['a'].root.children['b'].root.children['c'] = Trie()

res = T.search('bac')
print('fini')