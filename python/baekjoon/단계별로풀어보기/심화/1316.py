### 그룹 단어 체커

### 첫 풀이
"""
등장하는 스펠링을 담은 list를 만들고 그 리스트에 단어의 각 글자가 있는지 확인하는 방식
-> 동일한 스펠링이 연속해서 나오는 경우는 허용이기 때문에 확인 후 다른 경우에만 리스트에 넣고 연속되는 스펠링의 마지막만 리스트에 넣어서 중복 확인
-> 끝자리 중복 확인은 따로 했음
-> 다만 분기가 너무 많아서 코드가 지저분함 -> 더 좋은 방법이 있을 것 같음
-> 각 단어별로 리스트를 초기화 하는것 주의
"""
# 입력 단어 개수
num = int(input())

# 그룹 단어 개수 초기화
ans = 0

# 등장하는 스펠링을 담은 list
# ch_list = []

# num만큼 반복
for _ in range(num):  
    word = input()
    ch_list = []
    # print("입력단어:", word)
    is_group_word = True
    
    for i in range(len(word)-1):
        if word[i] != word[i+1] and word[i] not in ch_list:
            ch_list.append(word[i])
        elif word[i] == word[i+1]:
            pass
        elif word[i] in ch_list:
            is_group_word = False
            # print(word[i], "중복발생")
        else:
            # print(word[i], i, "예외발생")
            break
    if word[-1] in ch_list:
        is_group_word = False
        # print(word[-1], "끝자리 중복발생")
    if is_group_word:
        ans += 1
        # print(word, "그룹단어")
        
print(ans)


### 정답 풀이
num = int(input())

# 그룹 단어 개수 초기화
ans = 0

for _ in range(num):
    word = input()
    
    # 등장한 글자 중복 확인 -> 리스트보다 셋을 사용하면 검색이 더 빠름
    seen = set()
    
    # 이전 글자
    prev = ''
    
    # 그룹 단어 여부
    is_group_word = True

    # 단어의 각 글자를 순회
    for ch in word:
        # 이전 글자와 다르고
        if ch != prev:
            # 글자 리스트에 존재하는 글자라면 그룹 단어가 아니므로 바로 break
            if ch in seen:
                is_group_word = False
                break

            # 글자 리스트에 추가 -> set이므로 중복확인 필요 없음
            seen.add(ch)

        # 이전 글자 업데이트
        prev = ch

    if is_group_word:
        ans += 1

print(ans)