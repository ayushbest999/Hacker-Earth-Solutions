from itertools import  combinations
testcase = int(input())
size = int(input())
array = list(map(int, input().split()))

combi = []
for i in range(1, size+1):
    combi.append(list(combinations(array, i)))

#len_subset = len(*combi)
splitted_arr = [*combi]
print(combi)
count = 0
ans = 0
for i in array:
    for a in combi:
        for b in a:
            if i in b:
                count += 1
    if i >= count:
        ans += i
    count = 0
print(ans)