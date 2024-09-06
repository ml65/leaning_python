# Дополнительное практическое задание по модулю*

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Решение без циклов
grades_m = [sum(grades[0])/len(grades[0]),
            sum(grades[1])/len(grades[1]),
            sum(grades[2])/len(grades[2]),
            sum(grades[3])/len(grades[3]),
            sum(grades[4])/len(grades[4])]

students_sort = sorted(students)

dict1 = dict(zip(students_sort, grades_m))
print (dict1)

# Решение с циклами
ptr = 0
gratePointAverage = {}
for name in sorted(students):
    gratePointAverage[name]=sum(grades[ptr])/len(grades[ptr])
    ptr+=1

print (gratePointAverage)