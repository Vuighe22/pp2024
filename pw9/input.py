import numpy as np
import math
from domais import *
import zipfile
import pickle
import tkinter as tk
from tkinter import messagebox
import os

global entry_num_students, entry_student_id, entry_student_name, entry_student_dob
menu = ['Input Data', 'Print Data','Compress the files','Extract students.dat', 'Exit']

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
    global List_St
    n = int(entry_num_students.get())
    for id in range(n):
        ID = entry_student_id.get()
        name = entry_student_name.get()
        Day, Mon, Year = map(int, entry_student_dob.get().split('/'))
        while (check_date(Day, Mon, Year) == False):  # Check birthdate is valid
            messagebox.showwarning("Invalid Date", "The student's birthdate is invalid, please enter again!")
            return
        birth_date = [Day, Mon, Year]
        Infor_St = Student(name, ID, birth_date)
        List_St.append(Infor_St)
    std_to_file()
    if os.path.exists(r'C:\Users\PC\Documents\Python_for_Son\pp2024\pw9\students.txt'):
        messagebox.showinfo("Success", "Student information added successfully!")
    else:
        messagebox.showerror("Success", "Student information added successfully!")
    


# func for importing data of courses
def InputCourse():
    global List_Cs
    Num_course = int(entry_num_courses.get())
    for id in range(Num_course):
        ID = entry_course_id.get()
        name = entry_course_name.get()
        credits = int(entry_course_credits.get())
        Infor_Cs = Course(name, ID, credits)
        List_Cs.append(Infor_Cs)
    cs_to_file()
    if os.path.exists(r'C:\Users\PC\Documents\Python_for_Son\pp2024\pw9\courses.txt'):
        messagebox.showinfo("Success", "Course information added successfully!")
    else:
        messagebox.showerror("Success", "Course information added successfully!")

# Import mark for Student
def Mark_infor():
    global List_Mark
    for St in List_St:
        for Cs in List_Cs:
            mark = float(entry_marks.get())
            mark = math.floor(mark * 10) / 10.0  # round-down to 1-digit decimal
            Mark_in4 = Mark(St, Cs, mark)
            List_Mark.append(Mark_in4)
    mk_to_file()
    if os.path.exists(r'C:\Users\PC\Documents\Python_for_Son\pp2024\pw9\marks.txt'):
        messagebox.showinfo("Success", "Marks information added successfully!")
    else:
        messagebox.showerror("Success", "Marks information added successfully!")

# write to students.txt
def std_to_file():
    with open(r'C:\Users\PC\Documents\Python_for_Son\pp2024\pw9\students.txt','wb') as std_file:
        pickle.dump(List_St,std_file)

# write to courses.txt
def cs_to_file():
    with open(r'C:\Users\PC\Documents\Python_for_Son\pp2024\pw9\courses.txt','wb') as cs_file:
        pickle.dump(List_Cs,cs_file)

# write to marks.txt
def mk_to_file():
    with open(r'C:\Users\PC\Documents\Python_for_Son\pp2024\pw9\marks.txt','wb') as mk_file:
        pickle.dump(List_Mark,mk_file)

# Compress the files
def compress_files():
    with zipfile.ZipFile(r'C:\Users\PC\Documents\Python_for_Son\pp2024\pw9\students.dat.zip', 'w') as file_zip:
        file_zip.write(r'C:\Users\PC\Documents\Python_for_Son\pp2024\pw9\students.txt', arcname='students.txt')
        file_zip.write(r'C:\Users\PC\Documents\Python_for_Son\pp2024\pw9\courses.txt', arcname='courses.txt')
        file_zip.write(r'C:\Users\PC\Documents\Python_for_Son\pp2024\pw9\marks.txt', arcname='marks.txt')
