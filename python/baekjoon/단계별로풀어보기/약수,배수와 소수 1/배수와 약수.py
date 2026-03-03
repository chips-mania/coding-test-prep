#### 배수와 약수
"""
1. 입력받은 두 수를 비교하여 배수인지 약수인지 판별
2. 배수인 경우 "multiple" 출력
3. 약수인 경우 "factor" 출력
4. 배수도 약수도 아닌 경우 "neither" 출력



"""


import sys
input = sys.stdin.readline
print("start")

while True:
    a, b = map(int, input().strip().split())
    # print(a, b)
    if a == 0 and b == 0:
        break
    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")
print("end")


