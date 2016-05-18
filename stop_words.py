from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example = 'This is an example showing stop word filtration.'

stop_words = set(stopwords.words('english'))

words  = word_tokenize(example)

# long hand
#filtered_sentence = []
#for w in words:
#  if w not in stop_words:
#      filtered_sentence.append(w)

# short hand
filtered_sentence = [w for w in words if not w in stop_words]

print(filtered_sentence)
# ['This', 'example', 'showing', 'stop', 'word', 'filtration', '.']
