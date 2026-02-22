#### 세로읽기

### IndexError

## 첫 풀이
"""
논리적으로는 맞는데, 첫번째 row를 기준으로하고있어서 첫번째 row가 짧으면 전체를 못 읽는 경우가 있을 수 있음
-> 따라서, 첫번째 row의 길이를 기준으로 하는 것이 아니라, 가장 긴 row의 길이를 기준으로 해야함

"""
rows = {}
ans = []
for i in range(5):
    rows[i] = input()

    
for i in range(len(rows[0])):
    for j in range(5):
        try:
            # rows[1-5][0-100]
            print(rows[j][i], end = "")
        except IndexError:
            pass
print()


### 수정 후 풀이
rows = {}
max_len = 0
for i in range(5):
    rows[i] = input()

    # max_len 갱신
    max_len = max(max_len, len(rows[i]))

    
for i in range(max_len):
    for j in range(5):
        try:
            print(rows[j][i], end = "")
        except IndexError:
            pass
print()







