from tkinter import *
from tkinter import messagebox, ttk
import os
import cv2
import mysql.connector
from PIL import Image, ImageTk


class Student:
    def __init__(self,root):
        self.root =  root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #-------------VARIABLES--------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()



         #Head Image
        img = Image.open(r"Raw Images/Head.jpg")
        img = img.resize((1530,130),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=130)



        #Body Image
        bgimg = Image.open(r"Raw Images/Head_Body.jpg")
        bgimg = bgimg.resize((1530,660),Image.LANCZOS)
        self.photobgimg = ImageTk.PhotoImage(bgimg)

        bg_img = Label(self.root,image=self.photobgimg)
        bg_img.place(x=0,y=130,width=1530,height=660)

        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font = ("times new roman", 35, "bold"),bg = "white", fg = "#3e43ec")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=2,y=50,width=1520,height=600)

        #left label Frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",13,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=585)

        #Image LEFT FRAME
        img_left = Image.open(r"Raw Images/student_managment.jpg")
        img_left = img_left.resize((700,100),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=15,y=0,width=700,height=100)

        #current course information
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information",font=("times new roman", 13, "bold"))
        current_course_frame.place(x=5, y=120, width=717, height=120)

        #Department Label
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=20,pady=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=20,pady=10,sticky=W)

        #Course Label
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=20,pady=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=17)
        course_combo["values"]=("Select Course", "SE", "FE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=20,pady=10,sticky=W)

        # Year
        Year_label = Label(current_course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        Year_label.grid(row=1, column=0, padx=20, pady=10,sticky=W)

        Year_combo = ttk.Combobox(current_course_frame ,textvariable=self.var_year ,font=("times new roman", 13, "bold"), state="readonly",width=17)
        Year_combo["values"] = ("Select Year", "First", "Second", "Third", "Forth")
        Year_combo.current(0)
        Year_combo.grid(row=1, column=1, padx=20, pady=10,sticky=W)

        # Semester
        Semester_label = Label(current_course_frame, text="Semester" , font=("times new roman", 13, "bold"), bg="white")
        Semester_label.grid(row=1, column=2, padx=20, pady=10,sticky=W)

        Semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 13, "bold"), state="readonly",width=17)
        Semester_combo["values"] = ("Select Semester", "1 Semester", "2 Semester")
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=3, padx=20, pady=10,sticky=W)

        #Class Student information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white" , relief=RIDGE, text="Student Information",font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=240, width=717, height=317)

        # Student_ID
        student_id_label = Label(class_student_frame, text="Student ID" , font=("times new roman", 13, "bold"), bg="white")
        student_id_label.grid(row=0, column=0, padx=10, pady=10,sticky=W)

        student_id_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_id,font=("times new roman", 13, "bold"))
        student_id_entry.grid(row=0,column=1, padx=10, pady=10,sticky=W)

        # Student Name
        student_name_label = Label(class_student_frame, text="Student Name" , font=("times new roman", 13, "bold"), bg="white")
        student_name_label.grid(row=0, column=2, padx=10, pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_name,font=("times new roman", 13, "bold"))
        student_name_entry.grid(row=0,column=3, padx=10, pady=5,sticky=W)

        # Class Division
        class_division_label = Label(class_student_frame, text="Class Division" , font=("times new roman", 13, "bold"), bg="white")
        class_division_label.grid(row=1, column=0, padx=10, pady=5,sticky=W)

        division_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="readonly",width=17)
        division_combo["values"]=("A", "B", "C")
        division_combo.current(0)
        division_combo.grid(row=1,column=1,padx=11,pady=10,sticky=W)

        #class_division_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_div,font=("times new roman", 13, "bold"))
        #class_division_entry.grid(row=1,column=1, padx=10, pady=5,sticky=W)

        # Roll No
        rollno_label = Label(class_student_frame, text="Roll No" , font=("times new roman", 13, "bold"), bg="white")
        rollno_label.grid(row=1, column=2, padx=10, pady=5,sticky=W)

        rollno_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_roll,font=("times new roman", 13, "bold"))
        rollno_entry.grid(row=1,column=3, padx=10, pady=5,sticky=W)

        # Gender
        Gender_label = Label(class_student_frame, text="Gender" , font=("times new roman", 13, "bold"), bg="white")
        Gender_label.grid(row=2, column=0, padx=10, pady=10,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #Gender_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_gender,font=("times new roman", 13, "bold"))
       # Gender_entry.grid(row=2,column=1, padx=10, pady=5,sticky=W)

        # DOB
        DOB_label = Label(class_student_frame, text="DOB" , font=("times new roman", 13, "bold"), bg="white")
        DOB_label.grid(row=2, column=2, padx=10, pady=5,sticky=W)

        DOB_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=("times new roman", 13, "bold"))
        DOB_entry.grid(row=2,column=3, padx=10, pady=5,sticky=W)

        # Email
        Email_label = Label(class_student_frame, text="EMAIL" , font=("times new roman", 13, "bold"), bg="white")
        Email_label.grid(row=3, column=0, padx=10, pady=5,sticky=W)

        Email_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_email,font=("times new roman", 13, "bold"))
        Email_entry.grid(row=3,column=1, padx=10, pady=5,sticky=W)

        # Phone_no
        phoneno_label = Label(class_student_frame, text="Phone No." , font=("times new roman", 13, "bold"), bg="white")
        phoneno_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phoneno_entry = ttk.Entry(class_student_frame, width=20, textvariable=self.var_phone , font=("times new roman", 13, "bold"))
        phoneno_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, width=20,textvariable=self.var_address , font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1,text="Take a Photo Sample", value="Yes")
        radiobtn1.grid(row=6,column=0,pady=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1,pady=0)

        #buttons frame
        btn_frame=Frame(class_student_frame,bd= 2,relief=RIDGE)
        btn_frame.place(x=3,y=222,width=705,height=35)

        #Save Button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("times new roman", 12, "bold"),bg="Blue",fg="white",width=18)
        save_btn.grid(row=0,column=0)

        #update
        update_btn = Button(btn_frame, text="Update",command=self.update_data,font=("times new roman", 12, "bold"), bg="Blue", fg="white", width=19)
        update_btn.grid(row=0, column=1)

        #Delete
        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data,font=("times new roman", 12, "bold"), bg="Blue", fg="white", width=18)
        delete_btn.grid(row=0, column=2)

        #reset
        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data,font=("times new roman", 12, "bold"), bg="Blue", fg="white", width=19)
        reset_btn.grid(row=0, column=3)


        #button frame 2
        btn_frame1=Frame(class_student_frame,bd= 2,relief=RIDGE)
        btn_frame1.place(x=3,y=252,width=705,height=35)

        # Take a Photo
        reset_btn = Button(btn_frame1, text="Take a Photo Sample", command=self.generate_dataset , font=("times new roman", 12, "bold"), bg="Blue", fg="white",width=38)
        reset_btn.grid(row=0, column=0)

        # Update Photo
        reset_btn = Button(btn_frame1, text="Update Photo Sample", font=("times new roman", 13, "bold"), bg="Blue", fg="white",width=38)
        reset_btn.grid(row=0, column=1)









        #Right frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="DATABASE",font=("times new roman", 13, "bold"))
        Right_frame.place(x=760, y=10, width=730, height=550)

        #Image Right FRAME
        img_right = Image.open(r"Raw Images/student_managment.jpg")
        img_right = img_right.resize((700,100),Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=15,y=0,width=700,height=100)

        #==============SEARCH SYSTEM====================
        search_frame=LabelFrame(Right_frame,bg="white",font=("times new roman", 13, "bold"),bd=2,relief=RIDGE,text="Search System")
        search_frame.place(x=5,y=100,width=715,height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 13, "bold"), bg="red",fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        Semester_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), state="readonly",width=15)
        Semester_combo["values"] = ("Select", "Roll_No", "Phone_No")
        Semester_combo.current(0)
        Semester_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman", 13, "bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn = Button(search_frame, text="Search", font=("times new roman", 13, "bold"), bg="Blue",fg="white", width=13)
        search_btn.grid(row=0, column=3, padx=4)

        showall_btn = Button(search_frame, text="Show all", font=("times new roman", 13, "bold"), bg="Blue",fg="white", width=13)
        showall_btn.grid(row=0, column=4, padx=4)







        #==========Table Frame================
        table_frame=Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=700, height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","rollno","gender","dob","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem",  text="Semester")
        self.student_table.heading("id", text="Student Id")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("rollno", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="Photo  Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem",  width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("rollno", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=150)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=200)
        self.student_table.column("photo", width=130)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #=====================FUNCTION DECLARATION=========================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()==0:
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host = "localhost", username = "root", password = "wecrxd7fpv", database = "face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_radio1.get()

                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been Added SuccessFully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)



    #========================Fetch DATA================================
    def fetch_data(self):
        conn=mysql.connector.connect(host = "localhost", username = "root", password = "wecrxd7fpv", database = "face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


#=====================GET CURSOR ===================================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]


        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_radio1.set(data[13])



    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()==0:
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update the Student Details",parent = self.root)
                if Update>0:
                    conn=mysql.connector.connect(host = "localhost", username = "root", password = "wecrxd7fpv", database = "face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                self.var_std_id.get()
                                                                                                                                                                                                            ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details are successfully updated",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent = self.root)

    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required", parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do yo want to delete this student",parent = self.root)
                if delete>0:
                    conn=mysql.connector.connect(host = "localhost", username = "root", password = "wecrxd7fpv", database = "face_recognition")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id = %s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfuly Deleted Student Details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent = self.root)    


    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")


 #==============GENERATE DATA SET ====================================

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()==0:
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host = "localhost", username = "root", password = "wecrxd7fpv", database = "face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,EMail=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                            self.var_std_id.get() == id+1
                                                                                                                                                                                                                        ))
                

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
                #==================LOAD PREDEFINED DATA ON FACE FRONTAL FROM OPENCV================
                
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #Minimum Neighbour = 5
                    
                    for (x, y, w, h) in faces:
                        face_cropped = img [y:y+h,x:x+w]
                        return face_cropped
                
                cap = cv2.VideoCapture(1)
                img_id = 0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1 
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating Data Sets Completed",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)








if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()