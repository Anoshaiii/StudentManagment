# Student Management System using OOP
class StudentManagementSystem: # (creat a parent class)
  def __init__(self): # use constractor to initialize student data
    self.students = [] # create empty list to store dicitionry data
  def add_student(self): # create functon this function work is add student in list
    studentId = int(input("Enter your Id : ")) # take input from users
    name = input("Enter your name : ")
    age = int(input("Enter your Age : "))
    course = input("Enter your Course : ")
    print("Student Id",studentId)
    print("Student Name" , name )
    print("Student Age" , age )
    print("Student Course" , course)
    std_info = {"StudentId":studentId,"Name":name,"Age":age,"Course":course} # create a dictionary because data collect in key and value form
    self.students.append(std_info) # use append method because to add the student dicitionry into list
  def view_student(self): # create a function view student when i create this function is i watch save data of student
    for data in self.students: # using for loop because through each student in list
      print(data)
  def update_student(self): #use update function beacuse using the existing student id
    Student_Id = int(input("Enter Student Id: ")) # take input from user old id
    for data in self.students: # use loop for empty list
      if data["StudentId"] == Student_Id: # USE IF condition because check student id matched the entered id
        data["Name"] = input("Enter your name : ")
        print("Student Name" , data["Name"])
        data["Age"] = int(input("Enter your Age : "))
        print("Student Age" , data["Age"])
        data["Course"] = input("Enter your Course : ")
        print("Student Course" , data["Course"])
        print("Detail update successfully")
        break
    else:
      print("Student Not Found")
class std_management(StudentManagementSystem): # create a child class and inherit paraent class
  def view_student(self): # again create view function but print data of student
    for data in self.students:
      print("=== Student Information ===")
      print("Student Id" , data["StudentId"])
      print("Student Name" , data["Name"])
      print("Student Age" , data["Age"])
      print("Student Course" , data["Course"])
std_obj = std_management() # create an object of the child class
while True: # use while condition is display the menu until the user choose exit
    print("=== Student Management System ===") # create a menu bar
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Exit")
    choice = int(input("Enter your choice: 1-4 : ")) # user choose option
    if choice == 1: # use if condition and call all function and use break statment when i use 4 option so programe is closed
      std_obj.add_student()
    elif choice == 2:
      std_obj.view_student()
    elif choice == 3:
      std_obj.update_student()
    elif choice == 4:
      break
    else:
      print("Invalid choice. Please try again." ) # show error when user choose incorrect number
