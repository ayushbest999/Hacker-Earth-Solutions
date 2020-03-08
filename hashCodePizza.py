from itertools import permutations

max_pizza_slices, types_of_pizza = map(int, input().split())
slices = list(map(int, input().split()))

cart = []
for i in range(1, types_of_pizza):
    cart.append(list(permutations(slices, i)))

ans = set()
for i in cart:
    for j in i:
        a = sum(j)
        if a <= max_pizza_slices and a > sum(ans):
            ans = j

for i in ans:
    print(slices.index(i), end=' ')