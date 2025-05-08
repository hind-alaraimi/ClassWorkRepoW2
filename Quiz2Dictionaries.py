student_directory = {}
def add_student(directory, student_id, name, age):
    student_directory[student_id] = [name,age]
    if(student_id in student_directory):
        student_directory.update({student_id:[name,age]})

def remove_student(directory, student_id):
    if (student_id in student_directory.keys()):
        student_directory.pop(student_id)
    else:
        print("Student not found")
        
def display_students(directory):
    for k in student_directory:
        print(f"Student id: {k} - Name: {student_directory[k][0]} - Age: {student_directory[k][1]}")
        
add_student(student_directory, "101", "Ali", 20)
add_student(student_directory, "102", "Sara", 22)
add_student(student_directory, "103", "Ahmed", 19)
remove_student(student_directory, "102")
display_students(student_directory)