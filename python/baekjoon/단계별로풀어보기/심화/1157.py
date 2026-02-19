### 단어공부

# 첫 풀이
# word = input().upper()
# ch_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# cnt_list = []
# most_used_ch = ""

# for i in range(len(ch_list)):
#     cnt_list.append(word.count(ch_list[i]))

# if cnt_list.count((max(cnt_list))) >= 2:
#     print("?")
# else:
#     max_value = max(cnt_list)
#     max_index = cnt_list.index(max_value)
#     print(ch_list[max_index])

# 정석풀이
from collections import Counter

word = input().upper()
counter = Counter(word)

# 가장 많이 나온 문자
# most_common()이란 Counter 객체에 들어있는 (원소, 개수)를 개수 기준으로
# 내림차순 정렬해서 리스트로 반환하는 메서드
# 예시: mama -> [('M', 2), ('A', 2)]
most_common = counter.most_common()
print(most_common)

# 가장 많이 나온 문자의 개수
most_common_count = most_common[0][1]

# 그 개수가 여러개인지 확인
if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    print("?")
else:
    print(most_common[0][0])
