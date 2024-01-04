from math import *
# define a list to store inform of Student
List_St = []
# Funs for number of Student
def NumberofStudent():
    n = int(input())
    return n

# functions for import data of Stu
def InputStudent(n):
    for id in range(n):
        print('Enter the data for Student with ID ',id+1000)
        print('ID',end=' ')
        ID = input()
        print('Name:',end=' ')
        name = input()
        print('Date of birth',end=' ')
        DoB = input()
        Infor_St = {
            'Id' : id,
            'Name' : name,
            'Date of birth' : DoB
        }
        List_St.append(Infor_St)

# Print infor of Student
def Show_Inf_St():
    for St in List_St:
        for key,val in St.items():
            print(key,':',val)
        print()

#main 
if __name__ == '__main__':
    number_St = NumberofStudent()
    InputStudent(number_St)
    Show_Inf_St()
