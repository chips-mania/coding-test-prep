#### 소수

### 첫 풀이
"""
입력받은 수를 2부터 해당 수까지 나눠서 0이 되면 소수가 아니라고 판별
소수의 합과 최소값을 구함
소수가 없으면 -1을 출력

틀린 점
- 1을 소수로 판별하고 있음
- min을 쓸거면 sort는 불필요함
"""
M = int(input())
N = int(input())

prime_numbers = []

for i in range(M, N):
    is_prime = True
    for j in range(2, (i//2)+1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(i)
        
prime_numbers.sort()
if prime_numbers:
    print(sum(prime_numbers))
    print(min(prime_numbers))
else:
    print(-1)
            

### 개선한 코드
"""
- range(M, N+1)
- sort 제거
- 1은 소수로 판별하지 않도록
- is_prime 변수는 제거하고, 바로 break를 사용하여 소수가 아닌 경우 바로 종료
    ㄴ 나머지가 0이 아닌 경우만 리스트에 추가가

"""
M = int(input())
N = int(input())

prime_numbers = []

for i in range(M, N+1):
    if i < 2:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        prime_numbers.append(i)
            
if prime_numbers:
    print(sum(prime_numbers))
    print(min(prime_numbers))
else:
    print(-1)