#### 알고리즘 수업 - 알고리즘의 수행 시간 2

"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        sum <- sum + A[i]; # 코드1
    return sum;
}

-> 코드1의 수행횟수는 n번
-> 수행 시간이 n에 비례하므로 시간복잡도는 O(n)

🧠 감각 잡는 팁
이 문제 시리즈는 다 같은 패턴임:
코드 형태	실행 횟수	시간복잡도	차수
한 번 실행	1	         O(1)	    0
for문 1개	n	        O(n)	    1
for문 2중	n²	        O(n²)	    2


"""

print(int(input()))
print("1")

