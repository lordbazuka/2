import nltk
nltk.download('punkt')
from nltk.stem import LancasterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

lancaster = LancasterStemmer()

terms = ["enjoy", "enjoying", "enjoyed", "enjoyable", "enjoyment", "enjoyful"]

print("\n1. Performing lancaster stemming on the words")
for each_term in terms:
  print(lancaster.stem(each_term))

sentence = "Heya, Why is it so with the dancers that when dancers dance, they dance as if they are dancing in the air?"

print("\n2. Performing lancaster stemming on a sentence")
words = word_tokenize(sentence, language = 'english')
for each_word in words:
  print(lancaster.stem(each_word))

print("\n3. Performing lancaster stemming on a text file - one sentence at a time")

my_file = open("my.txt")
my_lines_list = my_file.readlines()

words = word_tokenize(my_lines_list[0], language = 'english')
for each_word in words:
  print(lancaster.stem(each_word))
