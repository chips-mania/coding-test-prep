### 단어공부

word = input().upper()
ch_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
cnt_list = []
most_used_ch = ""

for i in range(len(ch_list)):
    cnt_list.append(word.count(ch_list[i]))

    # if max(cnt_list) < word.count(ch_list[i]):
    #     most_used_ch = ch_list[i]    

if cnt_list.count((max(cnt_list))) >= 2:
    print("?")
else:
    max_value = max(cnt_list)
    max_index = cnt_list.index(max_value)
    print(ch_list[max_index])