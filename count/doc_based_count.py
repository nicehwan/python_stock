# BOW : Bag of Words 
# 카운트를 기반으로 문서로부터 특성을 추출하고 표현하는 방식

import nltk

nltk.download('movie_reviews')

from nltk.corpus import movie_reviews
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords   # 일반적으로 분석 대상이 아닌 단어들

def doc_based_count():
    print('#review count:', len(movie_reviews.fileids()))  # 영화 리뷰 갯수
    print('#samples of file ids:', movie_reviews.fileids()[:10])  # 영화리뷰 id를 10개까지만 출력

    fileid = movie_reviews.fileids()[0]  # 첫번째 문서의 id를 반환
    print('#id of the first review:', fileid)

    # 첫번째 문서의 내용을 200자까지만 출력
    print('#first review content:\n', movie_reviews.raw(fileid)[:200])

    # 첫번째 문서를 sentence tokenize한 결과 중 앞 두 문장
    print('#sentence tokenization result:', movie_reviews.sents(fileid)[:2])

    # 첫번째 문서를 word tokenize한 결과 중 앞 20개 단어
    print('#word tokenization result:', movie_reviews.words(fileid)[:20])


def get_text_based_bow():
    documents = [list(movie_reviews.words(fileid)) for fileid in movie_reviews.fileids()]
    print(documents[0][:50])    # 첫째 문서의 앞 50개 단어를 출력

    word_count = {}
    for text in documents:
        for word in text:
            word_count[word] = word_count.get(word, 0) + 1

    sorted_features = sorted(word_count, key=word_count.get, reverse=True)
    for word in sorted_features[:10]:
        print(f"count of '{word}': {word_count[word]}", end=', ')

def get_text_regexp():
    tokenizer = RegexpTokenizer("[\w']{3,}")     # 정규표현식으로 토크나이저를 정의
    english_stops = set(stopwords.words('english'))     # 영어 불용어를 가져옴

    # words() 대신 raw() 로 원문을 가져옴
    documents = [movie_reviews.raw(fileid) for fileid in movie_reviews.fileids()]

    # stopwords의 적용과 토큰화를 동시에 수행
    tokens = [[token for token in tokenizer.tokenize(doc) if token not in english_stops] for doc in documents]
    word_count = {}
    for text in tokens:
        for word in text:
            word_count[word] = word_count.get(word, 0) + 1

    sorted_features = sorted(word_count)


if __name__ == "__main__":
    # doc_based_count()
    get_text_based_bow()
