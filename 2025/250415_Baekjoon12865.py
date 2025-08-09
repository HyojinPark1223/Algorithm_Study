# 25.04.15 DP 알고리즘
# DP: 단순 재귀와 비슷하지만 중복된 것을 제거하는 효율적인 방법(한 번 구한 값을 저장해둠)
# dp문제 어려워서 매번 볼때마다 뭔소리인지 몰랐는데, 표 그리면서 알려준 블로그 참고하니 이해가 갑자기 확 됨..! 재밌다~ 근데 블로그 주소 첨부하려다 실수로 꺼버린..ㅠㅠ

import sys
sys.stdin = open("input.txt", 'r')

N, K = map(int, input().split())
stuff = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(K + 1) for _ in range(N + 1)]
# 계산의 편의를 위해 N + 1, K + 1로 줌(index값 혼선 방지)

for i in range(1, N + 1):
    for j in range(1, K + 1):       # 가치표의 j는 현재 최대 무게
        # 현재 무게가 물건의 무게보다 작으면, 물건을 담을 수 없음.
        if j >= stuff[i - 1][0]:
            # 물건을 담을 수 있다면, 두 개의 더한 값, 이전 물건의 값을 비교하여 최댓값을 넣어줌.
            dp[i][j] = max(stuff[i - 1][1] + dp[i - 1][j - stuff[i - 1][0]], dp[i - 1][j])

        else:
            # 물건을 담을 수 없다면 이전 물건과 배낭 무게수의 기록을 그대로 가져와줌.
            dp[i][j] = dp[i - 1][j]

print(dp[N][K])  #DP[N][K]가 무조건 정답
