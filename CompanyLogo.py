string = input()
set = set(string)
#print(set)

dict = {}
for a in set:
    dict[a] = string.count(a)
print(dict)

inverse = [(value,key) for key, value in dict.items()]

print(max(inverse))
print(inverse)

final_list = []
count_list = []
for b in range(3):
    maximum = max(inverse)
    inverse.remove(maximum)
    maximum = list(maximum)
    print(maximum)
    final_list.append(maximum[1])
    count_list.append(maximum[0])
print(final_list)
print(count_list)

#for a in range(len(count_list)):
 #   if count_list[a] == count_list[a+1]:

