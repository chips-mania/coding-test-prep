#### 수학은 비대면강의입니다
"""
크래머 공식 활용
→ 연립 일차 방정식을 행렬식으로 바로 푸는 공식
→ 미지수 2개 짜리 연립방정식에서 자주 사용됨
"""
a,b,c,d,e,f = map(int, input().split())

det = a*e - b*d
x = (c*e - b*f) // det
y = (a*f - c*d) // det

# print(a,b,c,d,e,f)
print(x,y)