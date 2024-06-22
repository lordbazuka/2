import nltk
nltk.download('wordnet')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

wordnet = WordNetLemmatizer()

print("\n1. Performing WordNet lemmatization on single Words")
print(wordnet.lemmatize("corpora"))
print(wordnet.lemmatize("best"))
print(wordnet.lemmatize("geese"))
print(wordnet.lemmatize("feet"))
print(wordnet.lemmatize("cacti"))

print("\n2. Performing WordNet lemmatization on a sentence")

sentence = "Heyaa Reeba, how are you doing? Keep digging in for the sentences to observe lemmatization!"

list_words = nltk.word_tokenize(sentence)
print("\nConverting the sentence into a list of words")
print(list_words)

final = ' '.join([wordnet.lemmatize(each_word, pos = 'v') for each_word in list_words])
print("\nAfter applying wordnet lemmatizer, the result is....")
print(final)