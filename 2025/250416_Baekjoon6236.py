# 25.04.16 이분탐색

import sys
sys.stdin = open("input.txt", 'r')

n, m = map(int, input().split())
days = list(map(int, input().split()))

answer = 0
s = max(days)
e = min(days)

while s <= e:
    mid = (s + e) // 2  # 중간 값(이진 탐색을 위함)

    total = 0
    cnt = 0

    for money in days:
        if total + money <= mid:
            total += money

        else:
            cnt += 1
            total = 0
            total += money

    if total:
        cnt += 1

    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)