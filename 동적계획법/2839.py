'''
1.아이디어
while문으로 sugar가 0이상이면 반복
  if 5의 배수이면 5로 나눈 몫을 구하고 나눠 떨어진
  값을 result에 넣고 결과값을 print를 하고 break한다.
  그리고 -3을 하고 result에 +=를 한다.
else print(-1)

2.시간복잡도
O(N) = 5000/3

3.자료구조
result = int
'''

import sys
input = sys.stdin.readline

N = int(input())
result = 0

while N >= 0:
    if (N % 5 == 0):
        result += N//5
        print(result)
        break
    N -= 3
    result += 1
    if (N == 0):
        print(result)
        break
else:
    print(-1)
