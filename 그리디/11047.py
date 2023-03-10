'''
1. 아이디어
그리디 알고리즘을 이용해서 
coins를 reverse 해준다음 
K의 돈을 큰수대로 나누고
나머지를 저장한 후 for문을 돌린다

for coin in coins:
  if K // coin >0:
    each = K//coin
    result += each
    K = K% (each * coin)

2. 시간복잡도
for문이기 때문에 O(N)


3. 자료구조
N, K: int
coins: int[]
result: int
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

coins.reverse()
result = 0

for coin in coins:
    if K // coin > 0:
        each = K//coin
        result += each
        K = K % (each * coin)

print(result)
