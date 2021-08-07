import os
import pickle


filler_words = {'real', 'largely', 'hopefully', 'very', 'well', 'easily', 'definitely', 'literally', 'surely', 'seriously', 'anyway', 'perhaps', 'entirely', 'especially', 'actually', 'relatively', 'frankly', 'fully', 'start', 'actual', 'fairly', 'absolutely', 'frequently', 'apparently', 'mostly', 'certainly', 'so', 'truly', 'specifically', 'whatever', 'primarily', 'okay', 'try', 'slightly', 'necessarily', 'particularly', 'totally', 'whoever', 'much', 'rather', 'essentially', 'basically', 'practically', 'significantly', 'obviously', 'right', 'most', 'possibly', 'ok', 'widely', 'typically', 'begin', 'whenever', 'simply', 'approximately', 'maybe', 'usually', 'quite', 'exactly', 'precisely', 'things', 'heavily', 'like', 'clearly', 'too', 'effectively', 'just', 'generally', 'ultimately', 'extremely', 'might', 'amazing', 'strongly', 'really', 'hardly', 'highly', 'completely', 'virtually', 'stuff', 'probably', 'nicely', 'wherever', 'badly'}
# print(filler_words)
# print(len(filler_words)) = 83

filler_words_path = '/Users/hoanguyen' + '/expresso_website/nlp_data/buzzwords.pickle' + '/expresso_website/nlp_data/filler_words.pickle'
# os.getenv('HOME')

if not os.path.isfile(filler_words_path):
 with open(filler_words_path, 'wb') as file:
  pickle.dump(filler_words, file, pickle.HIGHEST_PROTOCOL)
  file.close()