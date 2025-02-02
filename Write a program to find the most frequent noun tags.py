nltk.download('universal_tagset')
from nltk.corpus import brown
noundist = nltk.FreqDist(w2 for ((w1, t1), (w2, t2)) in
      nltk.bigrams(brown.tagged_words(tagset="universal"))
      if w1.lower() == "the" and t2 == "NOUN")
noundist.most_common(10)