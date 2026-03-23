#### 소인수분해

### 첫 풀이
N = int(input())

while N > 1:
    for i in range(2,N+1):
        if N%i == 0:
            # print(f"N = {N}")
            N = N//i
            # print(f"N//i = {N}")
            print(i)
            break