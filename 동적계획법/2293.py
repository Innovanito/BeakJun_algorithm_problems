'''
1.아이디어
n과 k를 기준으로 표를 만들면 점화식 형태로 문제가 풀어진다는 것을 알 수 있다.
dp[i][j] : i번째 동전 사용 시, j원을 만드는 경우의 수

2. 시간복잡도
?

3.지료그조
coins : int[]
n, k : int
coins: []
result: int
'''

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# 초기화
dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
    for j in range(coin, k+1):
        dp[j] += dp[j-coin]

print(dp[k])
