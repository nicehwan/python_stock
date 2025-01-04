from wordcloud import WordCloud
import nltk
from nltk.corpus import gutenberg
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

file_names = gutenberg.fileids()

print(file_names)
nltk.download('punkt_tab')
nltk.download('punkt')

doc_alice = gutenberg.raw('carroll-alice.txt')

wordcloud = WordCloud().generate(doc_alice)

plt.axis('off')
plt.imshow(wordcloud, interpolation='bilinear') # 이미지를 출력
plt.show()

tokenizer = RegexpTokenizer("[\w']{3,}")

reg_tokens_alice = tokenizer.tokenize(doc_alice.lower())
english_stops = set(stopwords.words('english')) # change the set datatype for not changeable

alice_word_count = dict()

result_alice = [word for word in reg_tokens_alice if word not in english_stops]

for word in result_alice:
    alice_word_count[word] = alice_word_count.get(word, 0) + 1

wordcloud = WordCloud(max_font_size=60).generate_from_frequencies(alice_word_count)
plt.figure()
plt.axis('off')
plt.imshow(wordcloud, interpolation='bilinear')
plt.show()