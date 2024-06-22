# using Recursive Descent Parser
import nltk
grammar1 = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
V -> "saw" | "ate" | "walked"
NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
Det -> "a" | "an" | "the" | "my"
N -> "man" | "dog" | "cat" | "telescope" | "park"
P -> "in" | "on" | "by" | "with"
""")

sent = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
  print(tree)
  tree.draw()

# *****************************************************************************

import nltk
nltk.download('punkt')
from nltk import tokenize

grammar1 = nltk.CFG.fromstring("""
S -> VP
VP -> VP NP
NP -> Det NP
Det -> 'that'
NP -> singular Noun
NP -> 'flight'
VP -> 'Book'
""")

sentence = "Book that flight"

for index in range(len(sentence)):
  all_tokens = tokenize.word_tokenize(sentence)
print("Token: ",all_tokens)
parser = nltk.ChartParser(grammar1)
for tree in parser.parse(all_tokens):
  print(tree)
  tree.draw()
