no_of_inputs = int(input())
dict = {}
for a in range(no_of_inputs):
    temp = list(map(str,input().split()))
    dict[temp[0]] = temp[1]

print(dict)
while True:
    a = input()
    if a in dict.keys():
        print(a+'='+dict[a])
    else:
        print('Not found')