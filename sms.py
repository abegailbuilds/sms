

courses = set()
students = {}
lecturers = []
lecture_halls = ()
choice = 0


print("Welcome to the school management system!")
print("1. Add course")
print("2. Add student")
print("3. Add lecturer")
print("4. Add lecture hall")
print("5.Search student or course")
print("6. Remove course")
print("7. Update student details")
print("8. Exit")

while choice != 8:

    choice=int(input("Choose an option to continue: "))

    match(choice):
        case 1:

            course=input("Enter a course to add: ")
            courses.add(course)

        case 2:

                regNo=input("Enter Reg No for students to add: ")


                name=input("Enter Name: ")
                course_taking=input("Enter course: ")
                age=int(input("Enter Age: "))
                year=input("Enter Year: ")

                students[regNo]={
                    "name":name,
                    "course_taking": course_taking,
                    "age": age,
                    "year":year
                    }




        case 3:

            lecturer=input("Enter lecturer's name: ")
            lecturers.append(lecturer)
            print(type(lecturers))

        case 4:

            lecture_hall=input("Enter a room: ")
            lecture_halls=tuple(lecture_hall)
            print(type(lecture_halls))

        case 5:

            courseToSearch=input("Enter the course to search: ")

            if courseToSearch in courses:
                print("Course found!")
            else:

                print("Course not found!")

            studentToSearch = input("Enter the regNo of the student to search: ")
            print(students.get(studentToSearch))


        case 6:

            courseToRemove=input("Enter course to remove")
            courses.remove(courseToRemove)


        case 7:

            studentToUpdate=input("Enter regNo for student to update: ")
            newName=input("Enter new name: ")
            newCourseTaking=input("Enter new course: ")
            newAge=int(input("Enter new age: "))
            newYear=input("Enter new year of study: ")

            students["name"]=newName
            students["units"]=newCourseTaking
            students["age"]=newAge
            students["year"]=newYear



        case 8:
            print("Exitted!!!")
            break