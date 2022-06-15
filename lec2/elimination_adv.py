# Elimination with Matrices

N = int(input("행의 개수: "))

Matrix_A = []

for i in range(N):
	Matrix_A.append(list(map(int, input().split())))

# 행과 열의 길이
row_length = len(Matrix_A)-1
col_length = len(Matrix_A[0])-1

# row의 index : i
i = 0
# 처음 피봇은 행의 첫번째 원소
pivot = 0

# 마지막 row는 밑에 elimination할 행이 없기 때문에 고려하지 않음
while (i <= row_length-1):
    # process는 처음에 "Success"로 초기화
    process = "Success"

    # 주의!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # 피봇 위치에 있는 값이 0이면 row exchange를 해야 함
    if Matrix_A[i][pivot] == 0:
        # 일단 process failure라고 판단
        process = "Failure"
        # exchange할 row의 index : k
        # 바로 밑에 있는 행부터 탐색
        k = i + 1
        # 마지막 행까지
        while(k <= row_length):
            # 그 다음 행의 피봇 위치에 있는 값이 0이 아니면 두 행렬을 교환하고 반복문 탈출
            if (Matrix_A[k][pivot] != 0):
                Matrix_A[i], Matrix_A[k] = Matrix_A[k], Matrix_A[i]
                # process는 다시 Success로 재개
                process = "Success"
                break

            # 다음 행
            k += 1

    # 만약 피봇 위치에 있는 값이 0이고, row exchange할 row도 못찾았다면
    # row operation할 내용이 없기 때문에 피봇 위치를 한칸 내리고 다시 시도
    if process == "Failure":
        pivot += 1
        continue


    # 피봇 교통 정리는 끝났고 row operation할 차례


    # operand row의 index : h
    # 바로 밑에 있는 행부터 row operation 진행
    h = i + 1
    # 마지막 행까지
    while(h <= row_length):
        # elimination을 위한 계수
        # Matrix_A[h][pivot]이 0인 경우, 자연스럽게 E도 0이 된다
        E = Matrix_A[h][pivot]/Matrix_A[i][pivot]

        # 반복문에서 시작점으로 사용할 pivot 위치
        p = pivot

        # Elimination
        # pivot 위치부터 빼면 된다
        while(p <= col_length):
            Matrix_A[h][p] = Matrix_A[h][p] - E * Matrix_A[i][p]
            p += 1

        # 다음 행
        h += 1

    # 다음 행에서는 피봇 위치가 한칸 뒤로 가도록
    i += 1
    pivot += 1

print(Matrix_A)
