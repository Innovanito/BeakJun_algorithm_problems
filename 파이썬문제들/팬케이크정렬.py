# from random import sample


def pancake_sort(lst):
    flip = 0  # 뒤집은 횟수 초기화
    for i in range(len(lst)-1):  # 리스트 길이만큼 반복
        # 정렬전 범위에서 최고값의 위치 저장,#i는 정렬완료된것을 빼는 것
        m = lst.index(max(lst[:len(lst)-i]))
        print(f'm의 값: {m}')
        if m == len(lst)-1:  # 최고값의 위치가 맨 뒤라면
            continue  # 아무 것도 하지 않고 처음으로 돌아감
        if 0 < m:  # 최고값의 위치가 맨 앞이 아니라면
            print(f'lst[m::-1] 전 값: {lst[m::-1]}')
            print(f'lst[m+1:]전 값: {lst[m+1:]}')
            lst = lst[m::-1]+lst[m+1:]  # 처음부터 max까지를 뒤집고
            print(f'lst[m::-1] 후 값: {lst[m::-1]}')
            print(f'lst[m+1:]후 값: {lst[m+1:]}')
            flip += 1  # 뒤집은 횟수 증가
            print('flip>', flip, lst)  # 뒤집은 횟수와 뒤집은 후 리스트 출력

        # 최고값의 위치가 맨 앞이므로 정렬전 범위 전체를 뒤집고
        lst = lst[len(lst)-1-i::-1]+lst[len(lst)-i:]
        flip += 1  # 뒤집은 횟수 증가
        print('flip>', flip, lst)  # 뒤집은 횟수와 뒤집은 후 리스트 출


# 1~ 50까지의 정수 중에서 겹치지 않는 랜덤한 값 10개 추출
# lst = sample([i+1 for i in range(50)], 10)
lst = [2, 4, 3, 5, 1]
print('flip >', '0', lst)
pancake_sort(lst)
