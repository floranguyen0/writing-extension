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
words = [w for w in list(set(w for w in wordnet.words())) if ('_' not in w)]
pos_map = {'nouns': ['n'], 'adjectives': ['a', 's'], 'verbs': ['v'], 'adverbs': ['r']}

all_synonyms = {'nouns': {}, 'verbs': {}, 'adjectives': {}, 'adverbs': {}}
for idx, word in enumerate(words):
  if (idx % 5000) == 0:
    print ('processing word ' + str(idx) + '...')

  for pos in pos_map.keys():
    synonyms = []
    for synset in wordnet.synsets(word, pos=pos_map[pos]):
      synonyms.extend([syn.lower() for syn in synset.lemma_names() if ('_' not in syn)])
    synonyms = list(set(synonyms) - set([word]))
    if len(synonyms):
      all_synonyms[pos][word] = synonyms

# print (all_synonyms)
# 'so-so': ['acceptably', 'tolerably']. pay attention to '-'

synonyms_path = os.path.join(os.getcwd(), 'nlp_data/synonyms.pickle')
# os.getenv('HOME')
if not os.path.isfile(synonyms_path):
 with open(synonyms_path, 'wb') as file:
  pickle.dump(all_synonyms, file, pickle.HIGHEST_PROTOCOL)
  file.close()



