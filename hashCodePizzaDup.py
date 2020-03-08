from itertools import permutations

k_m, slices = list(map(int, input().split())), list(map(int, input().split()))
cart = [list(permutations(slices, i)) for i in range(1, k_m[1])]
ans = set()
for i in cart:
    for j in i:
        a = sum(j)
        if a <= k_m[0] and a > sum(ans):
            ans = j
print(len(ans))
for i in ans:
    print(slices.index(i), end=' ')