binary = int(input())
n = binary
ans_list = []
flag = True
count = 0
count_list = []

while flag:
    if n // 2 >=1:
        print(n)
        ans_list.append(n % 2)
        n = n//2
    else:
        ans_list.append(n % 2)
        flag = False
    print('--------------')
print(ans_list)
ans_list.reverse()
print(ans_list)

for i in range(len(ans_list)):
    if ans_list[i] == 1:
        a = i
        while(ans_list[a] == 1):
            print(a)
            count += 1
            if (a + 1) < len(ans_list):
                a += 1
            else:
                break
            print('-----------')

        count_list.append(count)
        count = 0
print(count_list)
print(max(count_list))