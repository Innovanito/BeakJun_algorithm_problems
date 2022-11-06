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
