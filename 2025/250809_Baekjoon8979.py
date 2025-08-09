# 25.08.09 백준 8979 올림픽

import sys
sys.stdin = open("input.txt", 'r')

n, k = map(int, sys.stdin.readline().split())
record = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

record.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

medal = [1] * (n+1)
for i in range(1, n):
    if [record[i][1], record[i][2], record[i][3]] == [record[i-1][1], record[i-1][2], record[i-1][3]] :
        medal[record[i][0]] = medal[record[i - 1][0]]

    else:
        medal[record[i][0]] = i + 1


print(medal[k])