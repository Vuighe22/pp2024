
# define a list to store inform of Student
List_St = []
List_Cs = []
List_Mark = []

# Check Date valid or invalid
def check_date(date, month, year):
    a = False
    if month == 2:  # moth 2
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):  # leap year
            if 0 < date <= 29:
                a = True
        else:
            if 0 < date <= 28:
                a = True
    elif month in [1, 3, 5, 7, 8, 10, 12]:  # month 1,3,5,7,8,10,12
        if 0 < date <= 31:
            a = True
    elif month in [4, 6, 9, 11]:  # month 4,6,9,11
        if 0 < date <= 30:
            a = True
    return a


# class for Students
class Student:
    def __init__(self,name,id,DoB):
        self.__Name = name
        self.__IDStudent = id
        self.__DoB = DoB

    def get_Namest(self):
        return self.__Name
    
    def get_IDStudent(self):
        return self.__IDStudent
    
    def get_DoB(self):
        return self.__DoB
    
    def __str__(self):
        return f"Name: {self.__Name}\nID of Student: {self.__IDStudent}\nDate of birth: {self.__DoB}"


# class for Course
class Course:
    def __init__(self,name,id):
        self.__Name = name
        self.__IDCourse = id

    def __str__(self):
        return f'Name: {self.__Name}\nID of course: {self.__IDCourse}'
    
    def get_NameCs(self):
        return self.__Name
    
    def get_IDCourse(self):
        return self.__IDCourse

# class for Mark
class Mark:
    def __init__(self,StudentIf,CourseIf,Mark):
        self.__StudentIf = StudentIf
        self.__CourseIf = CourseIf
        self.__Mark = Mark

    def __str__(self) -> str:
        return f'___Student__ \n{self.__StudentIf}\n___Mark of course__\n{self.__CourseIf} : {self.__Mark}'

# functions for importing data of Students
def InputStudent():
    n = int(input('Enter the number of Student: '))
    for id in range(n):
        print('Enter the data for Student - ',id+1)
        print('ID:',end=' ')
        ID = input()
        print('Name:',end=' ')
        name = input()
        print('Date of birth (format:Day/Mon/Year)',end=' ')
        Day,Mon,Year = map(int,input().split('/'))
        while(check_date(Day,Mon,Year)==False): # Check birthdate is valid
            print("The student's birthdate is invalid, please enter again! ")
            print('Date of birth (format:Day/Mon/Year)',end=' ')
            Day,Mon,Year = map(int,input().split('/'))
        birth_date = [Day,Mon,Year]
        Infor_St = Student(name,ID,birth_date)
        List_St.append(Infor_St)
        print()

# func for importing data of courses
def InputCourse():
    Num_course = int(input('Enter Number of Course:'))
    for id in range(Num_course):
        print('Enter the data for Course - ',id+1)
        print('ID:',end=' ')
        ID = input()
        print('Name:',end=' ')
        name = input()
        Infor_Cs = Course(name,ID)
        List_Cs.append(Infor_Cs)
        print()

# Import mark for Student
def Mark_infor():
    for St in List_St:
        print('Enter marks for Student with Id: ', St.get_IDStudent())
        for Cs in List_Cs:
            print('Marks in Course: ',Cs.get_NameCs())
            mark = int(input("Mark: "))
            Mark_in4 = Mark(St,Cs,mark)
            List_Mark.append(Mark_in4)
        print()

# main function 
if __name__ == '__main__':
    InputStudent()
    InputCourse()
    Mark_infor()