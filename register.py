from tkinter import *


class register:
    def __init__(self,root) :
        self.root = root
        self.root.title("Registration For The Contact-Book")
        self.root.geometry("1400x700")

#>>>>>>>>>>>>>>Registration-Frame>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        frame1 = Frame(self.root,bg = "white")
        frame1.place(x = 300, y = 100, width = 700, height = 500)

        title = Label(frame1,text ="Register Here", font = ("times new roman", 20, "bold"),bg = "white", fg = "cyan").place (x = 50, y = 30)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>first and last Name Row
        
        fs_name = Label(frame1,text ="First Name: ", font = ("times new roman", 15, "bold"),bg = "white", fg = "gray").place (x = 50, y = 100)
        text_fsname = Entry(frame1, font = ("times new roman", 12), bg = "lightgray").place(x = 50, y = 130, width = 250)


        ls_name = Label(frame1,text ="Last Name: ", font = ("times new roman", 15, "bold"),bg = "white", fg = "gray").place (x = 370, y = 100)
        text_lsname = Entry(frame1, font = ("times new roman", 12), bg = "lightgray").place(x = 370, y = 130, width = 250)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Contact and Email Row        

        contact = Label(frame1,text ="Contact No.: ", font = ("times new roman", 15, "bold"),bg = "white", fg = "gray").place (x = 50, y = 170)
        text_contact = Entry(frame1, font = ("times new roman", 12), bg = "lightgray").place(x = 50, y = 200, width = 250)


        email = Label(frame1,text ="E-Mail: ", font = ("times new roman", 15, "bold"),bg = "white", fg = "gray").place (x = 370, y = 170)
        text_email = Entry(frame1, font = ("times new roman", 12), bg = "lightgray").place(x = 370, y = 200, width = 250)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Password Row

        password = Label(frame1,text ="Password: ", font = ("times new roman", 15, "bold"),bg = "white", fg = "gray").place (x = 50, y = 240)
        text_password = Entry(frame1, font = ("times new roman", 12), bg = "lightgray").place(x = 50, y = 270, width = 250)


        chpassword = Label(frame1,text ="Change Password: ", font = ("times new roman", 15, "bold"),bg = "white", fg = "gray").place (x = 370, y = 240)
        text_chpassword = Entry(frame1, font = ("times new roman", 12), bg = "lightgray").place(x = 370, y = 270, width = 250)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Terms & Condition Row

        check = Checkbutton(frame1, text = "I agree the terms & condition", onvalue = 1, offvalue = 0, bg = "white", font = ("times new roman", 12)).place(x = 50, y = 320)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Button

        R_btn = Button(frame1, text = "Register", font = ("times new roman",20) ,cursor = "hand2", bg = "White", bd =0).place(x = 50, y = 380)
        L_btn = Button(frame1, text = "Sign In",font = ("times new roman",20), cursor = "hand2", bg = "White", bd =0).place(x = 450, y = 380, width = 180)

root = Tk()
obj = register(root)
root.mainloop()