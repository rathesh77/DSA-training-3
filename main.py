from Trie import *
from Node import * 


T = Trie()

#T.insert('salut les amis')


res2 = T.insert('arme')
res2 = T.insert('armure')
res2 = T.insert('alarme')

res2 = T.insert('toto')
res2 = T.insert('alr')
res2 = T.insert('rater')
res2 = T.insert('armurier')

print('fini')
collects = T.collectAllWords()
autocomplete = T.autocomplete('arm')

res2 = T.search('rat')
print('fini')
