
"""
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


courses=set({})

students={}

halls=()

choice=0
lecturers=[]

def addStudents():

    regno=input("Enter reg no: ")
    name=input("Enter name: ")
    course=input("Enter course: ")
    year=input("Enter year: ")

    if regno not in students.keys():
        students[regno]={}

        students[regno]["name"]=name
        students[regno]["course"]=course
        students[regno]["year"]=year


        print("The student has been added!")
    else:
        print("this student alreadiy exists!!")
        return


def addLecturers():

    lecturerName=input("Add a lecturer name: ")

    if lecturerName in lecturers:
        print("This lecturer already exists!!")
        return
    else:
        lecturers.append(lecturerName)
        print("Lecturer added!!")

def addHalls():


    halls=input("Enter your halls(comma separated)")

    halls=halls.split(",")

    halls=tuple(h.strip() for h in halls)

    print("Lecturer halls added!")

    for hall in halls:
        print(hall)



def search():
    searchString=input("Enter an adm no to search")

    if searchString not in students.keys():
        print("Student was not found!!")
        return

    else:
        print(f"Student found: {students.get(searchString)}")

def remove():
    searchString=input("Enter a student to remove: ")

    if searchString not in students.keys():
        print("The student cannot be found! ")
        return
    else:
        del students[searchString]

        print("The student has been removed!!")

def edit():
    searchString=input("Enter the student to update: ")
    newName=input("Enter new name or leave blank to ignore: ")
    newCourse=input("Enter new course or leave blank to ignore: ")
    newYear=input("Enter new year or leave blank to ignore: ")

    if searchString not in students.keys():
        print("Student can't be edited, not found!")
        return
    if len(newName) <=0:
        pass
    else:
        students[searchString]["name"]=newName

    if len(newCourse) >=0:
        students[searchString]["course"]=newCourse
    else:
        pass

    if len(newYear) <=0:
        pass
    else:
        students[searchString]["year"]=newYear

    print("Student has been updated!!")

def main():
    global choice
    while choice !=8:
        print("1. Add student")
        print("2. Add lecturer")
        print("3. Add Halls")
        print("4. Search Students")
        print("5. Remove Students")
        print("6. Edit Students")
        print("7. Exit")

        choice=int(input("Please choose an option 1-8"))

        match choice:
            case 1:
                addStudents()
            case 2:
                addLecturers()
            case 3:
                addHalls()
            case 4:
                search()
            case 5:
                remove()
            case 6:
                edit()

            case 7:

                break




if __name__=="__main__":
    main()

"""

#advanced data manipulation
#1. list comprehension
#e.g square of numbers

#syntax -[expression loop condition]
"""
nums=[1,2,3,4,5,6,7,8,9]
squares=[]
for num in nums:
        squares.append(num**3)


print(squares)


print([x**3 for x in nums])

students=["eb1/74310","eb1/6545","eb1/76584"]

for student in students:
    if student=="":
        print("Found")

print([student for student in students if "eb1/74310" in students])

"""


nums=[3,5,8,11,14,24,35,66,13,19]

result=[[23],[56],[32]]
print([num for num in nums if num % 2!=0])

print([i for i in range(3,19) if i % 2 !=0])

print([value for value in result for value in value])



#set comprehensions
nums={1,2,3,4,5,67,8,9}

print(
    {x for x in nums if x %  2==0 }
)

#dictionary
myStudents={
    "eb1":{
        "name":"idontknow",
        "email":"weemzee@gmail.com",
        "school":"myschool"
    },
    "eb2": {
        "name": "idontknow1",
        "email": "weemzee@gmail.com",
        "school": "myschool"
    },
    "eb3": {
        "name": "idontknow2",
        "email": "weemzee@gmail.com",
        "school": "myschool"
    }

}

"""for key, value in myStudents.items():
    print(key, "=" ,value)

"""

#dict x: value for key in value.items()
print(
    {
        key: value for key ,value in myStudents.items() if key == "eb2"
    }
)
print({key: value for key, value in myStudents.items() })


keys=["name","age","phone"]
values=["wee",23,"0712345678"]

print({key: value for key,  value in zip(keys,values)})

myClients={
    "ererere":{
        "name":'client1',
        "age":20,
        "date":"1/1/2026",
        "date Due": "14/1/2026",
        "days due":10
    },
    "erererw":{
        "name":"client2",
        "age":34,
        "date":"1/1/2026",
        "date Due": "14/1/2026",
        "days due":10
    },
    "rrererw":{
        "name":"client3",
        "age":34,
        "date":"10/10/2026",
        "date Due": "24/10/2026",
        "days due":0
    }
}



print({key: value for key, value in myClients.items() if value["days due"] > 0})



myQueue=[1,2,3,4,5,67,8,9,89]
#yield - used to specify a generator expression(only used inside a function(
#next-used to update the status of a generator expression
#iter-keyword to creator a generator expressions from an object iterable

"""
def myQueue():
    num=0
    print("We are at num: " + str(num))


    yield num

    num+=1
    print("We are at num: " + str(num))


    yield num

    num+=1
    print("We are at num: " + str(num))

    yield num

gen=myQueue()

next(gen)

next(gen)

next(gen)

"""

gen=iter(myClients)

print(next(gen))
print(next(gen))
print(next(gen))

#abbie's change
print(next(gen))


def test():
    return 1+1



