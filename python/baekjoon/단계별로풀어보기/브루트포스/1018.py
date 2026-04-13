#### 체스판 다시 칠하기
"""
첫 풀이
"""

N, M = map(int, input().split())

board = [input() for _ in range(N)]
print(board)

for i in range(N-7):
    for j in range(M-7):
        board[i][j] =