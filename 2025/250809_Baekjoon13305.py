# 25.08.09 백준 13305 주유소
# 더 싼 지점이 나올 때까지 계속 더해주면 됐는데... 처음에 너무 복잡하게 풀었다.

import sys
sys.stdin = open("input.txt", 'r')

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
p = price[0]
for i in range(n-1):
    if p > price[i]:
        p = price[i]
    result += (p * distance[i])

print(result)