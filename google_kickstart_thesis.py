test_cases = int(input())
for a in range(test_cases):
    n_papers = int(input())
    l_papers = list(map(int, input().split()))
    l_of_lpapers = len(l_papers)
    final_arr = []

    global i
    i = 2
    while(len(final_arr) <= l_of_lpapers):
        for b in range(i):
            final_arr.append(i-1)
        i += 1
    ans = final_arr[:l_of_lpapers]
    z = a+1
    final_str = 'Case #'+str(a+1)+':'
    for c in ans:
        final_str += (' '+str(c))
    print(final_str)
