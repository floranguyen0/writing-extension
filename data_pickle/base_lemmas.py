import os
import nltk
import pickle
# in case cant download wordnet, run the following code:
# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download('wordnet')


wordnet = nltk.corpus.wordnet
wordnet_words = [w for w in list(set(w for w in wordnet.words())) if ('_' not in w)]

base_lemmas = {}
for idx, word in enumerate(wordnet_words):
 
  if word not in base_lemmas.keys():
    related_lemmas = []
    wordnet_lemmas = [lm for lm in wordnet.lemmas(word)]
    while len(wordnet_lemmas):
      related_lemmas.extend(wordnet_lemmas)
    # wordnet_lemmas = gather all derivationally related forms of wordnet_lemmas
      wordnet_lemmas = [lm for lemma in wordnet_lemmas for lm in lemma.derivationally_related_forms() if (lm not in related_lemmas)]
    # related_lemma = wordnet_lemmas 
    related_words = list(set([lm.name().lower() for lm in related_lemmas]))
    related_words_len = [len(w) for w in related_words]
    base_lemma = related_words[related_words_len.index(min(related_words_len))]
    base_lemmas.update({word: base_lemma for word in related_words if (word != base_lemma)})

# type(base_lemmas) = <class 'dict'>
# print(base_lemmas)
# 'trade-in': 'trade_in'. Pay attention to '-'

base_lemmas_path = os.getenv('HOME') + '/nlp_data/base_lemmas.pickle'

if not os.path.isfile(base_lemmas_path):
   with open(base_lemmas_path ,'wb') as file:
       pickle.dump(base_lemmas, file, pickle.HIGHEST_PROTOCOL)
   file.close() 



