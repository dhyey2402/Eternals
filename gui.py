import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
root.geometry('1920x1080')
root.title("Edutech")

label = tk.Label(root, text="Edutech")
label.pack()
def adm():
    newWindow = Toplevel(root)
    newWindow.title('login')
    newWindow.geometry('925x500+300+200')
    newWindow.configure(bg='#fff')
    newWindow.resizable(False,False)

    img = PhotoImage(file='istockphoto-1281150061-1024x1024.png')
    Label(newWindow, image=img, bg='white').place(x=50,y=50)

    frame = Frame(newWindow, width=350, height=350, bg='white')
    frame.place(x=480, y=70)

    heading = Label(frame, text="Sign In", fg='#57a1f8', bg='white', font=('oswald',23,'bold')).place(x=100,y=5)
    def sign_in():
        username=user.get()
        password=code.get()
        if username=='admin' and password=='aps@123':
                screen = Toplevel(newWindow)
                screen.title("Edutech")
                screen.geometry("925x500+300+200")
                screen.config(bg='white')
        elif username!='admin' and password!='aps@123':
            messagebox.showerror("Invalid", "Invalid Username and Password")
        elif password!='aps@123':
            messagebox.showerror("Invalid", "Invalid Password")
        elif username!='admin':
            messagebox.showerror("Invalid", "Invalid username")

    user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
    user.place(x=50,y=80)
    user.insert(0,'Username')
    user.bind()
    user.bind()
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=104)
    ##########################################################################
    code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light',11))
    code.place(x=50,y=150)
    code.insert(0,'Password')
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=174)
    code.bind()
    code.bind()

    btn = Button(frame, text='Sign In',width=39,pady=7, border=0,bg='#57a1f8',fg='white', command=sign_in).place(x=35,y=204)

    newWindow.mainloop()
    ##########################################################################
    
b1 = Button(root, text='Administration', font=("algerian","21"), command=adm).place(x=540,y=300)
b2 = Button(root, text='Parent/Student', font=("algerian","20")).place(x=540,y=370)
root.mainloop()