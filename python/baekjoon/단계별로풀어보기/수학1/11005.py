#### 진법변환 2

N, B = map(int,input().split())

# 인덱스활용
digit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# B진법으로 변환한 답
ans = ""

# N에서 계속 나누어야하므로
while N > 0:
    # ans 갱신
    # 1의 자리의 수 부터 왼족에 추가됨
    ans = digit[N%B] + ans

    # N 갱신
    N //= B


# print(ans)
print(ans)