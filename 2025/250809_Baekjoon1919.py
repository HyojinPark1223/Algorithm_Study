# 25.08.09 백준 1919 애너그램 만들기
from collections import Counter
import sys
sys.stdin = open("input.txt", 'r')

w1 = input()
w2 = input()

d1 = Counter(w1)
d2 = Counter(w2)

answer = 0

for k, v in dict(d2-d1).items():
    answer += v
for k, v in dict(d1-d2).items():
    answer += v

print(answer)