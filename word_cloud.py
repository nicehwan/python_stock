import nltk

nltk.download('gutenberg')

from nltk.corpus import gutenberg

file_names = gutenberg.fileids()

print(file_names)

doc_alice = gutenberg.open('carroll-alice.txt').read()
print('@Num of characters used:', len(doc_alice))   #사용된 문자 수
print('#Text Sample:')
print(doc_alice[:500])  #앞의 500자만 출력