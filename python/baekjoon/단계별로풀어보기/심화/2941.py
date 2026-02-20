# ### 크로아티아 알파벳

## 첫 풀이
# word = input().strip()
# alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# cnt = 0
# length = len(word)
# for i in alphabets:
#     if i in word:
#         cnt += word.count(i)
#         length -= len(i)
#         word = word.replace(i, " ")

#         print(i)
#         print("length of", i, "is", len(i))
#         print("length of word is", length)
#         print("cnt is", cnt)
#         print(word.count(i))

# print(length + cnt)


## 수정 후 풀이
s = input().strip()
# 인덱스
i = 0
# 크로아티아 알파벳 개수
count = 0

# 인덱스가 문자열의 길이보다 작을 때 반복
while i < len(s):
    # dz= 먼저 확인 (3글자)
    # 입력받은 문자의 특정 인덱스에 위치한 단어가 dz=와 같으면 인덱스를 3 증가시키고 크로아티아 알파벳 개수를 1 증가시킴
    if s[i:i+3] == "dz=":
        i += 3
    
    # 글자 패턴 확인
    # 입력받은 문자의 특정 인덱스에 위치한 단어가
    # c=, c-, d-, lj, nj, s=, z= 중 하나와 같으면 인덱스를 2 증가시키고 크로아티아 알파벳 개수를 1 증가시킴
    elif s[i:i+2] in ["c=", "c-", "d-", "lj", "nj", "s=", "z="]:
        i += 2
    
    # 일반 문자
    else:
        i += 1
    
    count += 1

print(count)