#### 블랙잭
"""
itertools의 combination으로 nC3 조합을 출력
-> 각 조합의 합에 조건을 걸어서 필터링

만약 itertools 안쓴다고하면 삼중 for문으로 구현

"""

from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0
temp_sum = 0

for card in combinations(cards, 3):
    temp_sum = sum(card)
    if temp_sum > M:
        continue
    elif temp_sum > ans:
        ans = temp_sum
    else:
        continue
        
print(ans)