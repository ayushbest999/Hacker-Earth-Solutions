N = int(input())
ans = []
for N_itr in range(N):
    firstNameEmailID = input().split()

    firstName = firstNameEmailID[0]
    emailID = firstNameEmailID[1]

    mail = emailID.split('@')
    if mail[1] == 'gmail.com':
        ans.append(firstName)
s_list = sorted(ans)
for item in s_list:
    print(item)
    