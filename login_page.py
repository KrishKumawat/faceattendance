import os
import tkinter
from datetime import datetime
from time import strftime
from tkinter import *
from tkinter import messagebox, ttk

import mysql.connector
from PIL import Image, ImageTk

from attendance import Attendance
from developer import Developer
from face_recognition import Face_Recognition
from help import Help
from student import Student
from train import Train


def main():
    win=Tk()
    app=Login_System(win)
    win.mainloop()

class Login_System:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")

        #==========image=================
        img = Image.open(r"Raw Images/Body101.jpg")
        img = img.resize((1530, 790), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1530, height=790)

        #phone Image
        phone_img = Image.open(r"Raw Images/phone.jpg")
        phone_img = phone_img.resize((294, 449), Image.LANCZOS)
        self.photophone_img = ImageTk.PhotoImage(phone_img)

        phone_lbl = Label(self.root, image=self.photophone_img)
        phone_lbl.place(x=500, y=160, width=294, height=449)



        #=======LOGIN FRAME================
        login_frame = Frame(f_lbl,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=850,y=160,width=300,height=450)

        #-------------------------------------------------------
        self.username = StringVar()
        self.password = StringVar()
        #-------------------------------------------------------

        login_img = Image.open(r"Raw Images/loginicon.png")
        login_img = login_img.resize((100, 100), Image.LANCZOS)
        self.photologin_img = ImageTk.PhotoImage(login_img)

        login_icon_lbl = Label(login_frame, background="white",image=self.photologin_img)
        login_icon_lbl.place(x=0, y=-150, width=294, height=449)    


        #=========USER NAME=============
        title1_lbl = Label(login_frame, text="User Name",font=("times new roman", 13), bg="white", fg="black")
        title1_lbl.place(x=1, y=120)

        user_frame = Frame(login_frame,bd=2,relief=RIDGE,bg="white")
        user_frame.place(x=3,y=143,width=290,height=30)

        self.txtuser=ttk.Entry(login_frame,width=20,textvariable=self.username,font=("times new roman", 12, "bold"))
        self.txtuser.place(x=3,y=143,width=290,height=30)



        #========PASSWORD==========
        title_lbl = Label(login_frame, text="Password",font=("times new roman", 13), bg="white", fg="black")
        title_lbl.place(x=1, y=180)

        pwd_frame = Frame(login_frame,bd=2,relief=RIDGE,bg="white")
        pwd_frame.place(x=3,y=203,width=290,height=30) 

        self.txtpass=ttk.Entry(login_frame,width=20,textvariable=self.password,show="*",font=("times new roman", 12, "bold"))
        self.txtpass.place(x=3,y=203,width=290,height=30) 



        #-------LOGIN BUTTON-------
        img2 = Image.open(r"Raw Images/login.jpg")
        img2 = img2.resize((142, 47), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = Button(login_frame,command=self.login , image=self.photoimg2,cursor="hand2")
        b1.place(x=70, y=270, width=142, height=47)


        #-----------HR LABEL------------
        hr = Label(login_frame,bg="light gray")
        hr.place(x=38,y=350,width=200,height=2)

        #------------OR LABEL-----------
        or_ = Label(login_frame, text="OR",font=("times new roman",13),bg="white",fg="light gray")
        or_.place(x=125,y=339)

        #----------Forgot Button-----------
        btn_forgot = Button(login_frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",12),bg="white",fg="black",bd=0,activebackground="white")
        btn_forgot.place(x=85,y=365)

        btn_reg = Button(login_frame,text="New User Register",command=self.register_window,font=("times new roman",12),bg="white",fg="black",bd=0,activebackground="white")
        btn_reg.place(x=80,y=389)













        #------------ANIMATION IMAGES
        self.imag1=ImageTk.PhotoImage(file="Raw Images/phone_img1.png")
        self.imag2=ImageTk.PhotoImage(file="Raw Images/phone_img2.png")
        self.imag3=ImageTk.PhotoImage(file="Raw Images/phone_img3.png")

        self.lbl_change_image =Label(self.root,bd=1,bg = "black")
        self.lbl_change_image.place(x=582,y=180,width=195,height=415)

        self.animate()

    def animate(self):
        self.imag=self.imag1
        self.imag1=self.imag2
        self.imag2=self.imag3
        self.imag3=self.imag
        self.lbl_change_image.config(image=self.imag)
        self.lbl_change_image.after(2000,self.animate)








    #--------------------------------------
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app = Register(self.new_window)













    #--------------LOGIN FUNCTION--------------------
    def login(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error"," All Fields are required !!")
        elif self.username.get()=="Krish" or self.password.get()=="1234":
            messagebox.showinfo("Success","Welcome to my Face \n Recognition Attendance System Project")
        else:
            conn=mysql.connector.connect(host = "localhost", username = "root", password = "wecrxd7fpv", database = "face_recognition")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password = %s",(
                                                                                            self.username.get(),
                                                                                            self.password.get()
                                                                                        ))

            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid User Name and Password")
            else:
                open_main = messagebox.askyesno("YesNo","Access Only to Admin")
                if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            
            conn.commit()
            conn.close()
    
    
            



    #-------------Reset PASSWORD WINDOW------------------------
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question")
        elif self.security_ans.get()=="":
            messagebox.showerror("Error","Please Enter the Answer")
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter the New Password")
        else:
            conn=mysql.connector.connect(host = "localhost", username = "root", password = "wecrxd7fpv", database = "face_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.security_ans.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Please enter the correct answer")
            else:
                query = ("update register set password=%s where email=%s")
                value = (self.txt_newpass.get(),self.username.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info ","Your Password has been Reset\nPlease login with new Password")




    #-------------FORGOT PASSWORD WINDOW------------------------
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host = "localhost", username = "root", password = "wecrxd7fpv", database = "face_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            # print (row)

            if row == None:
                messagebox.showerror("Name Error","please enter a valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",18,"bold"),fg="red",bg="white")
                l.place(x=0,y=20,relwidth=1)

                security=Label(self.root2,text="Select Security Question",font=("time new roman",13,"bold"),bg="white")
                security.place(x=50,y=80)

                self.combo_security_Q = ttk.Combobox(self.root2,font=("time new roman",13,"bold"),state="readonly")
                self.combo_security_Q["values"] = ("Select","Your Birth Place","Your GirlFriend Name", "Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=170)
                self.combo_security_Q.current(0)

                sec_ans=Label(self.root2,text="Security Answer",font=("time new roman",13,"bold"),bg="white")
                sec_ans.place(x=50,y=150)

                self.security_ans = ttk.Entry(self.root2,font=("time new roman",13,"bold"))
                self.security_ans.place(x=50,y=180,width=170)

                new_password=Label(self.root2,text="New Password",font=("time new roman",13,"bold"),bg="white")
                new_password.place(x=50,y=220)

                self.txt_newpass = ttk.Entry(self.root2,font=("time new roman",13,"bold"))
                self.txt_newpass.place(x=50,y=250,width=170)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("time new roman",13,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)



















#class register

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")

        #===================== VARIABLES =========================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()






        self.bg = ImageTk.PhotoImage(file="Raw Images/Body.jpg")
        bg_label = Label(self.root,image=self.bg)
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        #phone Image
        phone_img = Image.open(r"Raw Images/phone.jpg")
        phone_img = phone_img.resize((294, 449), Image.LANCZOS)
        self.photophone_img = ImageTk.PhotoImage(phone_img)

        phone_lbl = Label(self.root, image=self.photophone_img)
        phone_lbl.place(x=500, y=160, width=294, height=449)

        #===============MAin Frame=====================    
        frame= Frame(self.root,bg="white")
        frame.place(x=850,y=160,width=500,height=450)

        register_lbl=Label(frame,text="Register Here",font=("times new roman",17,"bold"),fg="dark green",bg="white")
        register_lbl.place(x=180,y=10)

        #------------Label ---------------
        fname=Label(frame,text="First name",font=("time new roman",13,"bold"),bg="white")
        fname.place(x=50,y=50)

        fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font=("time new roman",13,"bold"))
        fname_entry.place(x=52,y=75,width=170)

        lname=Label(frame,text="Last name",font=("time new roman",13,"bold"),bg="white")
        lname.place(x=250,y=50)

        lname_entry = ttk.Entry(frame,textvariable=self.var_lname,font=("time new roman",13,"bold"))
        lname_entry.place(x=252,y=75,width=170)


        #----------2nd row------------
        con=Label(frame,text="Contact No",font=("time new roman",13,"bold"),bg="white")
        con.place(x=50,y=115)

        con_entry = ttk.Entry(frame,textvariable=self.var_contact,font=("time new roman",13,"bold"))
        con_entry.place(x=52,y=140,width=170)

        email=Label(frame,text="Email",font=("time new roman",13,"bold"),bg="white")
        email.place(x=250,y=115)

        email_entry = ttk.Entry(frame,textvariable=self.var_email,font=("time new roman",13,"bold"))
        email_entry.place(x=252,y=140,width=170)


        #----------2nd row------------
        sec=Label(frame,text="Security",font=("time new roman",13,"bold"),bg="white")
        sec.place(x=50,y=190)

        self.combo_sec_Q = ttk.Combobox(frame,textvariable=self.var_securityQ,font=("time new roman",13,"bold"),state="readonly")
        self.combo_sec_Q["values"] = ("Select","Your Birth Place","Your GirlFriend Name", "Your Pet Name")
        self.combo_sec_Q.place(x=52,y=215,width=170)
        self.combo_sec_Q.current(0)

        sec_ans=Label(frame,text="Security Answer",font=("time new roman",13,"bold"),bg="white")
        sec_ans.place(x=250,y=190)

        sec_ans_entry = ttk.Entry(frame,textvariable=self.var_securityA,font=("time new roman",13,"bold"))
        sec_ans_entry.place(x=252,y=215,width=170)



        #-----------PWD----------------
        pwd=Label(frame,text="Password",font=("time new roman",13,"bold"),bg="white")
        pwd.place(x=50,y=255)

        pwd_entry = ttk.Entry(frame,textvariable=self.var_pass,font=("time new roman",13,"bold"))
        pwd_entry.place(x=52,y=280,width=170)

        pwd_con=Label(frame,text="Confirm Password",font=("time new roman",13,"bold"),bg="white")
        pwd_con.place(x=250,y=255)

        pwd_con_entry = ttk.Entry(frame,textvariable=self.var_confpass,font=("time new roman",13,"bold"))
        pwd_con_entry.place(x=252,y=280,width=170)



        #============CHECK BUTTON==========================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree the terms and conditons",font=("time new roman",12),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=330)



        #----------REGISTER BUTTONS----------------
        img=Image.open(r"Raw Images/register.png")
        img=img.resize((80,25),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)

        b1= Button(frame,image=self.photoimage, command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=80,y=380)

        #----------LOGIN BUTTONS----------------
        img1=Image.open(r"Raw Images/login_btn.jpg")
        img1=img1.resize((80,25),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        b2= Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b2.place(x=290,y=380)













        #------------ANIMATION IMAGES---------------
        self.imag1=ImageTk.PhotoImage(file="Raw Images/phone_img1.png")
        self.imag2=ImageTk.PhotoImage(file="Raw Images/phone_img2.png")
        self.imag3=ImageTk.PhotoImage(file="Raw Images/phone_img3.png")

        self.lbl_change_image =Label(self.root,bd=1,bg = "black")
        self.lbl_change_image.place(x=582,y=180,width=195,height=415)

        self.animate()

    def animate(self):
        self.imag=self.imag1
        self.imag1=self.imag2
        self.imag2=self.imag3
        self.imag3=self.imag
        self.lbl_change_image.config(image=self.imag)
        self.lbl_change_image.after(2000,self.animate)






        #==========FUNCTION DECLARATION===============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password is not same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree the terms and Conditions")
        else:
            conn=mysql.connector.connect(host = "localhost", username = "root", password = "wecrxd7fpv", database = "face_recognition")
            my_cursor = conn.cursor()
            query=("select * from register where email =%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exists \n Please Try Again",parent = self.root)

            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()

                                                                                        ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registered SuccessFully",parent = self.root)

    def return_login(self):
        self.root.destroy()





class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Head Image
        img = Image.open(r"Raw Images/Head.jpg")
        img = img.resize((1530, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1530, height=130)

        # Body Image
        bgimg = Image.open(r"Raw Images/Head_Body.jpg")
        bgimg = bgimg.resize((1530, 660), Image.LANCZOS)
        self.photobgimg = ImageTk.PhotoImage(bgimg)

        bg_img = Label(self.root, image=self.photobgimg)
        bg_img.place(x=0, y=130, width=1530, height=660)

        title_lbl = Label(bg_img, text="FACE  RECOGNITION  ATTENDENCE  SYSTEM  SOFTWARE",font=("times new roman", 35, "bold"), bg="white", fg="#2bacff")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #============ TIME ===========
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = Label(bg_img, font=("times new roman", 14,"bold"),background="white",foreground="blue")
        lbl.place(x=0,y=20,width=110,height=50)
        time()


        # student button1
        img1 = Image.open(r"Raw Images/btn1.jpg")
        img1 = img1.resize((220, 220), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1 = Button(bg_img, image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        # student button2
        img2 = Image.open(r"Raw Images/btn2.jpg")
        img2 = img2.resize((220, 220), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b2 = Button(bg_img, image=self.photoimg2,command= self.Face_Data ,cursor="hand2")
        b2.place(x=500, y=100, width=220, height=220)

        # student button3
        img3 = Image.open(r"Raw Images/btn3.jpg")
        img3 = img3.resize((220, 220), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b3 = Button(bg_img, image=self.photoimg3, command=self.attendance_Data ,cursor="hand2")
        b3.place(x=800, y=100, width=220, height=220)

        # student button4
        img4 = Image.open(r"Raw Images/btn4.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b4 = Button(bg_img, image=self.photoimg4,command=self.help ,cursor="hand2")
        b4.place(x=1100, y=100, width=220, height=220)

        # student button5
        img5 = Image.open(r"Raw Images/btn5.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b5 = Button(bg_img, image=self.photoimg5,command=self.Train_data,cursor="hand2")
        b5.place(x=200, y=370, width=220, height=220)

        # student button6
        img6 = Image.open(r"Raw Images/btn6.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b6 = Button(bg_img, image=self.photoimg6, command=self.open_img, cursor="hand2")
        b6.place(x=500, y=370, width=220, height=220)

        # student button7
        img7 = Image.open(r"Raw Images/btn7.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b7 = Button(bg_img, image=self.photoimg7, command=self.developer, cursor="hand2")
        b7.place(x=800, y=370, width=220, height=220)

        # student button8
        img8 = Image.open(r"Raw Images/btn8.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b8 = Button(bg_img, image=self.photoimg8, command=self.iexit, cursor="hand2")
        b8.place(x=1100, y=370, width=220, height=220)


    def open_img(self):
        os.startfile("data")



        # ===============Function Buttons======================

    def student_details(self):
         self.new_window = Toplevel(self.root)
         self.app = Student(self.new_window)


    def Train_data(self):
         self.new_window = Toplevel(self.root)
         self.app = Train(self.new_window)

    def Face_Data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_Data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure want to Exit the window", parent = self.root)
        if self.iexit > 0:
            self.root.destroy()
        else:
            return
        
    











if __name__ == "__main__":
    main()