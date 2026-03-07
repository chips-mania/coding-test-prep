#### 소수찾기


### 첫 풀이
"""
개수와 수들을 입력받은 후 입력받은 수를 2부터 해당 수까지 나눠서 0이 되면 소수가 아니라고 판별
cnt를 1 더하고 마지막으로 N에서 cnt를 빼서 소수의 개수를 구함

개선점
- cnt가 소수의 개수가 아닌 소수가 아닌 수이므로 직관성이 떨어짐
- 1을 따로 처리하고 있는데, 하나의 로직으로 묶을 방법이 있는지 찾아볼것
- 불필요하게 끝까지 탐색함 -> 약수는 절반까지만 탐색해도 됨
    ㄴ break를 이용하긴하지만 소수의 경우에는 전체 탐색을 해야하므로 비효율적임

"""
N = int(input())
numbers = list(map(int, input().split()))
cnt = 0

for i in range(N):
    if numbers[i] == 1:
        cnt += 1
    else:
        for j in range(2, numbers[i]):
            if numbers[i] % j == 0:
                cnt += 1
                break
            
print(N - cnt)


### 개선한 코드
N = int(input())
numbers = list(map(int, input().split()))
# 소수의 개수
cnt = 0

for number in numbers:
    if number == 1:
        continue
    # 소수인지 판별
    isprime = True

    # 절반까지만 탐색
    for i in range(2, int(number**0.5) + 1):
        # 만약 약수를 발견하면
        if number % i == 0:

            # 소수가 아니므로 False로 변경
            isprime = False
            # 더 이상 탐색할 필요가 없으므로 break
            break
    
    # 해당 수는 소수가 아니므로 cnt를 1 더함
    if isprime:
        cnt += 1

# 입력받은 수를 모두 탐색한 후 소수의 개수를 출력
print(cnt)


    