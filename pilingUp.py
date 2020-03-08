test_cases = int(input())


for a in range(test_cases):
    def max_el_finder(l):
        #print(l)
        max_el = max(l)
        a = [l[0], l[len(l) - 1]]
        if max_el in a:
            return max_el
        else:
            return "No"
    n_cubes = int(input())
    length_list = list(map(int, input().split(' ')))
    #print(length_list)
    final_list = []
    flag = True

    while len(length_list) > 0 :
        val = max_el_finder(length_list)
        if val != 'No':
            final_list.append(val)
            print(val)
            length_list.remove(val)
        else:
            flag = False
            print('No')
            break

    if flag == True:
        print('Yes')


