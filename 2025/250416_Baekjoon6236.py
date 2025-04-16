# 25.04.16 이분탐색
# 문제가 이해가 안되서 풀이를 못 찾은..ㅋㅋ..
# 이분 탐색: 시작과 끝, 중간값을 정한 뒤, 찾고자 하는 범위가 중간값보다 크면 시작값을 중간 + 1로, 작으면 끝값을 중간 -1로 설정하여 원하는 수를 찾는 방법.

import sys
sys.stdin = open("input.txt", 'r')

n, m = map(int, input().split())
days = [int(input()) for _ in range(n)]

answer = 0
# n일동안 써야하므로 적어도 최대값을 넣어주고, 한 번에 뽑아서 다 쓰는 경우가 최대.

s = max(days)
e = sum(days)

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
        s = mid + 1
    else:
        e = mid - 1
        answer = mid

print(answer)