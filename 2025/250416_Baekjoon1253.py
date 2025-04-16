# 25.04.16 투 포인터
# 처음에 조합으로 풀었는데 시간 초과났다. 시간 복잡도가 2초라서 NlogN의 시간복잡도 알고리즘을 사용해야 했던 것.

import sys
sys.stdin = open("input.txt", 'r')

n = int(input())
arr = list(map(int, input().split()))
arr.sort()  # 퀵소트를 사용하기 위한 정렬.

answer = 0

for i in range(n):
    num = arr[i]
    start = 0
    end = n - 1

    while start < end:
        if arr[start] + arr[end] == num:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                answer += 1
                break

        elif arr[start] + arr[end] > num:
            end -= 1

        elif arr[start] + arr[end] < num:
            start += 1

print(answer)