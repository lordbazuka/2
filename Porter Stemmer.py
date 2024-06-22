import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

porter = PorterStemmer()

terms = ["gene", "genes", "genesis", "genetic", "generic", "general"]

print("\n1. Performing porter stemming on the words")
for each_term in terms:
  print(porter.stem(each_term))

sentence = "Heya, do you know it is important to be pythonly while pythoning with python language. Stay being a pythoner"

print("\n2. Performing porter stemming on a sentence")
words = word_tokenize(sentence, language = 'english')
for each_word in words:
  print(porter.stem(each_word))

