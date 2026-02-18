### 별찍기 - 7

n = int(input())

for i in range(1, 2*n):
    if i <= n:
        print((n-i)*" "+(2*i-1)*"*")
    else:
        m = i-n
        print((m)*" "+(2*n-2*m-1)*"*")