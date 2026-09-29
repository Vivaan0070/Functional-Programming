# -*- coding: utf-8 -*-
Session 6

subjects = ['math', 'english', 'physics', 'chemistry', 'biology']
marks = {}
total_marks_obtained = 0
max_total_marks = len(subjects) * 100

print("Enter marks for each subject:")
for i in range(len(subjects)):
    subject = subjects[i]
    mark = int(input(f"  Enter {subject.capitalize()} marks: "))
    marks[subject] = mark
    total_marks_obtained += mark


combined_percentage = (total_marks_obtained / max_total_marks) * 100
print(f"\nCombined percentage for all subjects: {combined_percentage:.1f}")


if combined_percentage >= 90:
    overall_grade = 'A'
elif combined_percentage >= 75:
    overall_grade = 'B'
elif combined_percentage >= 50:
    overall_grade = 'C'
else:
    overall_grade = 'F'

print(f"Overall Grade: {overall_grade}")
