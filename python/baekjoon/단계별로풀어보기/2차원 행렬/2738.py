### 행렬 덧셈

# 행렬의 크기 입력
N, M = map(int, input().split())
A = []
B = []

# 행렬 A 입력
for _ in range(N):
    A.append(list(map (int, input().split())))

# 행렬 B 입력
for _ in range(N):
    B.append(list(map (int, input().split())))

# 행렬 덧셈 계산
for i in range(N):
    for j in range(M):
        # A와 B의 동일한 행, 열의 원소를 더함
        result = A[i][j] + B[i][j]
        # 공백으로 구분하여 출력 -> 한줄씩 출력하는게 아니라 한 행씩 출력하기 위해 end = " " 사용
        print(result, end = " ")
    # 줄바꿈
    print()




