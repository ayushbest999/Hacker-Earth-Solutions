# Enter your code here. Read input from STDIN. Print output to STDOUT

test_case = int(input())
for _ in range(test_case):
    no = int(input())
    if no == 2 or no == 3:
        print('Prime')
    elif no % 2 == 0:
        print('Not prime')
    elif no == 1 :
        print('Not prime')

    else:
        global flag
        flag = True
        half = no//2
        l = []
        for i in range(3,half,2):
            l.append(i)
        #print(l)
        for i in l:
            if no % i == 0:
                flag = False
        if flag == True:
            print('Prime')
        else:
            print('Not prime')