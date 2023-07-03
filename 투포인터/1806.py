def find_shortest_subtotal_length(N, S, sequence):
    left = 0  # 왼쪽 포인터 초기화
    right = 0  # 오른쪽 포인터 초기화
    subtotal = 0  # 현재 서브토탈 초기화
    min_length = float('inf')  # 최소 길이를 큰 값으로 초기화

    while left < N:  # 왼쪽 포인터가 수열의 끝에 도달할 때까지 반복
        if subtotal < S and right < N:  # 현재 서브토탈이 S보다 작고 오른쪽 포인터가 범위 내에 있는 경우
            subtotal += sequence[right]  # 오른쪽 포인터의 요소를 현재 서브토탈에 더함
            right += 1  # 오른쪽 포인터를 한 칸 앞으로 이동
        else:  # 현재 서브토탈이 S보다 크거나 같거나 오른쪽 포인터가 범위를 벗어난 경우
            if subtotal >= S:  # 현재 서브토탈이 S보다 크거나 같은지 확인
                # 더 짧은 길이를 찾으면 최소 길이를 업데이트
                min_length = min(min_length, right - left)
            subtotal -= sequence[left]  # 왼쪽 포인터의 요소를 현재 서브토탈에서 뺌
            left += 1  # 왼쪽 포인터를 한 칸 앞으로 이동

    if min_length == float('inf'):
        return 0  # 서브토탈을 만들 수 없는 경우 0 반환
    else:
        return min_length  # 최소 길이 반환


# 입력 받기
N, S = map(int, input().split())  # N과 S를 입력으로 받음. 공백으로 구분된 정수들로 가정
sequence = list(map(int, input().split()))  # 수열을 입력으로 받음. 공백으로 구분된 정수들로 가정

# 함수 호출 및 결과 출력
result = find_shortest_subtotal_length(N, S, sequence)  # 입력값으로 함수 호출
print(result)  # 결과 출력
