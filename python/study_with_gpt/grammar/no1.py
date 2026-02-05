# 이건 에러남
# map은 이렇게 써야함 -> map(함수, iterable)
# 따라서, words = list(map(int, input().split())) 이런식으로 쓰는게 맞는데,
# 이 코드는 str을 숫자로 바꿔서 리스트로 만드는 코드임
# words = list(map(input().split()))

# input()으로 한줄 문자열을 받고, 
# split()으로 공백 기준으로 쪼개서 문자열 리스트를 만듦
words = input().split()
# words = ["abc", "ab1", "hello", "123test", "go"]

result = []

# 첫번째 w는 "abc"
for w in words:
	
	# 길이 체크
	# 길이가 1,2는 continue -> 이번 반복만 건너뛰고 다음 반복으로
	# break는 -> 지금 반복문을 완전히 종료
	if len(w) < 3:
		continue
		
	# 숫자 포함 여부
	has_digit = False
	
	
	# ch는 character
	# 첫번째 ch = "a"
	for ch in w:
	
		# .isdigit()은 문자열에 붙여쓰는 메서드 숫자면 True
		# if True: -> 이게 true여야 뒤로감?
		if ch.isdigit():
			# 
			has_digit = True
			break
		
	# 이게 없으면 숫자가 있던 없던 append
	if has_digit:
		continue	
	result.append(w)
	
if not result:
	print("EMPTY")
else:
	# *을 붙이면 리스트를 풀어서 원소들을 print에 개별 인자로 넘김
	# 공백으로 구분되어 한줄로 출력됨
	# sep 인자를 넣으면 구분자를 바꿀 수 있음
	print(*result)