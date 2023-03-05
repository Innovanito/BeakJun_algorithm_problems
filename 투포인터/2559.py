'''
1. 아이디어
-투포인터를 활용
-for로 처음 k개 값 저장 후
다음인덱스 더해주고, 이전 인덱스를 빼줌
-이때마다 최대값을 갱신

2. 시간복잡도
-O(N) = 10^5

3. 자료구조
-N개 값 저장: int[]
-K개 값을 저장
-최대값
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numList = list(map(int, input().split()))
maxVal = 0
eachVal = 0
firstVal = 0

for i in range(K):
    firstVal += numList[i]

maxVal = firstVal
eachVal = firstVal

for i in range(K, N):
    eachVal += numList[i]
    eachVal -= numList[i-K]
    maxVal = max(eachVal, maxVal)


print(maxVal)
