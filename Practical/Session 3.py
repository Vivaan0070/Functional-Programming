# Write your exercise solutions here
# 1.
set1 = []
number_of_elements_set1 = int(input("Enter the number of elements in the first set: "))

for a in range(number_of_elements_set1):
    element = input("Enter an element for the first set: ")
    set1.append(element)

set2 = []
number_of_elements_set2 = int(input("Enter the number of elements in the second set: "))
for b in range(number_of_elements_set2):
    element = input("Enter an element for the second set: ")
    set2.append(element)

set1 = set(set1)
set2 = set(set2)

print("First set:", set1)
print("Second set:", set2)
print("Elements common to both sets:", set1 & set2)


# 2.
students_grades = {}
for i in range(5):
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    students_grades[name] = grade

print("the student with the highest grade is:", max(students_grades, key=students_grades.get), "with grade:", students_grades[max(students_grades, key=students_grades.get)])