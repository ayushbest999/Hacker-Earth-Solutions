no_of_students = int(input())
#print(no_of_students)
marks_list = []
for a in range(no_of_students):
    val = int(input())
    marks_list.append(val)

final_list = []
for b in marks_list:
    if b < 38:
        final_list.append(b)
    else:
        floor = b // 5
        val = (floor+1)*5 - b
        if val < 3:
            act_val = 5*(floor + 1)
            final_list.append(act_val)
        else:
            final_list.append(b)
#print(final_list)
for c in final_list:
    print(c)