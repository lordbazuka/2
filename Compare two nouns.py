import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet

syn1 = wordnet.synsets('football')
syn2 = wordnet.synsets('soccer')

for s1 in syn1:
  for s2 in syn2:
    print("Path similarity of: ")
    print(s1, '(', s1.pos(), ')', '[', s1.definition(), ']') #Each synset has a name (e.g., Synset('football.n.01')), part of speech (e.g., noun 'n'), and a definition.
    print(s2, '(', s2.pos(), ')', '[', s2.definition(), ']')
    print(" is", s1.path_similarity(s2))
    print()