#illbe honest i hugely ran out of time for this project, i have removed large chunks of it that just werent working to a standard i would be pleased to hand in
# i am aware this is a very bare bones program that could have had a lot more complexity and i canonly apologise
#that being said this program is meant as a simplified version of a school admin system to track the information or students and lecturers and classes as well as record aattendance at these classes

#main person class creates template for a person type object
class person():
    #define the basic info needed to create a person
    #TO DO - add validation to these using regex
    def __init__(self, FirstName:str , LastName:str , Email:str, PhoneNumber:str):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.PhoneNumber = PhoneNumber

    #getters and setters for various aspects of the person object
    def getInfo(self):
        return (f"first name: {self.FirstName} \nlast name: {self.LastName}\nemail: {self.Email}\nPhone number: {self.PhoneNumber}")
    
    #function to get the name of the individual
    def getname(self):
        return(self.FirstName + " "+ self.LastName)
    
    def setname(self):
        self.FirstName = input("new first name: ")
        self.LastName = input("new last name: ")
        return ("name has been set to "+self.FirstName+ " "+ self.LastName)
    
    def getEmail(self):
        return self.Email
    
    def setEmail(self):
        self.Email = input("new email: ")
        return ("email has been set to "+self.Email)
    
    def getPhoneNumber(self):
        return (self.PhoneNumber)
    
    def setPhoneNumber(self):
        self.PhoneNumber = input("new phone number: ")
        return("phone number has been set to "+ self.PhoneNumber)


#student class inheriting from person class
class student(person):
    #initialiser to create a new student type object
    def __init__(self, FirstName:str, LastName:str, Email:str, PhoneNumber:str, classes:list[str], attendanceRecord:list[str], accomAddress:str):
        super().__init__(FirstName, LastName, Email, PhoneNumber) # uses the parent class routine for common variables
        # additional factors unique to a student
        self.courses = classes
        self.attendanceRecord = attendanceRecord
        self.accomAddress = accomAddress

    #getters and setters for various aspects of the student object
    def getInfo(self):
        return (f"first name: {self.FirstName} \nlast name: {self.LastName}\nemail: {self.Email}\nPhone number: {self.PhoneNumber}\nattendance percentage: {self.getAttendancepercentage()}")

    def getclasses(self):
        classText = ""
        for Class in self.classes:
            classText = classText + Class + "\n"
        return classText
    
    def addclasses(self, className):
        self.classes.add(className)
        return("this students classes now are: \n"+self.getclasses())
    
    def removeclasses(self, className):
        self.classes.remove(className)
        return("this students classes now are: \n"+self.getclasses())
    
    def getAttendancepercentage(self):
        totalClasses = 0
        presentClasses = 0
        for mark in self.attendanceRecord:
            totalClasses = totalClasses+1
            if mark == "present":
                presentClasses = presentClasses + 1
        try:
            atendancePercentage = (100/totalClasses) * presentClasses
        except ZeroDivisionError:
            atendancePercentage = 0
        return atendancePercentage
    
    def addAttendancerecord(self, attendance):
        self.attendanceRecord = self.attendanceRecord.append(attendance)
    
    def GetAccomAdress(self):
        return self.accomAddress

    def setAccomAdress(self, address):
        self.accomAddress = address
        return ("the new adress is set as: "+ self.accomAddress)
        
    
            


#class lecturer inheriting from person class
class lecturer(person):
    #initialiser to create a new lecturer type object
    def __init__(self, FirstName:str, LastName:str, className:str, Email:str, PhoneNumber:str, studentList:list[student]):
        super().__init__(FirstName, LastName, Email, PhoneNumber) # uses the parent class routine for common variables
        # additional factors unique to a Lecturer
        self.className = className
        self.studentList = studentList
    
    #getters and setters for various aspects of the lecturer object
    def getClassName(self):
        return self.className

    def setClassName(self, classname):
        self.className = classname
        return ("the new class is called: "+ self.className)
    
    def getStudentList(self):
        return self.studentList
    
    def addStudent(self, student):
        self.listOfStudents.append(student)
        return("the updated list of students is: "+ self.getStudentList)
    
    def removeStudent(self, student):
        self.listOfStudents.remove(student)
        return("the updated list of students is: "+ self.getStudentList)
        
# create a register for a class
def RegisterClass( date, lecturer):
    classname = lecturer.getClassName()
    StudentList = lecturer.getStudentList()
    #create a register file with custom name for the course and date
    register = open(classname+date+".txt", "a") #will create the file if it doesnt exist or can be used to overwrite if an error was made on the day

    for student in StudentList:
        present = ""
        while present != "y" and present !="n":
            present = input("is "+ student.getname()+ " here: ")
        if present == "y":
            register.write(student.getname()+ ": present\n")
            student.addAttendancerecord("present")
        if present == "n":
            register.write(student.getname()+ ": absent\n")
            student.addAttendancerecord("absent")


        

def main():
    #initialise some students and lecturers to begin with
    student1 = student("Melanie","Sykes", "mel@email.com", "09432759", ["intro to electronics", "intro to programming"], [], "H3-02 keynes")
    student2 = student("April", "Summers", "Applesauce@kent.ac.uk", "095724878", ["intro to electronics"], [], "H2-02 keynes")
    lecturer1 = lecturer("steve", "backshall", "intro to electronics", "profesh@email.com", "293846238563", [student1, student2])
    lecturer2 = lecturer("honesty", "Plum", "intro to programming", "whazzup@email.com", "347623846", [student1])

    #test all of the different fucntions
    print(student1.getInfo())
    RegisterClass("22072006", lecturer1)
    #this was intended to eventually become a functioning selection menu
    print("welcome! what would you like to do? \n 1. take a register for a class \n2. register a new student \n3. register a new teacher\n4. find/change student information\n5. find/change teacher information\n6. something special")


#i have removed the testing file but this was put here so that the testing file could interract with this file and the computer knew where to run the code from
if __name__ == "__main__":
    main()