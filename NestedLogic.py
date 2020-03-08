# Enter your code here. Read input from STDIN. Print output to STDOUT
returned_date_list = list(map(int, input().split()))
#print(returned_date_list)

last_date_lst = list(map(int, input().split()))
#print(last_date_lst)

if returned_date_list[2] == last_date_lst[2]:
    if returned_date_list[1] <= last_date_lst[1]:
        if returned_date_list[0] <= last_date_lst[0]:
            print(0)
        else:
            a = returned_date_list[0] - last_date_lst[0]
            print(15*a)
    else:
        n = returned_date_list[1] - last_date_lst[1]
        ans = n*500
        print(ans)
elif returned_date_list[2] < last_date_lst[2]:
    print(0)
else:
    print(10000)