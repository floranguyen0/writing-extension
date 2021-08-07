import os
import pickle


hedge_words = {'must', "if i'm understanding you correctly", 'rare', 'much', 'certainly', 'occasionally', 'appeared', 'thinks', 'estimate', 'largely', 'seemed', 'alleged', 'understands', 'say', 'somewhat', 'in my opinion', 'finds', 'really', 'guessed', 'mostly', 'would', 'in my understanding', 'maybe', 'certain', 'suggest', 'supposes', 'often', 'partially', 'about', 'in general', 'sort of', 'should', 'bunch', 'something or other', 'thought', 'et cetera', 'inconclusive', 'assumes', 'sometimes', 'considers', 'my thinking is', 'consistent with', 'could', 'practically', 'frequently', 'quite', 'possibility', "don't know", 'pretty', 'doubt', 'assumed', 'tend', 'found', 'virtually', 'looks like', 'believe', 'actually', 'at least', 'few', 'be sure', 'can', 'seems', 'suppose', 'somewhere', 'little', 'considered', 'seem', 'rarely', 'some', 'perhaps', 'believes', 'evidently', 'appear', 'possible', 'doubtful', 'supposed', 'couple', 'read', 'and so forth', 'allege', 'unsure', 'around', 'probably', 'generally', 'basically', 'unlikely', 'may', 'always', 'seldom', 'estimated', 'might', 'presumably', 'so far', 'assumption', 'appear to be', 'believed', 'most', 'appears', 'understood', 'clear', 'hopefully', 'indicate', 'something', 'improbable', 'in my view', 'someone', 'approximately', 'guesses', 'says', 'necessarily', 'rather', 'suggests', 'suggestive', 'likely', 'almost never', 'assume', 'fairly', 'look like', 'apparent', 'speculates', 'definite', 'somehow', 'like', 'probability', 'roughly', 'several', 'kind of', 'speculate', 'conceivably', 'find', 'quite clearly', 'definitely', 'think', 'suggested', 'consider', 'guess', 'speculated', 'will', 'my understanding is', 'probable', 'more or less', 'effectively', 'somebody', 'possibly', 'supposedly', 'presumable', 'apparently', 'my impression', 'almost', 'understand', 'diagnostic', 'surely', 'many', 'a bit', 'and all that', 'clearly', 'overall', 'mainly', 'usually', 'estimates', 'their impression', 'in my mind'}
# print(hedge_words)
# print(len(hedge_words)) = 162
hedge_words_path = os.getenv('HOME') + '/nlp_data/hedge_words.pickle'

if not os.path.isfile(hedge_words_path):
 with open(hedge_words_path, 'wb') as file:
  pickle.dump(hedge_words, file, pickle.HIGHEST_PROTOCOL)
  file.close()