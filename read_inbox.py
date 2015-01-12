"""
Following along with some examples from this blog post.

http://engineroom.trackmaven.com/blog/monthly-challenge-natural-language-processing/

"""

from mailbox import mbox
import pandas as pd

def store_content(message, body=None):
    if not body:
        body = message.get_payload(decode=True)
    if len(message):
        contents = {
            "subject": message['subject'] or "",
            "body": body,
            "from": message['from'],
            "to": message['to'],
            "date": message['date'],
            "labels": message['X-Gmail-Labels'],
            "epilogue": message.epilogue,
        }
        return df.append(contents, ignore_index=True)

# Create an empty DataFrame with the relevant columns
df = pd.DataFrame(
    columns=("subject", "body", "from", "to", "date", "labels", "epilogue"))

# Import your downloaded mbox file
box = mbox('gmail-short.mbox')

fails = []
for message in box:
    try:
        if message.get_content_type() == 'text/plain':
            df = store_content(message)
        elif message.is_multipart():
            # Grab any plaintext from multipart messages
            for part in message.get_payload():
                if part.get_content_type() == 'text/plain':
                    df = store_content(message, part.get_payload(decode=True))
                    break
    except:
        fails.append(message)


# Top 10 most common subject words
from collections import Counter

# Find top ten most common terms.
subject_word_bag = df.subject.apply(lambda t: t.lower() + " ").sum()
#counter = Counter(subject_word_bag.split()).most_common()[:10]

# Find top ten most common terms while ignoring common words.
from nltk.corpus import stopwords
stops = [unicode(word) for word in stopwords.words('english')] + ['re:', 'fwd:', '-']
subject_words = [word for word in subject_word_bag.split() if word.lower() not in stops]
#counter = Counter(subject_words).most_common()[:10]
#print counter

# Find bigrams with a frequency higher than 5
from nltk import collocations
bigram_measures = collocations.BigramAssocMeasures()
bigram_finder = collocations.BigramCollocationFinder.from_words(subject_words)
bigram_finder.apply_freq_filter(5)
for bigram in bigram_finder.score_ngrams(bigram_measures.raw_freq)[:10]:
    print bigram


