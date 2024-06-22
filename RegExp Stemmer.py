import nltk
nltk.download('punkt')
from nltk.stem import RegexpStemmer

regexp = RegexpStemmer('ing$|s$|e$|able$|ment$|less$|ly$', min=4)

print("\n1. Performing regexp stemming on one word at a time")
print(regexp.stem('cars'))
print(regexp.stem('bee'))
print(regexp.stem('compute'))

terms = ["reebas", "stemming", "mentally", "ease","rockstar", "frictionless", "management","flowers","advisable"]

print("\n2. Performing regexp stemming on a list of words")
for each_term in terms:
  print(regexp.stem(each_term)) 

