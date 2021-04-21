# for
# while
# engineering 8

# for i in range(8):
#     print(i)

# i =0
# while i<8:
#     print(i)
#     i +=1
n_stud = int(input("Enter number of students: "))
max_marks = -1
max_student_id = 0
for i in range(n_stud):
    x = int(input("Enter marks of student "+ str(i+1) +": "))
    if x >= max_marks:
        max_marks = x
        max_student_id = i+1
print(max_student_id)
#
#
# for i in range(0,10,3):
#     print(i)

# Given a class for n students tell the index of the student with the highest marks