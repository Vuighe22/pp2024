from math import *
# define a list to store inform of Student
List_St = []
List_Cs = []
List_Mark = []

# Check Date valid or invalid
def check_date(date, month, year):
    a = False
    if month == 2:  # Thang 2
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

# Funs for number of Student
def NumberofStudent():
    print('Enter the number of Student: ',end=' ')
    n = int(input())
    return n

# functions for import data of Students
def InputStudent(n):
    for id in range(n):
        print('Enter the data for Student - ',id+1)
        print('ID:',end=' ')
        ID = input()
        print('Name:',end=' ')
        name = input()
        print('Date of birth (format:Day/Mon/Year)',end=' ')
        Day,Mon,Year = map(int,input().split('/'))
        while(check_date(Day,Mon,Year)==False): # Check birthdate is valid
            print("The student's bithdate is invalid, please enter again! ")
            print('Date of birth (format:Day/Mon/Year)',end=' ')
            Day,Mon,Year = map(int,input().split('/'))
        birth_date = [Day,Mon,Year]
        Infor_St = {
            'Id' : ID,
            'Name' : name,
            'Date of birth' : birth_date
        }
        List_St.append(Infor_St)
        print()

# func for import courses
def InputCourse():
    print('Enter Number of Course:',end=' ')
    Num_course = int(input())
    for id in range(Num_course):
        print('Enter the data for Course - ',id+1)
        print('ID:',end=' ')
        ID = input()
        print('Name:',end=' ')
        name = input()
        Infor_Cs = {
            'Id Course' : ID,
            'Name of course' : name,
        }
        List_Cs.append(Infor_Cs)
        print()

# Print infor of Student
def Show_Inf_St():
    print('------------- Inform of Students ----------------')
    for St in List_St:
        for key,val in St.items():
            if key == 'Date of birth':
                day,month,year = val
                print(key,end=': ')
                print(day,month,year,sep='/')
            else:
                print(key,':',val)
    print()

# Print infor of Course
def Show_Inf_Cs():
    print('------------- Inform of Courses ----------------')
    for Cs in List_Cs:
        for key,val in Cs.items():
            print(key,':',val)
    print()

# Import mark for Student
def Mark_infor():
    for St in List_St:
        print('Enter matks for Student with Id: ', St['Id'])
        for Cs in List_Cs:
            print('For ',Cs['Name of course'])
            print('Mark: ',end=' ')
            mark = int(input())
            marks = {
                'Course' : Cs['Name of course'],
                'ID Student' : St['Id'],
                'Name student' : St['Name'],
                'Mark' : mark
            }
            List_Mark.append(marks)
        print()

# Show student marks for a given course
def Table_Grade():
    print('------------- Study result ----------------')
    print('Id Student | Name Student | ', end='')
    for Cs in List_Cs:
        print(Cs['Name of course'] , end=' | ')
    print()

    # Print data
    for St in List_St:
        print(St['Id'], St['Name'],sep=' | ', end=' | ')
        for Cs in List_Cs:
            # print marks of Student corressponding to given Courses if no found. return N/A
            mark_data = next((mark['Mark'] for mark in List_Mark if mark['ID Student'] == St['Id'] and mark['Course'] == Cs['Name of course']),'N/A')
            print(mark_data, ' | ', end='')
        print()

#main 
if __name__ == '__main__':
    number_St = NumberofStudent()
    InputStudent(number_St)
    InputCourse()
    Show_Inf_St()
    Show_Inf_Cs()
    Mark_infor()
    Table_Grade()
