#update of the first 'students program'
import operator

def allStudents(): #gets info of all of the students
    print("Enter the number of students: ")
    numberofStudents = int(input()) #it has to be an int number since i'll call it in a for loop
    studentsData = {} #this is where all the data will be stored
    for student in range (0, numberofStudents): #this for loop will keep running till the number of students be fullfiled
        print("Enter the name of the student: ")
        names = input()
        print("Enter their mark points: ")
        marks = int(input())
        studentsData[names] = marks #dictionary[key] = value
    return studentsData #this statement will make sure i can call the data inside of this function later on

def rankOfStudents(studentsData): #this is calling a previous dictionary as an operator
    try:
        print()
        sortedstudentsData = sorted(studentsData.items(), key = operator.itemgetter(1), reverse=True)
        #turnin dict into a sorted tuple list (highest to lowest value using operator library)
        print("{} has scored {} marks and secured the first place!".format(sortedstudentsData[0][0], sortedstudentsData[0][1]))
        print("{} has scored {} marks and secured the second place!".format(sortedstudentsData[1][0], sortedstudentsData[1][1]))
        print("{} has scored {} marks and secured the third place!".format(sortedstudentsData[2][0], sortedstudentsData[2][1]))
        return sortedstudentsData # I will use this data in the next function
    except IndexError:
        print("Enter a minimum of 3 students")
        quit()

def prizeReward(sortedstudentsData, reward): #this'll be the 2 operators i'll be using in this function
    print()
    print("1st place: {} has won ${}!".format(sortedstudentsData[0][0], reward[0]))
    print("2nd place: {} has won ${}!".format(sortedstudentsData[1][0], reward[1]))
    print("3rd place: {} has won ${}!".format(sortedstudentsData[2][0], reward[2]))

def appreciationStudent(sortedstudentsData):
    print()
    for data in sortedstudentsData:
    #this for loop will run over all the students data list testing if they scored 950 or over.
        if data[1] >= 950: #the [1] calls the VALUE of the dictionary over than the KEY. Key would be [0].
            print("Congratulations on scoring {} points, {}".format(data[1], data[0]))
        else:
            break


studentsData = allStudents()
sortedstudentsData = rankOfStudents(studentsData)
reward = (500, 300, 100)
prizeReward(sortedstudentsData, reward)
appreciationStudent(sortedstudentsData)
