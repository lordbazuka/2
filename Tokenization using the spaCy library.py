!pip install spacy
from spacy.lang.en import English
nlp = English()

text =  "Founded in 2002, SpaceX’s mission is to enable humans to become a spacefaring civilization and a multi-planet species by building a self-sustaining city on Mars. In 2008, SpaceX’s Falcon 1 became the first privately developed liquid-fuel launch vehicle to orbit the Earth."

my_doc = nlp(text)

token_list = []
for token in my_doc:
  token_list.append(token.text)

token_list
print(token_list)