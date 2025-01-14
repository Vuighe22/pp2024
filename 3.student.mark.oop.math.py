import numpy as np
import math
import curses
import sys

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


# class for Students
class Student:
    def __init__(self, name, id, DoB):
        self.__Name = name
        self.__IDStudent = id
        self.__DoB = DoB
        self.__GPA = 0

    def get_Namest(self):
        return self.__Name

    def get_IDStudent(self):
        return self.__IDStudent

    def get_formattedDoB(self):
        return f"{self.__DoB[0]}/{self.__DoB[1]}/{self.__DoB[2]}"
    
    def set_GPA(self,gpa):
        self.__GPA = gpa

    def __str__(self):
        return f"_ Full name: {self.__Name}\n_ ID of Student: {self.__IDStudent}\n_ Date of birth: {self.get_formattedDoB()}\n_ GPA: {self.__GPA}"


# class for Course
class Course:
    def __init__(self, name, id, credits):
        self.__Name = name
        self.__IDCourse = id
        self.__Credit = credits

    def __str__(self):
        return f'_ Name course: {self.__Name}\n_ ID of course: {self.__IDCourse}\n_ Credit: {self.__Credit}'

    def get_NameCs(self):
        return self.__Name

    def get_IDCourse(self):
        return self.__IDCourse
    
    def get_Credit(self):
        return self.__Credit


# class for Mark
class Mark:
    def __init__(self, StudentIf, CourseIf, Mark):
        self.__StudentIf = StudentIf
        self.__CourseIf = CourseIf
        self.__Mark = Mark

    def get_Marks(self):
        return self.__Mark

    def get_StudentIf(self):
        return self.__StudentIf
    
    def get_Course(self):
        return self.__CourseIf

    def __str__(self) -> str:
        return f'___Student__ \n{self.__StudentIf}\n___Mark of course__\n{self.__CourseIf} : {self.__Mark}'


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


# Print information of Student
def Show_Inf_St():
    print('------------- Inform of Students ----------------')
    stt = 1
    for i in Gpa:
        print(stt,'Name of Student:',end=' ')
        print(i['NameSt'],end='- ID: ')
        print(i['IdSt'],end=' - GPA: ')
        print(i['GPA'])
        stt+=1


# Print information of Course
def Show_Inf_Cs():
    print('------------- Inform of Courses ----------------')
    for Cs in List_Cs:
        print(Cs)
        print()


# Display Marks of Student
def Show_Mark():
    print('--------------- Mark Table ----------------')
    header = ['Student ID', 'Student Name']
    for Cs in List_Cs:
        header += [Cs.get_NameCs()]
    print('\t'.join(header))
    for St in List_St:
        row = [St.get_IDStudent(), St.get_Namest()]
        for mark in List_Mark:
            if mark.get_StudentIf() == St:
                row += [str(mark.get_Marks())]
        print('\t'.join(row))

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

# Decorate the UI
def main(stdscr):
    curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_WHITE)
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    BLUE_AND_YELLOW = curses.color_pair(3)
    GREEN_AND_WHITE = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)

    stdscr.clear()
    stdscr.attron(GREEN_AND_WHITE)
    stdscr.border()
    stdscr.attroff(GREEN_AND_WHITE)

    
    stdscr.nodelay(True)

    current_opt = 0
    while True:
        try: 
            key = stdscr.getkey()
        except:
            key = None
        # stdscr.clear()
        h,w = stdscr.getmaxyx()
        Title = 'User Interface'
        x = w//2 - len(Title)//2 #Printing text in center of screen
        y = h//2 - len(menu)//2 -3
        stdscr.addstr(y,x,Title,BLUE_AND_YELLOW | curses.A_UNDERLINE)
        stdscr.addstr(y+1,x-6,'(PRESS RIGHT KEY TO ENTER)')
        stdscr.refresh()
        
        print_menu(stdscr,current_opt)
        
        if key == 'KEY_UP' and current_opt > 0:
            current_opt -= 1
        if key == 'KEY_DOWN' and current_opt < len(menu) -1:
            current_opt += 1
        if key == 'KEY_RIGHT':
            # stdscr.clear()
            if current_opt == len(menu) -1:
                sys.exit() # out of the program
            if menu[current_opt] == 'Input Data':
                curses.endwin()
                InputStudent()
                InputCourse()
                Mark_infor()
                cal_GPA()
            if menu[current_opt] == 'Print Data':
                curses.endwin()
                Show_Inf_St()
                Show_Inf_Cs()
                Show_Mark()
                input('Press ENTER key to continue')
            stdscr.refresh()
            stdscr.getch()          
        print_menu(stdscr,current_opt)
        stdscr.refresh()

    curses.curs_set(1)
    curses.echo()

    stdscr.getch()
    curses.endwin()



# main function
if __name__ == '__main__':
    # InputStudent()
    # InputCourse()
    # Mark_infor()
    # cal_GPA()
    # Show_Inf_St()
    # Show_Inf_Cs()
    # Show_Mark()
    while True:
     curses.wrapper(main)

