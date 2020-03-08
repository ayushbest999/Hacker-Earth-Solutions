def sockMerchant(n, ar):
    flag = 0
    for i in ar:
        ar.pop(0)
        print(ar)
        if i in ar:
            ar.remove(i)
            print(ar)
            flag += 1
        print('-----------------------')
    return flag
l = [10,20,20,10,10,30,50,10,20]
f = sockMerchant(9,l)
print(f)