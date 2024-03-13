from input import *
from domais import *
import curses
import numpy as np
import os


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


# Print information of Student
def Show_Inf_St():
    print('------------- Inform of Students ----------------')
    if len(Gpa) == 0:
        print("No student information available.")
    else:
        stt = 1
        for i in Gpa:
            print(f"{stt} Name of Student: {i['NameSt']} - ID: {i['IdSt']} - GPA: {i['GPA']}")
            stt += 1


# Print information of Course
def Show_Inf_Cs():
    print('------------- Inform of Courses ----------------')
    with open(r'C:\Users\PC\Documents\Python_for_Son\pp2024\pw8\students_dat\courses.txt','rb') as cs_file:
        List_Cs = pickle.load(cs_file)
        for cs in List_Cs:
            print(cs)


# Display Marks of Student
def Show_Mark():
    print('--------------- Mark Table ----------------')
    header = ['Student ID', 'Student Name']
    with open(r'C:\Users\PC\Documents\Python_for_Son\pp2024\pw8\students_dat\courses.txt','rb') as cs_file:
        List_Cs = pickle.load(cs_file)
        for Cs in List_Cs:
            header += [Cs.get_NameCs()]
        print('\t'.join(header))
        with open(r'C:\Users\PC\Documents\Python_for_Son\pp2024\pw8\students_dat\students.txt','rb') as st_file:
            List_St = pickle.load(st_file)
            for St in List_St:
                row = [St.get_IDStudent(),' '*(len(header[0])-len(St.get_IDStudent())+6), St.get_Namest(),' '*(len(header[1])-len(St.get_Namest())+4)]
                with open(r'C:\Users\PC\Documents\Python_for_Son\pp2024\pw8\students_dat\marks.txt','rb') as mk_file:
                    List_Mark = pickle.load(mk_file) 
                    for mark in List_Mark:
                        current_header = 2
                        if mark.get_StudentIf() == St:
                            row.append(str(mark.get_Marks()))
                            row.append(' '*(len(header[current_header])-len(str(mark.get_Marks()))+4))
                        current_header += 1
                    print(''.join(row))

# Display the menu
def print_menu(stdscr,selected_opt):
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_WHITE)
    h,w = stdscr.getmaxyx()
    # stdscr.clear()
    for idx,opt in enumerate(menu):
        x = w//2 - len(opt)//2
        y = h//2 - len(menu)//2 + idx
        stdscr.addstr(y,x,opt)
        if idx == selected_opt:
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(y,x,opt)
            stdscr.attroff(curses.color_pair(2))
        else:
            stdscr.addstr(y,x,opt)
    stdscr.refresh()

# Decompress students.dat.zip
def decompress_files():
    if os.path.exists(r'C:\Users\PC\Documents\Python_for_Son\pp2024\pw8\students.dat.zip'):
        directory = r'C:\Users\PC\Documents\Python_for_Son\pp2024\pw8\students_dat'
        if not os.path.exists(directory):
            os.makedirs(directory)
        with zipfile.ZipFile(r'C:\Users\PC\Documents\Python_for_Son\pp2024\pw8\students.dat.zip', 'r') as zip_object:
            zip_object.extractall(directory)
        
        print(f'Files are extracted to {directory}')
    else:
        print('No students.dat.zip found')