# 25.04.17 누적합
# 누적합은 아무리 봐도 이해가 안된다.. 다시 공부해야할듯.

import sys
sys.stdin = open("input.txt", 'r')

import bisect

T = int(input())
a = int(input())
an = list(map(int, input().split()))
b = int(input())
bn = list(map(int, input().split()))

aan, bbn = [], []   # an, bn의 누적합을 저장할 리스트
for i in range(a):
    for j in range(i + 1, a + 1):
        aan.append(sum(an[i:j]))
for i in range(b):
    for j in range(i + 1, b + 1):
        bbn.append(sum(bn[i:j]))

aan.sort()
bbn.sort()

# aan의 원소를 하나씩 체크하면서 합이 T가 되는 bbn의 원소 이진탐색으로 검색(탐색을 위해 위에서 소트해줌)
# 혹은 누적합을 구하면서 T를 사용해서 이미 계산 하여 구하는 방법.
ans = 0
for i in range(len(aan)):
    bmp = T - aan[i]

    # bisect 라이브러리를 사용해서 bbn 리스트에 bmp 값이 존재하는지 index 값을 알 수가 있다.
    left = bisect.bisect_left(bbn, bmp)
    right = bisect.bisect_right(bbn, bmp)
    ans += (right - left)

print(ans)

#참고 https://jaehwaseo.tistory.com/49