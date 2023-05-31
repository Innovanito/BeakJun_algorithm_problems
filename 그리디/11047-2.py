'''
1.아이디어
큰 액수부터 동전 차감
반례: 동전이 무한대여서 없는 것 같음 & 동전이 배수기도 함
-K를 동전으로 나눈 뒤 남은 값을 갱신

2. 시간복잡도
O(N)

3. 자료구조
동전금액: int[]
현재 남은 금액: int
동전 개수: int

'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

coins.reverse()
result = 0

for coin in coins:
    if K // coin > 0:
        each = K // coin
        result += each
        K = K % (each * coin)

print(result)
