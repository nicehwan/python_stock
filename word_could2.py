from wordcloud import WordCloud
import nltk
from nltk.corpus import gutenberg
import matplotlib.pyplot as plt

file_names = gutenberg.fileids()

print(file_names)
nltk.download('punkt_tab')
nltk.download('punkt')

doc_alice = gutenberg.raw('carroll-alice.txt')

wordcloud = WordCloud().generate(doc_alice)

plt.axis('off')
plt.imshow(wordcloud, interpolation='bilinear') # 이미지를 출력
plt.show()