# main.py
import curses
from input import *
from output import *
import domais
import sys

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
                std_to_file()
                cs_to_file()
                mk_to_file()
                compress_files()
            if menu[current_opt] == 'Print Data':
                curses.endwin()
                Show_Inf_St()
                Show_Inf_Cs()
                Show_Mark()
                input('Press ENTER key to continue')
            if menu[current_opt] == 'Extract students.dat':
                curses.endwin()
                decompress_files()
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
    while True:
     curses.wrapper(main)