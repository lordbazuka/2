import nltk
nltk.download('punkt')
from nltk.stem.snowball import SnowballStemmer

snowball_english = SnowballStemmer("english")
snowball_english = SnowballStemmer("dutch")

print("\n1. Performing snowball stemming one word")
word = snowball_english.stem("Vibing")
print(word)

terms = ["reeba", "cheerful", "bravery","drawing", "satisfactorily", "publisher", "painful", "hardworking","keys"]

print("\n2. Performing snowball stemming on a set of english language words")
for each_term in terms:
  print(snowball_english.stem(each_term))

terms2 = ["reeba", "bessen", "vriendelijkheid", "hobbelig"]

print("\n3. Performing snowball stemming on a set of dutch language words")
for each_term in terms2:
  print(snowball_english.stem(each_term))

