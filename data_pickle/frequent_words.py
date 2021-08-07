import os
import  pickle
from re import I




frequent_words_text_path = os.getenv('HOME') + '/expresso_website/nlp_data/frequent_words.txt'

with open(frequent_words_text_path,'rt') as file:
    file =  file.read().splitlines()


i = 0
frequent_words = {}
for word in file:
      frequent_words[word] = i 
      i += 1

# print(len(frequent_words)) = 1000

frequent_words_pickle_path = os.getenv('HOME') + '/nlp_data/frequent_words.pickle'

if not os.path.isfile(frequent_words_pickle_path):
 with open(frequent_words_pickle_path, 'wb') as file:
  pickle.dump(frequent_words, file, pickle.HIGHEST_PROTOCOL)
  file.close()

