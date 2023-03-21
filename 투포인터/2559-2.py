'''
1. 아이디어
-투포인터를 사용
-for문으로 처음에 K개값을 저장하고
-그 다음 인덱스를 더해주고, 이전 인덱스를 빼줌
- 이때마다 최대값을 갱신한다

2.시간복잡도
-O(N) = 1e5

3. 자료구조
input값 저장배열 : int[]
최대값 : int


'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
each = 0


for i in range(K):
    each += nums[i]
maxv = each

for i in range(K, N):
    each += nums[i]
    each -= nums[i-K]
    maxv = max(maxv, each)

print(maxv)
