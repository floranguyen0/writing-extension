import os
import nltk
import  pickle
# in case cant import cmudict, run the following code:
# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

# nltk.download('cmudict')


# The Carnegie Mellon Pronouncing Dictionary [cmudict]
cmudict = nltk.corpus.cmudict.dict()

# cmudict_item = cmudict.items()
# first_five = list(cmudict_item)[:5]
# print(first_five) = ('a', [['AH0'], ['EY1']]),  ('a.', [['EY1']]), ('a42128', [['EY1', 'F', 'AO1', 'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T']]), ('aaa', [['T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1']]), ('aaberg', [['AA1', 'B', 'ER0', 'G']])]
# => cmudict = {'a': [['AH0'], ['EY1']], 'a.': [['EY1']],...}
cmu = {word: cmudict[word][0] for word in cmudict.keys()}

# cmudict_item = cmu.items()
# first_five = list(cmudict_item)[:5]
# print(first_five) =[('a', ['AH0']), ('a.', ['EY1']), ('a42128', ['EY1', 'F', 'AO1', 'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T']), ('aaa', ['T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1']), ('aaberg', ['AA1', 'B', 'ER0', 'G'])]
# => cmu = {'a':['AH0'], 'a.':['EY1'],...}
phonemes_path = os.getenv('HOME') + '/nlp_data/phonemes.pickle'


if not os.path.isfile(phonemes_path):
   with open(phonemes_path ,'wb') as file:
       pickle.dump(cmu, file, pickle.HIGHEST_PROTOCOL)
   file.close() 


