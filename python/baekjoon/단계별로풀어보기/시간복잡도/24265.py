#### 알고리즘 수업 - 알고리즘의 수행 시간 4
"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}

수행횟수는 첫번째 for문 -> n번
두번째 for문 
-> 2,3,4,5,6, 7 -> 6번
-> 3,4,5,6,7 -> 5번
-> ...

6+5+4+3+2+1 = 21

식으로 나타내면, n((n-1)/2)
"""
n = int(input())
print(int(n*((n-1)/2)))
print("2")

"""
그냥, n개 중에 두 개 뽑는 경우 nC2 -> (n(n-1))/2 로 외워도 무방

"""
