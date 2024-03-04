import numpy as np
import math
from domais import *

menu = ['Input Data','Print Data','Exit']

# define a list to store inform of Student
List_St = []
List_Cs = []
List_Mark = []
# define numpy array and it's dtype
dtype = [('NameSt', 'U50'), ('IdSt', 'U10'), ('DoB', 'U10'), ('GPA', 'f2')]
Gpa = np.array([])

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


# functions for importing data of Students
def InputStudent():
    n = int(input('Enter the number of Student: '))
    for id in range(n):
        print('Enter the data for Student - ', id + 1)
        print('ID of Student:', end=' ')
        ID = input()
        print('Full name:', end=' ')
        name = input()
        print('Date of birth (format:Day/Mon/Year)', end=' ')
        Day, Mon, Year = map(int, input().split('/'))
        while (check_date(Day, Mon, Year) == False):  # Check birthdate is valid
            print("The student's birthdate is invalid, please enter again! ")
            print('Date of birth (format:Day/Mon/Year)', end=' ')
            Day, Mon, Year = map(int, input().split('/'))
        birth_date = [Day, Mon, Year]
        Infor_St = Student(name, ID, birth_date)
        List_St.append(Infor_St)
        print()


# func for importing data of courses
def InputCourse():
    Num_course = int(input('Enter Number of Course: '))
    for id in range(Num_course):
        print('Enter the data for Course - ', id + 1)
        print('ID of course:', end=' ')
        ID = input()
        print('Name of course:', end=' ')
        name = input()
        print('The number of Credits:', end = ' ')
        credits = int(input())
        Infor_Cs = Course(name, ID, credits)
        List_Cs.append(Infor_Cs)
        print()

# Import mark for Student
def Mark_infor():
    for St in List_St:
        print('Enter marks for Student with Id: ', St.get_IDStudent())
        for Cs in List_Cs:
            print('Marks in Course: ', Cs.get_NameCs())
            mark = float(input("Mark: "))
            mark = math.floor(mark*10)/10.0 #round-down to 1-digit decimal 
            Mark_in4 = Mark(St, Cs, mark)
            List_Mark.append(Mark_in4)
        print()

# function to calculate GPA
def cal_GPA():
    student_info = []
    for student in List_St:
        final_GPA = 0
        weighted_sum = 0
        total_credit = 0
        for mark in List_Mark:
            if student == mark.get_StudentIf():
                weighted_sum += mark.get_Marks() * mark.get_Course().get_Credit()
                total_credit += mark.get_Course().get_Credit()
        if total_credit != 0:
            final_GPA = weighted_sum / total_credit
        student.set_GPA(final_GPA)
        student_info.append((student.get_Namest(), student.get_IDStudent(), student.get_formattedDoB(), final_GPA))

    global Gpa
    Gpa = np.array(student_info, dtype=dtype)
    Gpa = np.sort(Gpa,order='GPA')[::-1]

