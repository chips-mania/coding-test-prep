#### 세탁소 사장 동혁


### 첫 풀이
"""
1. 입력받은 돈을 25, 10, 5, 1로 나누어서 몫을 구함
2. 나머지는 다음 단위로 나누어서 몫을 구함
"""
T = int(input())
ans = []
for _ in range(T):
    C = int(input())
    quarter = C // 25
    dime = (C-quarter*25) // 10
    nickel = (C-quarter*25-dime*10) // 5
    penny = C-quarter*25-dime*10-nickel*5

    # end = "" 사용하여 줄바꿈 없이 출력
    # -> 불필요요
    print(quarter, dime, nickel, penny, end = "")
    print()



# 수정 후 풀이
T = int(input())

for _ in range(T):
    C = int(input())
    
    quarter = C // 25
    # 나머지 연산자 사용하여 나머지 값을 계속 업데이트
    C %= 25
    
    dime = C // 10
    C %= 10
    
    nickel = C // 5
    C %= 5
    
    penny = C
    
    print(quarter, dime, nickel, penny)