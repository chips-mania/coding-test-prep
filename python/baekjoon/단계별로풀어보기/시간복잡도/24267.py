#### 알고리즘 수업 - 알고리즘의 수행 시간 6

"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}

n개 중 세개 뽑기 -> nC3 -> n(n-1)(n-2) / 3!

"""

n = int(input())
print(n*(n-1)*(n-2)//6)
print(3)