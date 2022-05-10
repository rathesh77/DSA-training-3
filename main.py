from Trie import *
from Node import * 


T = Trie()

#T.insert('salut les amis')
T.root.children['a'] = Trie()
T.root.children['a'].root.children['b'] = Trie()
T.root.children['a'].root.children['c'] = Trie()

T.root.children['a'].root.children['c'].root.children['d'] = Trie()

res = T.search('e')
res2 = T.insert('arme')
print('fini')