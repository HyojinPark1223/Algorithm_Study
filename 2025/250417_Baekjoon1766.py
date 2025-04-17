# 25.04.17 우선순위 큐
# 처음 보는 문제였다.. 우선순위 큐라는 게 있다는 걸 첨 알았음.
# 앞 번호부터 체크해본 뒤에, 연결 되어있는 노선이 있다면(먼저 계산해야하는 것이 있다면) 넣어주지 않음.
# 연결된 문제(예를들면 3, 1)의 경우 앞을 우선순위 큐로 queue의 앞으로 연결된 걸 땡겨 넣어준다.

import sys
sys.stdin = open("input.txt", 'r')

import heapq

n, m = map(int, input().split())

answer = []
graph = [[] for _ in range(n + 1)]
inDegree = [0 for _ in range(n+1)]
queue = []

for i in range(m):
    first, second = map(int, input().split())
    graph[first].append(second)
    inDegree[second] += 1

for i in range(1, n + 1):
    if inDegree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    tmp = heapq.heappop(queue)
    answer.append(tmp)
    for i in graph[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(queue, i)


print(" ".join(map(str, answer)))