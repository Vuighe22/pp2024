from input import *
from output import *
import domais
import sys

# The menu option
def menu_option(selected_opt):
    if selected_opt == 0:
        First = tk.Toplevel()
        First.title('Input number of Students')
        First.geometry('300x200')

        global entry_num_students
        label_num_students = tk.Label(First, text="Enter the number of Students:")
        label_num_students.pack()
        entry_num_students = tk.Entry(First)
        entry_num_students.pack()
        First_Button = tk.Button(First, text='Submit', command=lambda: submit_and_destroy(First))
        First_Button.pack()
    elif selected_opt == 1:
        Show_Inf_St()
        Show_Inf_Cs()
        Show_Mark()
    elif selected_opt == 2:
        compress_files()
        messagebox.showinfo("Success", "The files are compressed successfully!")
    elif selected_opt == 3:
        decompress_files()
        messagebox.showinfo("Success", "The files are decompressed successfully!")
    elif selected_opt == 4:
        main.destroy()

# Submit function for First window
def submit_first():
    num_students = int(entry_num_students.get())
    for i in range(num_students):
        Second = tk.Toplevel()
        Second.title(f'Input the data of Students-{i+1}th')
        Second.geometry('400x300')
        label_student_id = tk.Label(Second, text="Student ID:")
        label_student_id.pack()
        entry_student_id = tk.Entry(Second)
        entry_student_id.pack()

        label_student_name = tk.Label(Second, text="Student Name:")
        label_student_name.pack()
        entry_student_name = tk.Entry(Second)
        entry_student_name.pack()

        label_student_dob = tk.Label(Second, text="Date of Birth (format: Day/Mon/Year):")
        label_student_dob.pack()
        entry_student_dob = tk.Entry(Second)
        entry_student_dob.pack()

        var = tk.IntVar()
        Second_submit = tk.Button(Second, text="Submit", command=lambda: button_clicked(var,Second))
        Second_submit.pack()
        Second_submit.wait_variable(var)

def submit_and_destroy(window):
    submit_first()
    window.destroy()
def button_clicked(var,win):
    var.set(1)
    win.destroy()

# Main GUI window
main = tk.Tk()
main.title('Student Management system')
main.geometry('600x400')

# Create the menu
menu_frame = tk.Frame(main)
menu_frame.pack()

for idx, opt in enumerate(menu):
    tk.Button(menu_frame, text=opt, command=lambda idx=idx: menu_option(idx)).pack()

main.mainloop()
