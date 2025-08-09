# 25.08.09 백준 3699 주차 빌딩

import sys
sys.stdin = open("input.txt", 'r')

tc = int(input())

for _ in range(tc):
    h, i = map(int, input().split())
    parking = [list(map(int, input().split())) for _ in range(h)]

    # 손님 정보 저장
    cust = {}
    for f in range(h):
        for x in range(i):
            if parking[f][x] != -1:
                cust[parking[f][x]] = [f, x]

    answer = 0
    if len(cust) == 0:
        print(answer)
        continue

    info = [0] * h
    for c in range(1, len(cust) + 1):
        y, x = cust[c]
        coor_x = abs(info[y] - x)
        answer += (20 * y) + (min(coor_x, i - coor_x) * 5)
        info[y] = x

    print(answer)