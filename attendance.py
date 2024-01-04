import tkinter as tk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_attendance"
)

mycursor = mydb.cursor()


def collect_data():

    #student info
    Class_Name = class_name_spinbox.get()
    Student_ID = student_id_entry.get()
    Status = status_spinbox.get()

    #total 
    absent = int(absent_spinbox.get())
    total_student = int(total_student_spinbox.get())

    present = total_student - absent

    #insert data into database 
    sql = "INSERT INTO attendance (Class_Name, Student_ID, Status, Absent, Total_Student, Present) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (Class_Name, Student_ID, Status, absent, total_student, present)
    mycursor.execute(sql, val)
    mydb.commit()

    #output 
    output_label.config(text=f"Total student who is present is: {present}")
    
# Rest of your GUI code remains unchanged
window = tk.Tk()
window.title("Student Attendance")
window.geometry ('500x400')

frame = tk.Frame(window)
frame.pack()


#student info
student_info_frame=tk.LabelFrame(frame, text= "Student Info")
student_info_frame.grid(row= 0, column=0, padx=20, pady=10)

#first frame 
class_name_label = tk.Label(student_info_frame, text="Class Name")
class_name_spinbox = tk.Spinbox (student_info_frame, values=["", "Zuhal", "Marikh", "Musytari"])
class_name_label.grid(row=0, column=0)
class_name_spinbox.grid(row=1, column=0)

student_id_label = tk.Label(student_info_frame, text="Student ID")
student_id_label.grid(row=0, column=1)
student_id_entry = tk.Entry(student_info_frame)
student_id_entry.grid(row=1, column=1)

status_label = tk.Label(student_info_frame, text="Status")
status_spinbox = tk.Spinbox (student_info_frame, values=["", "Present", "Absent"])
status_label.grid(row=2, column=0)
status_spinbox.grid(row=3, column=0)

for widget in student_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#second frame
overall_attendance_frame =tk.LabelFrame(frame, text="Overall Attendance")
overall_attendance_frame.grid(row= 1, column=0, padx=20, pady=10)

absent_label = tk.Label(overall_attendance_frame, text="Absent")
absent_spinbox = tk.Spinbox(overall_attendance_frame, from_=0, to=100)
absent_label.grid(row=0, column=0)
absent_spinbox.grid(row=1, column=0)

total_student_label = tk.Label(overall_attendance_frame, text="Total Student")
total_student_spinbox = tk.Spinbox(overall_attendance_frame, from_=0, to=100)
total_student_label.grid(row=0, column=2)
total_student_spinbox.grid(row=1, column=2)

# Button
button = tk.Button(frame, text="Enter data", command= collect_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)


# Output Label & result
label = tk.Label(window, text='Total Student who is present', font=("Times New Romans",12))
label.pack(ipadx=10, ipady=10)
output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()