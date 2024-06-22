import nltk
nltk.download('brown')
nltk.download('punkt')
from nltk.corpus import brown
from nltk import word_tokenize
from nltk import RegexpTagger

brown_sents = brown.sents(categories = 'news')
brown_tagged_sents = brown.tagged_sents(categories = 'news')

import nltk
nltk.download('brown')
nltk.download('punkt')
from nltk.corpus import brown
from nltk import word_tokenize
from nltk import RegexpTagger
brown_sents = brown.sents(categories = 'news')
brown_tagged_sents = brown.tagged_sents(categories = 'news')

patterns = [
(r'.*ing$', 'VBG'), 
(r'.*ed$', 'VBD'),
(r'.*es$', 'VBZ'),
(r'.*ould$', 'MD'), 
(r'.*\'s$', 'NN$'), 
(r'.*s$', 'NNS'), 
(r'^-?[0-9]+(\.[0-9]+)?$', 'CD'), 
(r'.*', 'NN') 
]

regexp_tagger = nltk.RegexpTagger(patterns)
regexp_tagger.tag(brown_sents[3])