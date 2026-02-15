S = input()

print(S)
print(len(S))

alphabet = "abcdefghijklmnopqrstuvwxyz"

for ch in alphabet:
    if ch in S:
        print(S.index(ch), end=" ")
    else:
        print(-1, end=" ")

