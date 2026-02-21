### 너의 평점은은

# 과목 평점 표
d = {"A+":4.5,
"A0":4.0,
"B+":3.5,
"B0":3.0,
"C+":2.5,
"C0":2.0,
"D+":1.5,
"D0":1.0,
"F"	:0.0}

# 총 학점
hak = 0
# 총 평점
pyeong = 0

while True:
    try:
        c, p, g = input().split()
        # print("c:", c, "p:", p, "g:", g)
        p = float(p)
       
        # 등급이 P가 아니면 
        if g != "P":
            # 총학점에 과목별 학점을 더함
            hak += p
            # 과목평점표에서 등급별 평점을 가져오고 학점을 곱해서 총 평점에 더함
            pyeong += d.get(g)*p
        else:
            pass
        
    except:
        break
        
# 전공평점은 총 평점을 총학점으로 나눔
print(pyeong/hak)