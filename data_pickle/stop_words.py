import nltk
import os
import pickle


# in case cant download stop words, run the following code:
# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download('stopwords')

stop_words = set(nltk.corpus.stopwords.words("english"))
# print(stop_words)

# type(stop_words) = <class 'list'>
# stop_words[1:5] = ['me', 'my', 'myself', 'we']

stop_words_path = os.getenv('HOME') + '/nlp_data/stop_words.pickle'

if not os.path.isfile(stop_words_path):
 with open(stop_words_path, 'wb') as file:
  pickle.dump(stop_words, file, pickle.HIGHEST_PROTOCOL)
  file.close()


