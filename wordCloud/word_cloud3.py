from konlpy.corpus import kolaw
const_doc = kolaw.open("constitution.txt").read()

# print(type(const_doc))
# print(len(const_doc))
# print(const_doc[:600])

import jpype
from konlpy.tag import Okt

# JVM 경로를 명시적으로 설정
#jvmpath = "C:/Program Files/Java/jdk-23/bin/server/jvm.dll"
# 실제 JDK 경로를 사용하세요
jpype.startJVM()

t = Okt()
tokens_const = t.morphs(const_doc)  # 형태소 단위로 tokenize

#jpype.shutdownJVM()

print('#토큰의 수:', len(tokens_const))
print('#앞 100개의 토큰')
print(tokens_const[:100])