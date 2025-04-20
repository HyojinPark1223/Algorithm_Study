# 25.04.20 DP 문제 풀기

import sys
sys.stdin = open("input.txt", 'r')

n = int(input())
dp = [0] * (n+1)

# n은 1 이상부터라고 하였으니 2부터 n까지 진행.
for i in range(2, n+1):
    dp[i] = dp[i - 1] + 1   # 1을 빼는 연산은 모든 수에서 가능하므로 일단 저장

    # 2로 나눠지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

    # 3으로 나눠지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])