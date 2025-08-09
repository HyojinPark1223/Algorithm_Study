# 25.08.09 백준 11660 구간합
#* 입출력 속도 비교 : sys.stdin.readline > raw_input() > input()

import sys
sys.stdin = open("input.txt", 'r')
N, M = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*(N+1) for _ in range(N+1)]

for x in range(1, N+1):
    for y in range(1, N+1):
        dp[x][y] = dp[x][y-1] + dp[x-1][y] + arr[x-1][y-1] - dp[x-1][y-1]

print(dp)
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    result = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(result)