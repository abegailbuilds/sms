

courses = set()
students = {}
lecturers = []
lecture_halls = ()
choice = 0
while choice != 8:

    print("Welcome to the school management system!")
    print("1. Add course")
    print("2. Add student")
    print("3. Add lecturer")
    print("4. Add lecture hall")
    print("5.Search student or course")
    print("6. Remove course")
    print("7. Update student details")
    print("8. Exit")
    choice=int(input("Choose an option to continue: "))

    match(choice):
        case 1:

            course=input("Enter a course to add: ")

            if len(course)<=0:
                print("enter a valid course")
                break

            if course not in courses:
                print("the course exists!")
                break

            courses.add(course)
            print("the course was added !")

        case 2:

                regNo=input("Enter Reg No for students to add: ")
                name=input("Enter Name: ")
                course_taking=input("Enter course: ")
                age=int(input("Enter Age: "))
                year=input("Enter Year: ")


                #check and create dict for the student if they dont exist
                if regNo not in students.keys():
                    students[regNo]={
                        "name":name,
                        "course_taking": course_taking,
                        "age": age,
                        "year":year
                        }

                    print("student was added")
                else:
                    print("the student already exists!")
                    break
        case 3:

            lecturer=input("Enter lecturer's name: ")
            if lecturer in lecturers:
                print("the lecturer already exists!")
                break
            else:

                lecturers.append(lecturer)
                print(type(lecturers))

        case 4:

            lecture_hall=(input("Enter a room(comma separated): "))

            lecture_hall=lecture_hall.split(",")

            print(lecture_hall)

            lecture_halls=tuple(h.strip() for h in lecture_hall)


            print(type(lecture_halls))

        case 5:

            courseToSearch=input("Enter the course to search: ")

            if courseToSearch in courses:
                print("Course found!: "+str(courseToSearch))

            else:

                print("Course not found!")

            studentToSearch = input("Enter the regNo of the student to search: ")

            print(students.get(studentToSearch))


        case 6:

            courseToRemove=input("Enter course to remove")

            if courseToRemove not in courses:
                print("Course not found!!")
                break
            else:
                courses.remove(courseToRemove)
                print("Course was removed!!")


        case 7:

            studentToUpdate=input("Enter regNo for student to update: ")
            newName=input("Enter new name (or leave empty to ignore): ")
            newCourseTaking=input("Enter new course (or leave empty to ignore): ")
            newAge=int(input("Enter new age (or leave empty to ignore): "))
            newYear=input("Enter new year of study (or leave empty to ignore): ")

            if studentToUpdate not in students.keys():
                print("Could not update student, student not found!")
                break
            else:

                if newName =="":
                    pass
                else:
                    students[studentToUpdate]["name"]=newName

                if newCourseTaking =="":
                    pass
                else:
                    students[studentToUpdate]["units"]=newCourseTaking

                if len(age) <=0:
                    pass
                else:

                    students[studentToUpdate]["age"]=newAge

                if len(year)>=0:
                    students[studentToUpdate]["year"]=newYear
                else:
                    pass

                print("The student was successfully updated!!")

        case 8:
            print("Exitted!!!")
            break
