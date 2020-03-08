from collections import OrderedDict

s = list(input())
set_s = list(set(s))

od = OrderedDict()
for i in set_s:
    od[i] = s.count(i)

ans = []

for key, val in od.items():
    print(key, val)
    if len(ans) <= 3:
        ans.append(key+str(val))
    else:
        print(ans)
        for a in ans:
            if val > int(a[1:]):
                ans.remove(a)
                ans.append(key+str(val))
print(ans)
