max_str = 0
a = input().split("student_")
for i in a[1:]:
    if int(i[3:]) > max_str:
        max_n = i[:3]
    elif int(i[3:]) == max_str:
        max_n += "-" + i[:3]
print(max_n)
