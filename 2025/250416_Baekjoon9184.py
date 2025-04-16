'''
25.04.16 DP(메모이제이션)
메모이제이션의 개념은 알지만, 실제 문제는 처음봐서, 풀이를 보며 공부하는데 집중했다.

피보나치 수열의 메모이제이션 방법
def fibo(n):
    global memo
    if n >= len(memo):
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

memo = [0, 1]
'''

# 문제에 수식이 많아서 복잡해보이겠지만, 수식을 그대로 함수로 구현해주고(0이하 20초과만 미리 써준 뒤, 그 외에 값이 저장되어 있다면 그대로 출력)
# dp에서 바로 출력하면 되는 간단한 문제였다.

import sys
sys.stdin = open("input.txt", 'r')

dp = [[[0]*(21) for _ in range(21)] for _ in range(21)] # 0~20까지가 함수의 범위였으니 dp는 21까지
def w(a, b, c):
    # 모든 값 중 0 이하가 있다면 1 출력
    if a <= 0 or b<= 0 or c<=0:
        return 1
    # 모든 값 중 20 초과 이하가 있다면 전체 값에 20을 넣었을 때 값을 출력
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # 저장된 값이 있으면 바로 출력시키고, 아니라면 계속 진행(초기화는 0으로 진행 - 어차피 0, 0, 0 넣음 1이 나오므로 답에 0이 있을 수 없음)
    if dp[a][b][c]:
        return dp[a][b][c]

    # 위 조건이 없다면 재귀를 구현하듯 계속 값에 저장해줘야됨.
    if a < b < c:
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a, b-1, c)
        return dp[a][b][c]

    # otherwise it returns
    dp[a][b][c] = w(a-1, b, c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    return dp[a][b][c]

while 1:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')