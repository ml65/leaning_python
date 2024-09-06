# Дополнительное практическое задание по модулю*

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print (type(students))
print (sorted(students))
ptr = 0
gratePointAverage = {}
for name in sorted(students):
    gratePointAverage[name]=sum(grades[ptr])/len(grades[ptr])
    ptr = ptr + 1

print (gratePointAverage)