#### 세 막대
"""
가장 긴 막대를 줄일 수 있으니 가장 긴 막대를 최대한으로 사용할 수 있는 길이를 찾을 것
"""
 # 첫 풀이
a,b,c = map(int, input().split())
len_list = [a,b,c]
max_len = max(len_list)
sum_len = sum(len_list) - max_len

# 긴 막대의 길이가 나머지 두 막대의 합보다 작으면 
# 긴 막대를 줄일 필요없음
if max_len < sum_len:
    print(sum_len + max_len)
else:
    # 긴 막대를 줄일 필요가 있음
    # max_len < sum_len 이어야 하므로 긴 막대의 최대길이는
    # sum_len - 1이 되어야 함
    max_len = sum_len - 1
    print(max_len + sum_len)