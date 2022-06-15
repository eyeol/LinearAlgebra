# Elimination with Matrices

Matrix_A = [[1, 2, 1], [3, 8, 1], [0, 4, 1]]

# 첫 행부터 차례대로
# 마지막 행은 생각할 필요 없음
for Row_index in range(len(Matrix_A)-1):

	# Pivot을 지정해야 하는 행
	Row = Matrix_A[Row_index]

	# 행 안에서 0이 아닌 값에 도달할 때까지 탐색
	while (Row[index] == 0):
		index += 1

	# 0이 아니면서 가장 앞에 있는 값을 Pivot에 할당
	Pivot = Row[index]

	# 이때 Row exchange 여부를 어떻게 확인할 것인가



	# Eliminaton할 행의 index: 바로 아래 행부터
	Operand_index = Row_index + 1

	# Row Operation
	while (Operand_index <= len(Matrix_A)-1):
		# Operand Row
		Row2  = Matrix_A[Operand_index]

		# Elimination
		Fivot = Row2[index]
		Elim  = Fivot/Pivot
		for i in range(len(Row)):
			Row2[i] = Row2[i] - Elim*Row[i]

		Matrix_A[Operand_index] = Row2

		# Operand를 다음 행으로 옮김
		Operand_index += 1

print(Matrix_A)

# 실행 결과: [[1, 2, 1], [0.0, 2.0, -2.0], [0.0, 0.0, 5.0]]
