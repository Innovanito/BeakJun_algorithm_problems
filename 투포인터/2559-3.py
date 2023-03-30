'''
1.아이디어
연속하다는 특성을 이용해서
처음 K개를 더하고
for 문을 N-K만큼 돌려서 max 값을 저장

2. 시간복잡도
O(N)= 10만

3.자료구조
N, K = int
lst = int[]
maxVal = int
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))
each = 0
maxVal = 0

for i in range(K):
    each += lst[i]

maxVal = each

for i in range(K, N):
    each += lst[i]
    each -= lst[i-K]
    maxVal = max(maxVal, each)

print(maxVal)
