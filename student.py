# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk  # pip install pillow
# from tkinter import messagebox
# import mysql.connector
# import cv2  # pip install opencv-python
# import face_recognition
# import numpy as np


# class Student:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")

#         self.var_dep = StringVar()
#         self.var_course = StringVar()
#         self.var_year = StringVar()
#         self.var_semester = StringVar()
#         self.var_std_id = StringVar()
#         self.var_std_name = StringVar()
#         self.var_div = StringVar()
#         self.var_roll = StringVar()
#         self.var_gender = StringVar()
#         self.var_dob = StringVar()
#         self.var_email = StringVar()
#         self.var_phone = StringVar()
#         self.var_address = StringVar()
#         self.var_teacher = StringVar()

#         # First image
#         img = Image.open(r"images/left.jpg")
#         img = img.resize((520, 130), Image.LANCZOS)
#         self.photoimg = ImageTk.PhotoImage(img)

#         f_lbl = Label(self.root, image=self.photoimg)
#         f_lbl.place(x=0, y=0, width=520, height=130)

#         # Second image
#         img1 = Image.open(r"images/center.jpg")
#         img1 = img1.resize((520, 130), Image.LANCZOS)
#         self.photoimg1 = ImageTk.PhotoImage(img1)

#         f_lbl = Label(self.root, image=self.photoimg1)
#         f_lbl.place(x=500, y=0, width=520, height=130)

#         # Third image
#         img2 = Image.open(r"images/right.jpg")
#         img2 = img2.resize((530, 130), Image.LANCZOS)
#         self.photoimg2 = ImageTk.PhotoImage(img2)

#         f_lbl = Label(self.root, image=self.photoimg2)
#         f_lbl.place(x=1000, y=0, width=530, height=130)

#         # Background image
#         img3 = Image.open(r"images/fill.jpg")
#         img3 = img3.resize((1530, 710), Image.LANCZOS)
#         self.photoimg3 = ImageTk.PhotoImage(img3)

#         bg_img = Label(self.root, image=self.photoimg3)
#         bg_img.place(x=0, y=130, width=1530, height=710)

#         # Title
#         title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=(
#             "times new roman", 30, "bold"), bg="darkblue", fg="red")
#         title_lbl.place(x=0, y=0, width=1530, height=45)

#         # frame
#         main_frame = Frame(bg_img, bd=2, bg="white")
#         main_frame.place(x=15, y=55, width=1490, height=590)

#         # left frame
#         Left_frame = LabelFrame(main_frame, bd=2, bg="white", text="Student detail", font=(
#             "times new roman", 11, "bold"))
#         Left_frame.place(x=15, y=8, width=745, height=570)

#         img0 = Image.open(r"images/write.jpg")
#         img0 = img0.resize((710, 130), Image.LANCZOS)
#         self.photoimg0 = ImageTk.PhotoImage(img0)

#         f_lbl = Label(Left_frame, image=self.photoimg0)
#         f_lbl.place(x=0, y=0, width=740, height=130)

#         # current course
#         current_course_frame = LabelFrame(
#             Left_frame, bd=2, bg="white", relief=RIDGE, text="Current course", font=("times new roman", 11, "bold"))
#         current_course_frame.place(x=15, y=120, width=715, height=103)

#         # current course info

#         # department
#         dep_label = Label(current_course_frame, text="Department :", font=(
#             "times new roman", 11, "bold"), bg="white")
#         dep_label.grid(row=0, column=0, padx=10, pady=8, sticky=W)

#         dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
#             "times new roman", 11, "bold"), state="readonly")
#         dep_combo["values"] = ("Select department", "computer", "it", "civil")
#         dep_combo.current(0)
#         dep_combo.grid(row=0, column=1, padx=10, pady=8, sticky=W)

#         # course
#         dep_label = Label(current_course_frame, text="Course :",
#                           font=("times new roman", 11, "bold"))
#         dep_label.grid(row=0, column=2)

#         course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
#             "times new roman", 11, "bold"), state="readonly")
#         course_combo["values"] = ("Select course", "fe", "se", "te")
#         course_combo.current(0)
#         course_combo.grid(row=0, column=3, padx=19, pady=8, sticky=W)

#         # year
#         dep_label = Label(current_course_frame, text="year :",
#                           font=("times new roman", 11, "bold"))
#         dep_label.grid(row=1, column=0)

#         year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
#             "times new roman", 11, "bold"), state="readonly")
#         year_combo["values"] = ("Select year", "2021", "2022", "2023")
#         year_combo.current(0)
#         year_combo.grid(row=1, column=1, padx=19, pady=8, sticky=W)

#         # semester
#         dep_label = Label(current_course_frame, text="sem :",
#                           font=("times new roman", 11, "bold"))
#         dep_label.grid(row=1, column=2)

#         sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=(
#             "times new roman", 11, "bold"), state="readonly")
#         sem_combo["values"] = ("Select sem", "1", "2")
#         sem_combo.current(0)
#         sem_combo.grid(row=1, column=3, padx=19, pady=8, sticky=W)

#         # class student information frame
#         class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
#                                          text="Class student information", font=("times new roman", 11, "bold"))
#         class_student_frame.place(x=15, y=225, width=715, height=322)

#         # class student information

#         # student id
#         studentId_label = Label(class_student_frame, text="Student ID :", font=(
#             "times new roman", 11, "bold"))
#         studentId_label.grid(row=0, column=0, padx=10, pady=3, sticky=W)

#         studentId_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=(
#             "times new roman", 11, "bold"))
#         studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

#         # student name
#         studentName_label = Label(class_student_frame, text="Student Name :", font=(
#             "times new roman", 11, "bold"))
#         studentName_label.grid(row=0, column=2, padx=10, pady=8, sticky=W)

#         studentName_entry = ttk.Entry(
#             class_student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 11, "bold"))
#         studentName_entry.grid(row=0, column=3, padx=10, pady=8, sticky=W)

#         # class division
#         class_div_label = Label(class_student_frame, text="Class Division :", font=(
#             "times new roman", 11, "bold"))
#         class_div_label.grid(row=1, column=0, padx=10, pady=3, sticky=W)

#         div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, width=18, font=(
#             "times new roman", 11, "bold"), state="readonly")
#         div_combo["values"] = ("A", "B", "C")
#         div_combo.current(0)
#         div_combo.grid(row=1, column=1, padx=10, pady=8, sticky=W)

#         # roll no
#         roll_no_label = Label(class_student_frame, text="Roll no :", font=(
#             "times new roman", 11, "bold"))
#         roll_no_label.grid(row=1, column=2, padx=10, pady=8, sticky=W)

#         roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=(
#             "times new roman", 11, "bold"))
#         roll_no_entry.grid(row=1, column=3, padx=10, pady=8, sticky=W)

#         # gender
#         gender_label = Label(class_student_frame, text="Gender :", font=(
#             "times new roman", 11, "bold"))
#         gender_label.grid(row=2, column=0, padx=10, pady=8, sticky=W)

#         gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, width=18, font=(
#             "times new roman", 11, "bold"), state="readonly")
#         gender_combo["values"] = ("Male", "Female", "Other")
#         gender_combo.current(0)
#         gender_combo.grid(row=2, column=1, padx=10, pady=8, sticky=W)

#         # dob
#         dob_label = Label(class_student_frame, text="DOB :",
#                           font=("times new roman", 11, "bold"))
#         dob_label.grid(row=2, column=2, padx=10, pady=8, sticky=W)

#         dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=(
#             "times new roman", 11, "bold"))
#         dob_entry.grid(row=2, column=3, padx=10, pady=8, sticky=W)

#         # email
#         email_label = Label(class_student_frame, text="Email :",
#                             font=("times new roman", 11, "bold"))
#         email_label.grid(row=3, column=0, padx=10, pady=8, sticky=W)

#         email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=(
#             "times new roman", 11, "bold"))
#         email_entry.grid(row=3, column=1, padx=10, pady=8, sticky=W)

#         # phone no
#         phone_label = Label(class_student_frame, text="Phone no :",
#                             font=("times new roman", 11, "bold"))
#         phone_label.grid(row=3, column=2, padx=10, pady=8, sticky=W)

#         phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=(
#             "times new roman", 11, "bold"))
#         phone_entry.grid(row=3, column=3, padx=10, pady=8, sticky=W)

#         # address
#         address_label = Label(class_student_frame, text="Address :", font=(
#             "times new roman", 11, "bold"))
#         address_label.grid(row=4, column=0, padx=10, pady=8, sticky=W)

#         address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=(
#             "times new roman", 11, "bold"))
#         address_entry.grid(row=4, column=1, padx=10, pady=8, sticky=W)

#         # teacher name
#         teacher_label = Label(class_student_frame, text="Teacher name :", font=(
#             "times new roman", 11, "bold"))
#         teacher_label.grid(row=4, column=2, padx=10, pady=8, sticky=W)

#         teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=(
#             "times new roman", 11, "bold"))
#         teacher_entry.grid(row=4, column=3, padx=10, pady=8, sticky=W)

#         # radio buttons
#         self.var_radio1 = StringVar()
#         radiobtn1 = ttk.Radiobutton(
#             class_student_frame, variable=self.var_radio1, text="Take photo sample", value="Yes")
#         radiobtn1.grid(row=6, column=0)

#         radiobtn2 = ttk.Radiobutton(
#             class_student_frame, variable=self.var_radio1, text="No photo sample", value="No")
#         radiobtn2.grid(row=6, column=1)

#         # button frame
#         btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
#         btn_frame.place(x=0, y=225, width=710, height=38)

#         save_btn = Button(btn_frame, command=self.add_data, text="Save", width=19, font=(
#             "times new roman", 12, "bold"), bg="blue", fg="white")
#         save_btn.grid(row=0, column=0)

#         update_btn = Button(btn_frame, command=self.update_data, text="Update", width=19, font=(
#             "times new roman", 12, "bold"), bg="blue", fg="white")
#         update_btn.grid(row=0, column=1)

#         delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=19, font=(
#             "times new roman", 12, "bold"), bg="blue", fg="white")
#         delete_btn.grid(row=0, column=2)

#         reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=19, font=(
#             "times new roman", 12, "bold"), bg="blue", fg="white")
#         reset_btn.grid(row=0, column=3)

#         btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
#         btn_frame1.place(x=0, y=260, width=715, height=45)

#         take_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Take photo sample", width=40, font=(
#             "times new roman", 12, "bold"), bg="blue", fg="white")
#         take_photo_btn.grid(row=0, column=0)

#         update_photo_btn = Button(btn_frame1, text="Update photo sample", width=40, font=(
#             "times new roman", 12, "bold"), bg="blue", fg="white")
#         update_photo_btn.grid(row=0, column=1)

#         # right frame
#         Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
#                                  text="Student details", font=("times new roman", 11, "bold"))
#         Right_frame.place(x=765, y=7, width=710, height=570)

#         img99 = Image.open(r"images/spray.jpg")
#         img99 = img99.resize((690, 130), Image.LANCZOS)
#         self.photoimg99 = ImageTk.PhotoImage(img99)

#         f_lbl = Label(Right_frame, image=self.photoimg99)
#         f_lbl.place(x=10, y=0, width=690, height=130)

#         # ssearch system
#         search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,
#                                   text="Search system", font=("times new roman", 11, "bold"))
#         search_frame.place(x=7, y=120, width=693, height=70)

#         search_label = Label(search_frame, text="Search by :",
#                              font=("times new roman", 12, "bold"))
#         search_label.grid(row=0, column=0, padx=0, pady=5)
#         search_label.place(x=5,y=5)

#         search_combo = ttk.Combobox(search_frame, font=(
#             "times new roman", 13, "bold"), state="readonly",width=15)
#         search_combo["values"] = ("Select", "Roll no", "Phone no")
#         search_combo.current(0)
#         search_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)
#         search_combo.place(x=95,y=5,width=130)
        
#         search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",11,"bold"))
#         search_entry.grid(row=0,column=4,padx=10,pady=5,sticky=W)
#         search_entry.place(x=230,y=5,width=150,height=25)

#         search_btn = Button(search_frame, text="Search", width=8, font=(
#             "times new roman", 15, "bold"), bg="blue", fg="white")
#         search_btn.grid(row=0, column=3, padx=10)
#         search_btn.place(x=390,y=0,width=140,height=35)

#         showAll_btn = Button(search_frame, text="Show All", width=8, font=(
#             "times new roman", 15, "bold"), bg="blue", fg="white")
#         showAll_btn.grid(row=0, column=4, padx=10)
#         showAll_btn.place(x=540,y=0,width=140,height=35)

#         # =========================table frame=============================
#         table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
#         table_frame.place(x=6, y=195, width=695, height=345)

#         # ============Scroll Bar==============#
#         scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
#         scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

#         self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender",
#                                           "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

#         scroll_x.pack(side=BOTTOM, fill=X)
#         scroll_y.pack(side=RIGHT, fill=Y)
#         scroll_x.config(command=self.student_table.xview)
#         scroll_y.config(command=self.student_table.yview)

#         self.student_table.heading("dep", text="Department")
#         self.student_table.heading("course", text="Course")
#         self.student_table.heading("year", text="Year")
#         self.student_table.heading("sem", text="Semester")
#         self.student_table.heading("id", text="ID")
#         self.student_table.heading("name", text="Name")
#         self.student_table.heading("div", text="Division")
#         self.student_table.heading("roll", text="Roll No")
#         self.student_table.heading("gender", text="Gender")
#         self.student_table.heading("dob", text="D.O.B")
#         self.student_table.heading("email", text="Email")
#         self.student_table.heading("phone", text="Phone")
#         self.student_table.heading("address", text="Address")
#         self.student_table.heading("teacher", text="Teacher")
#         self.student_table.heading("photo", text="Photo")
#         self.student_table["show"] = "headings"

#         self.student_table.column("dep", width=100)
#         self.student_table.column("course", width=100)
#         self.student_table.column("year", width=100)
#         self.student_table.column("sem", width=100)
#         self.student_table.column("id", width=100)
#         self.student_table.column("name", width=100)
#         self.student_table.column("div", width=100)
#         self.student_table.column("roll", width=100)
#         self.student_table.column("gender", width=100)
#         self.student_table.column("dob", width=100)
#         self.student_table.column("email", width=100)
#         self.student_table.column("phone", width=100)
#         self.student_table.column("address", width=100)
#         self.student_table.column("teacher", width=100)
#         self.student_table.column("photo", width=150)

#         self.student_table.pack(fill=BOTH, expand=1)

#         self.student_table.bind("<ButtonRelease>", self.get_cursor)

#         self.fetch_data()

#         # ================== Function decration ================

#     def add_data(self):

#         if self.var_dep.get() == "Select department" or self.var_course.get() == "Select course" or self.var_year.get() == "Select year" or self.var_semester.get() == "Select sem" or self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_div.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "" or self.var_radio1.get() == "":

#             messagebox.showerror(
#                 "Error", "All fields are required", parent=self.root)

#         else:

#             try:
#                 conn = mysql.connector.connect(
#                     host="localhost", username="root", password="#include stdio.h687", database="maazdb")
#                 my_cursor = conn.cursor()
#                 my_cursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
#                     self.var_dep.get(),
#                     self.var_course.get(),
#                     self.var_year.get(),
#                     self.var_semester.get(),
#                     self.var_std_id.get(),
#                     self.var_std_name.get(),
#                     self.var_div.get(),
#                     self.var_roll.get(),
#                     self.var_gender.get(),
#                     self.var_dob.get(),
#                     self.var_email.get(),
#                     self.var_phone.get(),
#                     self.var_address.get(),
#                     self.var_teacher.get(),
#                     self.var_radio1.get()


#                 ))
#                 conn.commit()
#                 self.fetch_data()
#                 conn.close()
#                 messagebox.showinfo(
#                     "Success", "Student details has been added successfully", parent=self.root)

#             except Exception as es:
#                 messagebox.showerror(
#                     "Error", f"Due to : {str(es)}", parent=self.root)

#     def fetch_data(self):
#         conn = mysql.connector.connect(
#             host="localhost", username="root", password="#include stdio.h687", database="maazdb")
#         my_cursor = conn.cursor()
#         my_cursor.execute("Select * from students")
#         data = my_cursor.fetchall()

#         if len(data) != 0:
#             self.student_table.delete(* self.student_table.get_children())
#             for i in data:
#                 self.student_table.insert("", END, values=i)
#             conn.commit()

#         conn.close()

#         # ============== get cursor ==================
#     def get_cursor(self, event=""):
#         cursor_focus = self.student_table.focus()
#         content = self.student_table.item(cursor_focus)
#         data = content["values"]

#         self.var_dep.set(data[0]),
#         self.var_course.set(data[1]),
#         self.var_year.set(data[2]),
#         self.var_semester.set(data[3]),
#         self.var_std_id.set(data[4]),
#         self.var_std_name.set(data[5]),
#         self.var_div.set(data[6]),
#         self.var_roll.set(data[7]),
#         self.var_gender.set(data[8]),
#         self.var_dob.set(data[9]),
#         self.var_email.set(data[10]),
#         self.var_phone.set(data[11]),
#         self.var_address.set(data[12]),
#         self.var_teacher.set(data[13]),
#         self.var_radio1.set(data[14])

#    # ======================== update function ==========================
#     def update_data(self):

#         if self.var_dep.get() == "Select department" or self.var_course.get() == "Select course" or self.var_year.get() == "Select year" or self.var_semester.get() == "Select sem" or self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_div.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "" or self.var_radio1.get() == "":

#             messagebox.showerror(
#                 "Error", "All fields are required", parent=self.root)

#         else:
#             try:
#                 Update = messagebox.askyesno(
#                     "Update", "Do you want to update this student details", parent=self.root)
#                 if Update > 0:
#                     conn = mysql.connector.connect(
#                         host="localhost", username="root", password="#include stdio.h687", database="maazdb")
#                     my_cursor = conn.cursor()
#                     my_cursor.execute("update students set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s", (
#                         self.var_dep.get(),
#                         self.var_course.get(),
#                         self.var_year.get(),
#                         self.var_semester.get(),
#                         self.var_std_name.get(),
#                         self.var_div.get(),
#                         self.var_roll.get(),
#                         self.var_gender.get(),
#                         self.var_dob.get(),
#                         self.var_email.get(),
#                         self.var_phone.get(),
#                         self.var_address.get(),
#                         self.var_teacher.get(),
#                         self.var_radio1.get(),
#                         self.var_std_id.get()


#                     ))
#                 else:
#                     if not Update:
#                         return

#                 messagebox.showinfo(
#                     "Success", "Student deatail updated successfully", parent=self.root)
#                 conn.commit()
#                 self.fetch_data()
#                 conn.close()

#             except Exception as es:
#                 messagebox.showerror(
#                     "Error", f"Due to {str(es)}", parent=self.root)

#    # ========================= delete data =============================
#     def delete_data(self):

#         if self.var_std_id.get() == "":
#             messagebox.showerror(
#                 "Error", "Student id must be required ", parent=self.root)

#         else:
#             try:
#                 delete = messagebox.askyesno(
#                     "Student Delete page", "Do you want to delete this student detail", parent=self.root)
#                 if delete > 0:
#                     conn = mysql.connector.connect(
#                         host="localhost", username="root", password="#include stdio.h687", database="maazdb")
#                     my_cursor = conn.cursor()
#                     my_cursor.execute(
#                         "delete from students where Student_id=%s", (self.var_std_id.get(),))
#                 else:
#                     if not delete:
#                         return

#                 conn.commit()
#                 self.fetch_data()
#                 conn.close()
#                 messagebox.showinfo(
#                     "Delete", "Student deatail deleted successfully", parent=self.root)

#             except Exception as es:
#                 messagebox.showerror(
#                     "Error", f"Due to {str(es)}", parent=self.root)

#     def reset_data(self):
#         self.var_dep.set("Select Department"),
#         self.var_course.set("Select Course"),
#         self.var_year.set("Select Year"),
#         self.var_semester.set("Select Semester"),
#         self.var_std_id.set("")
#         self.var_std_name.set(""),
#         self.var_div.set(""),
#         self.var_roll.set(""),
#         self.var_gender.set(""),
#         self.var_dob.set(""),
#         self.var_email.set(""),
#         self.var_phone.set(""),
#         self.var_address.set(""),
#         self.var_teacher.set(""),
#         self.var_radio1.set("")

# #=================generating dataset =====================

#     def generate_dataset(self):
#         if (self.var_dep.get() == "Select department" or 
#             self.var_course.get() == "Select course" or 
#             self.var_year.get() == "Select year" or 
#             self.var_semester.get() == "Select sem" or 
#             self.var_std_id.get() == "" or 
#             self.var_std_name.get() == "" or 
#             self.var_div.get() == "" or 
#             self.var_roll.get() == "" or 
#             self.var_gender.get() == "" or 
#             self.var_dob.get() == "" or 
#             self.var_email.get() == "" or 
#             self.var_phone.get() == "" or 
#             self.var_address.get() == "" or 
#             self.var_teacher.get() == "" or 
#             self.var_radio1.get() == ""):

#             messagebox.showerror("Error", "All fields are required", parent=self.root)
#         else:
#             try:
#                 conn = mysql.connector.connect(
#                     host="localhost", username="root", password="#include stdio.h687", database="maazdb")
#                 my_cursor = conn.cursor()

#                 # Ensure student details are updated in the database
#                 my_cursor.execute("""
#                     UPDATE students SET 
#                     Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, 
#                     Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s 
#                     WHERE Student_id=%s
#                 """, (
#                     self.var_dep.get(),
#                     self.var_course.get(),
#                     self.var_year.get(),
#                     self.var_semester.get(),
#                     self.var_std_name.get(),
#                     self.var_div.get(),
#                     self.var_roll.get(),
#                     self.var_gender.get(),
#                     self.var_dob.get(),
#                     self.var_email.get(),
#                     self.var_phone.get(),
#                     self.var_address.get(),
#                     self.var_teacher.get(),
#                     self.var_radio1.get(),
#                     self.var_std_id.get()
#                 ))

#                 conn.commit()
#                 conn.close()

#                 # ================= Face Capture =================
#                 cap = cv2.VideoCapture(1)  # Start webcam
#                 img_id = 0  # Ensure new count for every student
#                 student_id = str(self.var_std_id.get())  # Convert student ID to string for filenames

#                 while img_id < 100:
#                     ret, my_frame = cap.read()
#                     if not ret:
#                         continue  # Skip if frame not captured

#                     # Convert the frame to RGB (required by face_recognition)
#                     rgb_frame = cv2.cvtColor(my_frame, cv2.COLOR_BGR2RGB)

#                     # Detect faces in the frame
#                     face_locations = face_recognition.face_locations(rgb_frame)
#                     if len(face_locations) == 0:
#                         continue  # Skip if no face is detected

#                     # Generate face encodings
#                     face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

#                     for face_encoding in face_encodings:
#                         img_id += 1
#                         # Save the face encoding to a file
#                         file_name_path = f"data/user.{student_id}.{img_id}.npy"
#                         np.save(file_name_path, face_encoding)

#                         # Display the face in a window
#                         face = cv2.resize(my_frame, (450, 450))
#                         cv2.putText(face, f"ID {student_id} Img {img_id}", (20, 40),
#                                     cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
#                         cv2.imshow("Cropped Face", face)

#                         if cv2.waitKey(1) == 13:  # If 'Enter' key is pressed, break
#                             break

#                 cap.release()
#                 cv2.destroyAllWindows()

#                 messagebox.showinfo("Success", f"Dataset generated for student ID: {student_id}", parent=self.root)

#             except Exception as es:
#                 messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)
#             finally:
#                 cap.release()
#                 cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# if __name__ == "__main__":
#     root = Tk()
#     obj = Student(root)
#     root.mainloop() 
