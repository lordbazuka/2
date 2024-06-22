import nltk
from nltk import CFG, ChartParser, word_tokenize

grammar1 = CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'a' | 'my'
N -> 'bird' | 'balcony'
V -> 'saw'
P -> 'in'
""")

sentence = "I saw a bird in my balcony"
all_tokens = word_tokenize(sentence)
print(all_tokens)

parser = ChartParser(grammar1)

for tree in parser.parse(all_tokens):
    print(tree)
    tree.draw()
