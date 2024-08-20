grades = [[5,3,3,5,4],[2,2,2,3,],[4,5,5,2],[4,4,],[5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = sorted(students)
grades_all = []
for i in grades:
    sum1 = sum(i)/len(i)
    grades_all.append(sum1)
dict1 = dict(zip(students_sort, grades_all))
print(dict1)


