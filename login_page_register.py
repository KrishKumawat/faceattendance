from tkinter import *
from tkinter import messagebox, ttk

import mysql.connector
from PIL import Image, ImageTk


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






        self.bg = ImageTk.PhotoImage(file="Raw Images\Body.jpg")
        bg_label = Label(self.root,image=self.bg)
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        #phone Image
        phone_img = Image.open(r"Raw Images\phone.jpg")
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
        img=Image.open(r"Raw Images\register.png")
        img=img.resize((80,25),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)

        b1= Button(frame,image=self.photoimage, command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=80,y=380)

        #----------LOGIN BUTTONS----------------
        img1=Image.open(r"Raw Images\login_btn.jpg")
        img1=img1.resize((80,25),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        b2= Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2")
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
                messagebox.showerror("Error","User Already Exists \n Please Try Again")

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
                messagebox.showinfo("Success","Registered SuccessFully")














if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()