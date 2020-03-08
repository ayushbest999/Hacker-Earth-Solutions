def sockMerchant(n, ar):
    s = set(ar)
    count = []
    for i in s:
        c = ar.count(i)
        if c == 1:
            pass
        else:
            count.append(c)
    ans = []
    for z in count:
        a = z//2
        ans.append(a)
    return sum(ans)
a = sockMerchant(3,[10,20,30])
print(a)
