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

from nltk.corpus import stopwords
nltk.download('stopwords')

english_stops = set(stopwords.words('english')) # change the set datatype for not changeable

result_alice = [word for word in reg_tokens_alice if word not in english_stops]

print('#Num of tokens with stopwords:', len(result_alice))
print('#Token sample:')
print(result_alice[:20])

alice_word_count = dict()
for word in result_alice:
    alice_word_count[word] = alice_word_count.get(word, 0) + 1

print('#Num of used words:', len(alice_word_count))

sorted_word_count = sorted(alice_word_count, key=alice_word_count.get, reverse=True)

print("#Top 20 high frequency words:")
for key in sorted_word_count[:20]:
    print(f'{repr(key)}: {alice_word_count[key]}', end=', ')