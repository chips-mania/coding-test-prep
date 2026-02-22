### 최댓값

## 첫 풀이
"""
전체 최댓값, 각 줄의 최댓값, 최댓값의 인덱스, 최댓값이 몇째 줄인지 저장
-> 입력받은 각 행에서 최대값을 찾고 그 값이 최댓값이면 그 값을 전체 최댓값으로 갱신
-> 최댓값의 인덱스도 갱신
-> 각 줄의 최댓값도 갱신
-> 최댓값이 몇째 줄인지도 갱신
"""
# 전체 최댓값
max_num = 0
# 최댓값의 인덱스
max_idx = 0
# 각 줄의 최댓값
max_temp = 0
# 최댓값이 몇째 줄인지
max_i = 0

for i in range(9):
    temp_list = (list(map(int, input().split())))
    max_temp = max(temp_list)
    
    if max_temp > max_num:
        max_num = max_temp
        # temp_list.index(max_temp)가 더 안전하다고함함
        max_idx = temp_list.index(max_num)
        max_i = i
print(max_num)
print(max_i+1, max_idx+1, end = " ")



## 개선한 코드
max_num = 0
max_row = 0
max_col = 0

for i in range(9):
    row = list(map(int, input().split()))
    
    # 값을 하나하나씩 비교하면서 최댓값을 찾음
    for j in range(9):
        if row[j] > max_num:
            max_num = row[j]
            max_row = i
            max_col = j

print(max_num)
print(max_row + 1, max_col + 1)