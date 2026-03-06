#### 약수들의 합

### 첫 풀이
"""
입력받은 수의 약수를 구함
입력받은 수 n을 for문으로 1부터 n-1까지 나누어서 약수를 구함

개선점
약수할때 1부터 n-1까지 나누는게 아니라 절반만 나누어도 구할 수 있음
print문에서 문자열 포매팅 사용
"""
import sys
input = sys.stdin.readline

while True:
    n = int(input())

    if n == -1:
        break

    n_list = []
    for i in range(1, n):
        if n % i == 0:
            n_list.append(i)
    if sum(n_list) == n:
        result = " + ".join(map(str, n_list))
        print(n, "=", result)
    else:
        print(n,"is NOT perfect.")



### 개선한 코드
import sys
input = sys.stdin.readline

while True:
    n = int(input())

    # -1이면 끝내기
    if n == -1:
        break

    # 약수 초기화
    divisors = [1]

    # 약수 구하기
    # 절반만 나누어도 구할 수 있음
    for i in range(2, int(n**0.5) + 1):
        # 약수이면 추가
        if n % i == 0:
            # 약수 리스트에 추가
            divisors.append(i)
            # 만약 n을 i로 나눈 몫이 i가 아니라면
            # 즉, i와 n // i가 다르면 몫도 추가
            if i != n // i:
                divisors.append(n // i)

    # 약수 정렬
    divisors.sort()

    # 약수 합이 n과 같으면 출력
    # f-string 사용
    if sum(divisors) == n:
        # 약수 리스트를 문자열로 변환하여 join을 활용해 출력
        print(f"{n} = {' + '.join(map(str, divisors))}")
    else:
        print(f"{n} is NOT perfect.")