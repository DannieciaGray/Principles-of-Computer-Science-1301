'''
Description: This code will  write a program that stores student’s exam
grades as a list and student attendance as a set. The program will print out the answers to
the following questions:
1. Grades
a. How many students took the exam?
b. What was the highest exam grade?
c. What was the lowest exam grade?
d. What was the class average for the exam?
2. Attendance
a. How many students attended the class?
b. Who attended both days of class?
c. Who attended only one day of class?
 

Author: Danniecia
'''
#stores exam grades in list
exam_grades=[ 83, 85, 72, 65, 76, 90,89,70,100]

#stores students who attended day one in set 
attendance_day1={"Trent","Jake","Mahmoud","Alex","Sam","Percy"}

#stores students who attended day two in set 
attendance_day2={"Trent","Mary","Mahmoud","Alex","Sam","John","Larry"}

#outputs # of students who took the exam, highest grade, lowest grade, class average
print(len(exam_grades),"Students took the exam.")
print("The highest grade was a",max(exam_grades))
print("The lowest grade was a",min(exam_grades))
print("The average grade for the exam was a ",sum(exam_grades)//len(exam_grades))

#prints new line
print("")

#prints # students who attended class, # who attended both, # who attended one class
print(len(attendance_day1), "students attended the class.")
print(set.intersection(attendance_day1,attendance_day2),"attended both class days.")
print(attendance_day1.symmetric_difference(attendance_day2),"attended one class day.")