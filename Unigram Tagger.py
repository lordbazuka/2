import nltk
nltk.download('brown')
nltk.download('punkt')
from nltk.corpus import brown
from nltk import UnigramTagger

brown_tagged_sents = brown.tagged_sents(categories = 'news')
brown_sents = brown.sents(categories = 'news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
tags = unigram_tagger.tag(brown_sents[2007])

print("\nDisplaying the tags from brown sents : \n", tags)
evaluation = unigram_tagger.evaluate(brown_tagged_sents)
print("\nEvaluation of brown tagged sents : ", evaluation)