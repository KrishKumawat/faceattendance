import csv
import os
from datetime import datetime
from time import strftime
from tkinter import *
from tkinter import filedialog, messagebox, ttk

import mysql.connector
import numpy as np
from PIL import Image, ImageTk

mydata = []

class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #================= VARAIBLES ====================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()





         #First Image
        img = Image.open(r"Raw Images\Head.jpg")
        img = img.resize((1530,130),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=130)



        #Second Image
        bgimg = Image.open(r"Raw Images\Head_Body.jpg")
        bgimg = bgimg.resize((1530,660),Image.LANCZOS)
        self.photobgimg = ImageTk.PhotoImage(bgimg)

        f_lbl = Label(self.root,image=self.photobgimg)
        f_lbl.place(x=0,y=130,width=1530,height=660)

        title_lbl = Label(f_lbl,text="STUDENT MANAGEMENT SYSTEM", font = ("times new roman", 35, "bold"),bg = "white", fg = "#3e43ec")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1500,height=600)

        #left label Frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT ATTENDANCE DETAILS",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=585)

        #Image left
        img_left = Image.open(r"C:\Users\Administrator\PycharmProjects\Facialrecognitionattendence\Raw Images\student_managment.jpg")
        img_left = img_left.resize((700,100),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=15,y=0,width=700,height=100)

        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=4,y=125,width=720,height=430)

        #attendance ID frame
        attendance_id_label = Label(left_inside_frame, text="Attendance ID" , font=("times new roman", 12, "bold"), bg="white")
        attendance_id_label.grid(row=0, column=0, padx=10, pady=10,sticky=W)

        attendance_id_entry=ttk.Entry(left_inside_frame, textvariable=self.var_atten_id, width=20,font=("times new roman", 12, "bold"))
        attendance_id_entry.grid(row=0,column=1, padx=10, pady=10,sticky=W) 

        #Roll
        Roll_label = Label(left_inside_frame ,text="Roll" , font=("times new roman", 12, "bold"), bg="white")
        Roll_label.grid(row=0, column=2, padx=10, pady=10,sticky=W)

        Roll_entry=ttk.Entry(left_inside_frame, textvariable=self.var_atten_roll, width=20,font=("times new roman", 12, "bold"))
        Roll_entry.grid(row=0,column=3, padx=10, pady=10,sticky=W) 

        #Name
        name_label = Label(left_inside_frame,  text="Name" , font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=10,sticky=W)

        name_entry=ttk.Entry(left_inside_frame, textvariable=self.var_atten_name, width=20,font=("times new roman", 12, "bold"))
        name_entry.grid(row=1, column=1, padx=10, pady=10,sticky=W) 

        #Department
        dep_label1 = Label(left_inside_frame, text="Department" , font=("times new roman", 12, "bold"), bg="white")
        dep_label1.grid(row=1, column=2, padx=10, pady=10,sticky=W)

        dep1_entry=ttk.Entry(left_inside_frame, textvariable=self.var_atten_dep, width=20,font=("times new roman", 12, "bold"))
        dep1_entry.grid(row=1,column=3, padx=10, pady=10,sticky=W) 

        #time frame
        time_label = Label(left_inside_frame, text="Time :" , font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=10,sticky=W)

        time_entry=ttk.Entry(left_inside_frame, textvariable=self.var_atten_time, width=20,font=("times new roman", 12, "bold"))
        time_entry.grid(row=2,column=1, padx=10, pady=10,sticky=W) 

        #date frame
        date_label = Label(left_inside_frame, text="Date :" , font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=10,sticky=W)

        date_entry=ttk.Entry(left_inside_frame, textvariable=self.var_atten_time,width=20,font=("times new roman", 12, "bold"))
        date_entry.grid(row=2,column=3, padx=10, pady=10,sticky=W) 

        #attendance Combobox
        attendance_label1 = Label(left_inside_frame, text="Attendance Status" , font=("times new roman", 12, "bold"), bg="white")
        attendance_label1.grid(row=3, column=0, padx=10, pady=10,sticky=W)

        attendance_combo=ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly",width=17)
        attendance_combo["values"]=("Status", "Present", "Absent")
        attendance_combo.grid(row=3,column=1,padx=20,pady=10,sticky=W)
        attendance_combo.current(0)



        #buttons frame
        btn_frame=Frame(left_inside_frame,bd= 2,relief=RIDGE)
        btn_frame.place(x=6,y=220,width=700,height=35)

        #Import Button
        Import_btn=Button(btn_frame,text="Import CSV",command=self.importCSV,font=("times new roman", 12, "bold"),bg="Blue",fg="white",width=18)
        Import_btn.grid(row=0,column=0)

        #Export
        Export_btn = Button(btn_frame, text="Export CSV",command=self.exportCsv,font=("times new roman", 12, "bold"), bg="Blue", fg="white", width=19)
        Export_btn.grid(row=0, column=1)

        #Update
        Update_btn = Button(btn_frame, text="Update",command=self.update_data,font=("times new roman", 12, "bold"), bg="Blue", fg="white", width=18)
        Update_btn.grid(row=0, column=2)

        #reset
        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data,font=("times new roman", 12, "bold"), bg="Blue", fg="white", width=19)
        reset_btn.grid(row=0, column=3)







        #Right frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="ATTENDANCE ",font=("times new roman", 12, "bold"))
        Right_frame.place(x=760, y=10, width=730, height=550)

        right_inside_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        right_inside_frame.place(x=5,y=0,width=716,height=520)


        #========= SCROLL BAR TABLE +++++++++++++=======
        scroll_x = ttk.Scrollbar(right_inside_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(right_inside_frame,orient=VERTICAL)

        self.AttandanceReportTable = ttk.Treeview(right_inside_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttandanceReportTable.xview)
        scroll_y.config(command=self.AttandanceReportTable.yview)

        self.AttandanceReportTable.heading("id",text="Attendance ID")
        self.AttandanceReportTable.heading("roll",text="Roll")
        self.AttandanceReportTable.heading("name",text="Name")
        self.AttandanceReportTable.heading("department",text="Department")
        self.AttandanceReportTable.heading("time",text="Time")
        self.AttandanceReportTable.heading("date",text="Date")
        self.AttandanceReportTable.heading("attendance",text="Attendance")
        self.AttandanceReportTable["show"]="headings"

        self.AttandanceReportTable.column("id",width=100)
        self.AttandanceReportTable.column("roll",width=100)
        self.AttandanceReportTable.column("name",width=100)
        self.AttandanceReportTable.column("department",width=100)
        self.AttandanceReportTable.column("time",width=100)
        self.AttandanceReportTable.column("date",width=100)
        self.AttandanceReportTable.column("attendance",width=100)

        self.AttandanceReportTable.pack(fill=BOTH,expand=1)

        self.AttandanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #================= FECTH DATA ===================

    def fetchdata(self,rows):
        self.AttandanceReportTable.delete(*self.AttandanceReportTable.get_children())
        for i in rows:
            self.AttandanceReportTable.insert("",END,values=i)

    #importCSV  
    def importCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent = self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)

            self.fetchdata(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data", "No Data Found to export",parent= self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent = self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data has been Exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)    

    #-----------------GET CURSOR-------------------
    def get_cursor(self,event=""):
        cursor_row = self.AttandanceReportTable.focus()
        content = self.AttandanceReportTable.item(cursor_row)
        row = content['values']

























        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6])




    
    #------------------UPDATE BUTTON---------------------    
    def update_data(self):
        if self.var_atten_attendance.get()=="Status" or self.var_atten_name.get()=="" or self.var_atten_id.get()==0:
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update the Student Details",parent = self.root)
                if Update>0:
                    conn=mysql.connector.connect(host = "localhost", username = "root", password = "wecrxd7fpv", database = "face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Roll=%s,Name=%s,Dep=%s,time=%s,date=%s,attendance=%s where atten_id=%s",(
                                                                                                                                        self.var_atten_roll.get(),
                                                                                                                                        self.var_atten_name.get(),
                                                                                                                                        self.var_atten_dep.get(),
                                                                                                                                        self.var_atten_time.get(),
                                                                                                                                        self.var_atten_date.get(),
                                                                                                                                        self.var_atten_attendance.get(),
                                                                                                                                        self.var_atten_id.get(),
                                                                                                                                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details Successfully updated",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent = self.root)





    #--------------------RESET BUTTON--------------------
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")





if __name__ =="__main__":  
    root = Tk()
    obj = Attendance(root)
    root.mainloop()