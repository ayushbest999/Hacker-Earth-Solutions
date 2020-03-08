test_case = int(input())
for i in range(test_case):
    size_arr = int(input())
    arr = list(map(int, input().split()))
    queries = int(input())
    li = list(map(int, input().split()))
    ri = list(map(int, input().split()))
    for j in range(len(li)):
        total = 0
        li_val = li[j]    # 1 3 4
        ri_val = ri[j]    # 4 7 10

        index_li = li_val % len(arr) - 1
        if index_li == -1:
            index_li += 1

        index_ri = ri_val % len(arr) - 1

        print(index_li)
        print(index_ri)
        if index_ri < index_li:
            if ri_val - li_val > len(arr):
                a = (ri_val - li_val) // len(arr)
                total = 2*sum(arr)
            for k in range(index_li, len(arr)):
                total += arr[k]
            for k in range(0, index_ri+1):
                total += arr[k]
        elif index_ri == index_li:
            s = sum(arr)
            total = s + arr[index_ri]
        else:
            for k in range(index_li, index_ri + 1):
                total += arr[k]

        print('sum is', total)