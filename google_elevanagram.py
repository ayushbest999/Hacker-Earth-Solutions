from itertools import permutations

test_case = int(input())


def returnActualNum(n):
    actual_num_str = ''
    for z in n:
        actual_num_str += str(z)
    actual_num = int(actual_num_str)
    return actual_num


for a in range(test_case):
    list_arr = list(map(int, input().split()))
    number = []
    for b in range(len(list_arr)):
        n = list_arr[b]
        for c in range(n):
            number.append(b + 1)

    a_c = returnActualNum(number)

    ans = 'Case #' + str(a + 1) + ': '
    if a_c % 11 == 0:
        ans += 'YES'
        print(ans)
        break
    else:
        perm = permutations(number)
        for y in perm:
            a_c = returnActualNum(y)
            if a_c % 11 == 0:
                ans += 'YES'
                break
        ans += 'NO'
        print(ans)
        break
