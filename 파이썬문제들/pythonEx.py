# 1. 주어진 검색 리스트에서 입력받은 검색값을 이진 탐색하는 재귀함수의 빈 괄호를 채워 완성하시오.
# 입력
# 1~20사이의 정수 1개
# 출력
# 검색 대상 리스트에 입력받은 값이 없으면 '검색값이 없음'
# 검색 대상 리스트의 i번째에 입력받은 값이 있으면 'i번째 있음'

# 2. 주어진 list를 이용해서 아래와 같은 구조와 단일 연결리스트 slit를 생성하여 실행 예시와 같이
# 출력되도록 반복문의 실행부분을 완성하시오.

# lst = ['서울', '수원', '천안', '대전', '대구', '부산', '제주']

# 입력

# 없음

# 출력

# 서울 > 수원
# 수원 > 천안
# 천안 > 대전
# 대전 > 대구
# 대구 > 부산
# 부산 > 제주

# 3. 다음 두 가지 조건을 가진 집합 S 중에서 합하여 K가 되는 숫자들을 출력하시오.
# 조건1 > 집합의 숫자를 합하여 반드시 K가 되는 조합이 있다.
# 조건2 > 집합의 어떤 숫자이든지 자신보다 앞서 있는 숫자들의 합과 같거나 크다.

# 4. 주어진 정수의 개수만큼 차례로 피보나치 수열을 입력하도록 다음 함수를 정의 하시오.
# 입력

# 13~20사이의 정수 1개

# 출력

# 2, 3으로 시작하여 입력 받은 정수의 개수만큼 피보나치 수열을 요소로 가지는 리스트

# 5. 오름차순으로 정렬된 리스트에서 입력받은 값을 이진 탐색하는 코드를 완성하시오.
# 6. 그리디 알고리즘을 적용하여 배낭이 가장 비싼 아이템 채우는 코드를 완성하시오.

# ex1
def binarySearch(array, target, left, right):
    middle_idx = (left+right)//2
    middle = array[middle_idx]
    if target == middle:
        print('입력 받는 값이 {}번째에 있음'.format(middle_idx))
    elif middle > target & array[]:
        binarySearch(array, target, left, middle_idx-1)
    elif middle < target:
        binarySearch(array, target, middle_idx+1, right)
    else:
        return print('입력 받는 값이 없음')


target = int(input('찾을 숫자:'))
m_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
length = len(m_list)

# 리스트 안에 수를 순서대로 정렬 (안해도 되긴 함)
m_list.sort()
left = 0
right = length-1

binarySearch(m_list, target, 0, right)


# ex2
lst = ['서울', '수원', '천안', '대전', '대구', '부산', '제주']

for i in range(0, len(lst)-1):
    print(lst[i]+'>' + lst[i+1])


# 4 ex
def fib(n):
    _curr, _next = 0, 1
    for _ in range(n):
        _curr, _next = _next, _curr + _next
    return _curr
