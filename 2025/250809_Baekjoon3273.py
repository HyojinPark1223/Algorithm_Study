# 25.08.09 3273 두 수의 합
# 이중 포인터 라는 것을 사용함. 처음엔 pop을 해서 리스트 내부를 빼버리려고 했는데.. 이런 방법이...

import sys
sys.stdin = open("input.txt", 'r')

n = int(input())
nums = sorted(list(map(int, input().split())))
goal = int(input())
#print( nums)

answer = 0
start, end = 0, n-1

while start < end:
    added = nums[start] + nums[end]
    if added == goal:
        answer += 1
        start += 1
        end -= 1
    elif added > goal:
        end -= 1
    else:
        start += 1
print(answer)