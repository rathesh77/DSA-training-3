from Trie import *
from Node import * 


T = Trie()

#T.insert('salut les amis')


res2 = T.insert('arme')
res2 = T.insert('armure')
res2 = T.insert('alarme')

res2 = T.insert('toto')
res2 = T.insert('alr')

print('fini')
collects = T.collectAllWords()
autocomplete = T.autocomplete('arm')
print('fini')