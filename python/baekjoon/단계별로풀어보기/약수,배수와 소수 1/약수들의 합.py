#### 약수들의 합

import sys

input = sys.stdin.readline

while True:
    n = int(input())

    if n == -1:
        print("end")
        break

    n_list = []
    for i in range(1, n):
        if n % i == 0:
            n_list.append(i)
    if sum(n_list) == n:
        result = " + ".join(map(str, n_list))
        print(result)
    else:
        print(n,"is NOT perfect.")

