'''
1. 아이디어
연속하다는 문제의 특성을 이용해서 투 포인터를 사용
for 문으로 i개를 더할지 정하고
  for문 안에서 투포인터를 사용한다
그리고 그 결과가 M이 만족하면 result에 +1

2. 시간복잡도
O(N^2) = 1억

3. 자료구조
수 배열 arr = int[]
result = int

'''

# 이해를 못하겠어요 => 다시 풀어보세요
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, 0
subsum = arr[0]
cnt = 0
while True:
    if subsum < M:  # 작으면 end point +1
        e += 1
        if e >= N:
            break
        subsum += arr[e]
    elif subsum == M:  # 같으면 cnt +1
        cnt += 1
        subsum -= arr[s]
        s += 1
    else:  # 크면 start point +1
        subsum -= arr[s]
        s += 1

print(cnt)
