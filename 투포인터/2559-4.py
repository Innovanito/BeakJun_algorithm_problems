# 1.아이디어
# 연속한 합이라는 조건을 이용해 투포인터 이용
# 먼저  for ->k번째 합을 구하고
# 병렬 for로 다음값 더하고 처음값 빼서 max()로 최대값 저장 후 프린트

# 2.시간복잡도
# O(n)

# 3.자료구조
# n,k = int
# temps = int[]
# maxv = int


n, k = map(int, input().split())
temps = list(map(int, input().split()))

maxv = 0

for i in range(k):
    maxv += temps[i]

newV = maxv
for j in range(n-k):
    newV += temps[k+j]
    newV -= temps[j]
    maxv = max(maxv, newV)

print(maxv)
