import os, os.path
path = os.path.expanduser('~/natural_language_toolkit_data')
if not os.path.exists(path):
  os.mkdir(path)
os.path.exists(path)

from nltk.corpus.reader import WordListCorpusReader
reader_corpus = WordListCorpusReader('.',['natural_language_toolkit_data/content/wordfile.txt'])
reader_corpus.words()

