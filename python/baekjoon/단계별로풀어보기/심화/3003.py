### 킹, 퀸, 룩, 비숍, 나이트, 폰

# 첫 풀이
"""
리스트끼리 산술연산은 안되는데 그냥 빼려고해서 틀림
-> 따라서, 리스트의 각 원소를 빼야함
"""
# pieces = list(map(int,input().split()))
# std = [1,1,2,2,2,8]
# ans = std - pieces
# print(*ans)


# 두 번째 풀이
"""
입력은 동일하게 하되 리스트 컴프리헨션과 zip()을 사용해서 풀이
-> zip()은 두 개의 리스트를 하나씩 묶어주는 함수
-> 따라서, std와 pieces의 각 원소를 묶어서 a와 b에 할당
-> 그 후, a - b를 계산하여 result 리스트에 추가
-> 마지막으로, result 리스트의 각 원소를 출력
"""
pieces = list(map(int,input().split()))
std = [1,1,2,2,2,8]
result = [a - b for a, b in zip(std, pieces)]
print(*result)