# 1.아이디어
# i번째 수를 뽑은 다음
# j번째 수를 더해 x가 되면 rst += 1
# ----------
# 그럼 투 포인터를 이용해보자
# 먼저 sort로 오름차순 정렬해주고
# i와 j를 투포인터를 이용해 3조건으로 풀어야함

# 2.시간복잡도
# 10^10 < 2억 => 1억이여서 안될 수도 있다. 아마 안될듯 => 시간초과 뜸

# 3.자료구조
# n = int
# arrs = int[]
# x = int


n = int(input())
arrs = list(map(int, input().split()))
x = int(input())

rst = 0

i = 0
j = len(arrs) - 1
arrs.sort()

while i < j:
    temp = arrs[i] + arrs[j]
    if temp == x:
        rst += 1
        i += 1
        j -= 1
    elif temp < x:
        i += 1
    else:
        j -= 1

print(rst)
