import nltk

nltk.download('gutenberg')

from nltk.corpus import gutenberg

file_names = gutenberg.fileids()

print(file_names)
nltk.download('punkt_tab')
nltk.download('punkt')

doc_alice = gutenberg.raw('carroll-alice.txt')

print('#Num of characters used:', len(doc_alice))   # used character count
print('#Text Sample:')
print(doc_alice[:500])  # print prev 500 characters

from nltk.tokenize import word_tokenize


tokens_alice = word_tokenize(doc_alice)     # execute tokenize

# print token num and 20 tokens,
# then compare to over contents
print('#Num of tokes used:', len(tokens_alice))
print('#Token sample:')
print(tokens_alice[:20])

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

# execute stemming about all of tokens
stem_tokens_alice = [stemmer.stem(token) for token in tokens_alice]

print('#Num of tokens after stemming:', len(stem_tokens_alice))
print('#Token sample:')
print(stem_tokens_alice[:20])

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# execute stemming about all of tokens
len_tokens_alice = [lemmatizer.lemmatize(token) for token in tokens_alice]

print('#Num of tokens after lemmatization:', len(len_tokens_alice))
print('#Token sample:')
print(len_tokens_alice[:20])

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[\w']{3,}")

reg_tokens_alice = tokenizer.tokenize(doc_alice.lower())
print('#Num of tokens with RegexpTokenizer:', len(reg_tokens_alice))
print('#Token sample:')
print(reg_tokens_alice[:20])