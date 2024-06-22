import nltk
nltk.download('brown')
from nltk.corpus import brown
brown.categories()

brown.words(categories = 'news')

brown.fileids()

brown.words(fileids='cg22')

brown.sents(categories=['news','editorial','reviews'])