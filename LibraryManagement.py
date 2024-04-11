from tkinter import *
from tkinter import messagebox
import cx_Oracle
from tkinter import ttk

win=Tk()
win.title("Library Management system")
win.maxsize(height=2000,width=2000)
win.minsize(height=800,width=800)
win.state('zoomed')
def student():
    f=Frame(bg="#fff")
    f.place(x=0,y=0,width=1500,height=988)
    f.configure(bg="#fff")
    stu=Label(f,text="STUDENTS",bg="yellow" ,font=("bold",20))
    stu.place(relx=0.4,rely=0.05)
    Label(f,image=img1,border=0,bg='white').place(relx=0.3,rely=0.2)
    bu1 = Button(f, height=2, width=25, text=' Register', bg="pink", command=register)
    bu2 = Button(f, height=2, width=25, text=' Login ',bg="pink", command=Loginstu)
    bu1.place(x=450,y=500)
    bu2.place(x=750,y=500)
def Loginstu():
    global stu1
    global stu2
    f1=Frame(bg="#fff")
    f1.place(x=0,y=0,width=1500,height=988)
    f1.configure(bg="#fff")
    labl_0=Label(f1,text="LOGIN",font=("bold",20),bg="blue")
    labl_0.place(x=600,y=50)
    labl_1 = Label(f1, text="USER ID", width=20, font=("bold", 10) ,bg="#fff")
    labl_1.place(x=450, y=130)
    stu1=Entry(f1)
   
   # messagebox.showinfo('message', msg)
    stu1.place(x=600, y=130)
    labl_2 = Label(f1,text="PASSWORD", width=20, font=("bold", 10),bg="#fff")
    labl_2.place(x=450, y=170)
    stu2= Entry(f1,show='*')
    stu2.place(x=600, y=170)
    Button(f1, text='Submit', width=20, bg='brown', fg='white',command=options).place(x=600, y=210)
def checklogin():
    conn=cx_Oracle.connect(user='C##SANJOT',password='6284')
    cur=conn.cursor()
    q2="select userid ,password from student where userid:1 and password:2"
    cur.execute(q2,(stu1.get(),stu2.get()))
    conn.commit()
    cur.close()

    
def Loginlib():
    global user_id
    global login_pass
    win = Tk()
    win.title("LOGIN")
    win.geometry("600x600+480+180")
    labl_0 = Label(win, text="ADMIN LOGIN ", font=("bold", 20), bg="purple")
    labl_0.place(x=210, y=50)
    labl_1 = Label(win, text="User Id", width=20, font=("bold", 10))
    labl_1.place(x=130, y=130)
    user_id= Entry(win)
    user_id.place(x=300, y=130)
    labl_2 = Label(win, text="Password", width=20, font=("bold", 10))
    labl_2.place(x=130, y=170)

    login_pass = Entry(win,show='*')
    login_pass.place(x=300, y=170)
    Button(win, text='Submit', width=20, bg='green', fg='white',command=option_lib).place(x=230, y=210)
    Button(win, text='EXIT', width=20, bg='red', fg='white',command=win.destroy).place(x=230, y=250)

    win.mainloop()
def login():
    conn=cx_Oracle.connect(user='C##SANJOT',password='6284')
    cur=conn.cursor()
    q2="select user_id ,login_pass from student where user_id:1 and login_pass:2"
    cur.execute(q2,(user_id.get(),login_pass.get()))
    conn.commit()
    cur.close()


def enter():
    conn=cx_Oracle.connect(user='C##SANJOT',password='6284')
    cur=conn.cursor()
    q1=f"insert into student values('{entry_1.get()}','{entry_2.get()}','{entry_3.get()}','{entry_4.get()}')"
    cur.execute(q1)
    conn.commit()
    cur.close()
    conn.close()
    
def register():
    global entry_1
    global entry_2
    global entry_3
    global entry_4
    f2=Frame(bg="#fff")
    f2.place(x=0,y=0,width=1500,height=988)
    f2.configure(bg="#fff")
    labl_0 = Label(f2, text="Registration form", width=20, font=("bold", 20))
    labl_0.place(x=90, y=53)

    labl_1 = Label(f2, text="USER NAME", width=20, font=("bold", 10))
    labl_1.place(x=80, y=130)

    entry_1 = Entry(f2)
    entry_1.place(x=240, y=130)

    labl_2 = Label(f2, text="USER ID", width=20, font=("bold", 10))
    labl_2.place(x=80, y=180)

    entry_2 = Entry(f2)
    entry_2.place(x=240, y=180)


    labl_3= Label(f2, text="PASSWORD", width=20, font=("bold", 10))
    labl_3.place(x=80, y=230)

    entry_3 = Entry(f2)
    entry_3.place(x=240, y=230)
    
    
    labl_4 = Label(f2, text="PHONE NUMBER", width=20, font=("bold", 10))
    labl_4.place(x=80, y=280)

    entry_4 = Entry(f2,show='*')
    entry_4.place(x=240, y=280)

    Button(f2, text='Submit', width=20, bg='brown', fg='white',command=enter).place(x=180, y=380)

    print("Registration form is created seccussfully...")


def option_lib():
    var.get()
    win = Tk()
    win.title('Library')
    win.geometry("600x600+480+180")
    win.resizable(False, False)
    b1 = Button(win, height=2, width=25, text=' Add Books ',bg="aqua", command=addbook)
    b2 = Button(win, height=2, width=25, text=' Issued Books ',bg="aqua", command=issuedbooks)
    b3 = Button(win, height=2, width=25, text=' Returned Books ',bg="aqua", command=returnbook)
    b4 = Button(win, height=2, width=25, text=' View Books ', bg="aqua",command=viewbook)
    b6 = Button(win, height=2, width=25, text=' Delete Books ', bg="aqua",command=deletebook)
    b7 = Button(win, height=2, width=25, text=' LogOut ', bg="red",command=win.destroy)
    b1.place(x=160, y=30)
    b2.place(x=160, y=80)
    b3.place(x=160, y=130)
    b4.place(x=160,y=180)
    b6.place(x=160, y=230)
    b7.place(x=160, y=280)
def viewbook():
    conn=cx_Oracle.connect(user='C##SANJOT',password='6284')
    cur=conn.cursor()
    cur.execute("select * from bookDB")
    t=cur.fetchall()
    if len(t) != 0:
        win=Tk()
    
    
        frame=Frame(win)
        frame.pack(side=LEFT)
        tv=ttk.Treeview(frame,columns=(1,2,3),show="headings" ,height="5")
        tv.grid(row=1,column=1,columnspan=2,padx=0,pady=10)
        tv.column(1,anchor=CENTER,width=160)
        tv.heading(1,text="BOOK NAME")
        tv.column(2,anchor=CENTER,width=160)
        tv.heading(2,text="BOOK NUMBER")
        tv.column(3,anchor=CENTER,width=160)
        tv.heading(3,text="AUTHOR")
        index=0
    
        for i in t:
            tv.insert('','end',values=i)
        index=index+1
        
        win.title("VIEW BOOK")
    
        win.mainloop()
    else:
      messagebox.showinfo("Books", "No Book Added")    
      conn.commit()
      cur.close()

    
    

def issuedbooks():
    conn=cx_Oracle.connect(user='C##SANJOT',password='6284')
    cur=conn.cursor()
    #cur.execute("select * from issue1 where student_name=:1 and student_id=:2 and book_number=:3 and book_name=:4",())
    #a=int(input("enter student id:"))
    #b=int(input("enter book id:"))
    cur.execute("select * from issue1")# where student_id=:1 and book_no=:2",(a,b))
    t=cur.fetchall()
    if len(t) != 0:
        win=Tk()
    
    
        frame=Frame(win)
        frame.pack(side=LEFT)
        tv=ttk.Treeview(frame,columns=(1,2),show="headings" ,height="5")
        tv.grid(row=1,column=1,columnspan=2,padx=0,pady=10)
        tv.column(1,anchor=CENTER,width=160)
        tv.heading(1,text="STUDENT ID")
        tv.column(2,anchor=CENTER,width=160)
        tv.heading(2,text="BOOK NUMBER")
        index=0
    
        for i in t:
            tv.insert('','end',values=i)
        index=index+1
        
        win.title("ISSUE BOOK")
    
        win.mainloop()
    else:
      messagebox.showinfo("Books", "No Book Issued")    
      conn.commit()
      cur.close()

    
    
def stu_issuebook():
    global student_name
    global student_id
    global book_number
    global book_name
    win = Tk()
    win.title('Issue Book')
    win.geometry("400x400+480+180")
    win.resizable(False, False)
    name = Label(win, text='STUDENT NAME')
    student_name = Entry(win)
    student_name.place(x=200, y=50)

    sid = Label(win, text='STUDENT ID')









    student_id = Entry(win)
    student_id.place(x=200, y=100)
    b_no = Label(win, text='BOOK NO')
    book_number= Entry(win)
    book_number.place(x=200, y=150)
    bname = Label(win, text='BOOK NAME')
    book_name = Entry(win)
    book_name.place(x=200, y=200)


    b = Button(win, height=2, width=21, text=' ISSUE BOOK ', command=issuedbooks)
    b1 = Button(win, height=2, width=21, text=' CLOSE ', command=win.destroy)
    name.place(x=70, y=50)
    sid.place(x=70, y=100)
    b_no.place(x=70, y=150)
    bname.place(x=70,y=200)
    b.place(x=100, y=250)
    b1.place(x=100, y=300)
    win.mainloop()
def options():
    win = Tk()
    win.title('Library')
    win.geometry("400x400+480+180")
    win.resizable(False, False)
    b1= Button(win, height=2, width=25, text=' Issue Book ', command=stu_issuebook)
    b2 = Button(win, height=2, width=25, text=' Return Book ', command=stu_returnbook)
    b3 = Button(win, height=2, width=25, text=' Available Books ', command=showbook)
    b4 = Button(win, height=2, width=25, text=' LogOut ',bg='red', command=win.destroy)
    b1.place(x=110, y=80)
    b2.place(x=110, y=130)
    b3.place(x=110,y=180)
    b4.place(x=110, y=250)
    win.mainloop()

    win.mainloop()
def showbook():
    conn=cx_Oracle.connect(user='C##SANJOT',password='6284')
    cur=conn.cursor()
    cur.execute("select * from bookDB")
    t=cur.fetchall()
    if len(t) != 0:
        win=Tk()
    
    
        frame=Frame(win)
        frame.pack(side=LEFT)
        tv=ttk.Treeview(frame,columns=(1,2,3),show="headings" ,height="5")
        tv.grid(row=1,column=1,columnspan=2,padx=0,pady=10)
        tv.column(1,anchor=CENTER,width=160)
        tv.heading(1,text="BOOK NAME")
        tv.column(2,anchor=CENTER,width=160)
        tv.heading(2,text="BOOK NUMBER")
        tv.column(3,anchor=CENTER,width=160)
        tv.heading(3,text="AUTHOR")
        index=0
    
        for i in t:
            tv.insert('','end',values=i)
        index=index+1
        
        win.title("VIEW BOOK")
    
        win.mainloop()
    else:
      messagebox.showinfo("Books", "No Book Added")    
      conn.commit()
      cur.close()

    
        

def issuebooks():
    conn=cx_Oracle.connect(user='C##SANJOT',password='6284')
    cur=conn.cursor()
    q1=f"insert into issue1 values('{student_name.get()}','{student_id.get()}','{book_number.get()}','{book_name.get()}')"
    cur.execute(q1)
    conn.commit()
    cur.close()
    conn.close()
    
    win.mainloop()

def stu_returnbook():
    global student_id
    global book_number
    win = Tk()
    win.title('Return Book')
    win.geometry("400x400+480+180")
    win.resizable(False, False)

    sid = Label(win, text='STUDENT ID')
    student_id = Entry(win)
    student_id.place(x=200, y=100)
    no = Label(win, text='BOOK NO')
    book_number= Entry(win)
    book_number.place(x=200, y=150)


    #now = datetime.datetime.now()


    b = Button(win, height=2, width=21, text=' RETURN BOOK ', command=returnbooks)
    b1 = Button(win, height=2, width=21, text=' CLOSE ', command=win.destroy)
    sid.place(x=100,y=100)
    no.place(x=100,y=150)
    b.place(x=150, y=200)
    b1.place(x=150, y=242)
    win.mainloop()

def returnbooks():
    conn=cx_Oracle.connect(user='C##SANJOT',password='6284')
    cur=conn.cursor()
    q1=f"insert into bookreturn values('{student_id.get()}','{book_number.get()}')"
    cur.execute(q1)
    conn.commit()
    cur.close()
    conn.close()
    
    win.mainloop()    

def addbook():
    global book_name
    global book_number
    global author
    win = Tk()
    win.title('Add Book')
    win.geometry("600x600+480+180")
    win.resizable(False, False)
    sub = Label(win, text="BOOK NAME")
    book_name= Entry(win)
    book_name.place(x=200, y=50)
    tit = Label(win, text='BOOK NUMBER')
    book_number = Entry(win)
    book_number.place(x=200, y=90)
    auth = Label(win, text='AUTHOR')
    author= Entry(win)
    author.place(x=200, y=130)

    b = Button(win, height=2, width=21, text=' ADD BOOK TO DB ', command=addbooks)
    b1 = Button(win, height=2, width=21, text=' CLOSE ', command=win.destroy)
    sub.place(x=70, y=50)
    tit.place(x=70, y=90)
    auth.place(x=70, y=130)
    b.place(x=180, y=210)
    b1.place(x=180, y=252)
    win.mainloop()

def addbooks():
    conn=cx_Oracle.connect(user='C##SANJOT',password='6284')
    cur=conn.cursor()
    q2=f"insert into bookDB values('{book_name.get()}','{book_number.get()}','{author.get()}')"
    cur.execute(q2)
    conn.commit()
    cur.close()
    conn.close()
    win.mainloop()
def returnbook():
    conn=cx_Oracle.connect(user='C##SANJOT',password='6284')
    cur=conn.cursor()
    q2=f"select * from bookreturn"
    cur.execute(q2)
    t=cur.fetchall()
    if len(t) != 0:
        win=Tk()
    
    
        frame=Frame(win)
        frame.pack(side=BOTTOM)
        tv=ttk.Treeview(frame,columns=(1,2),show="headings" ,height="5")
        tv.grid(row=1,column=1,columnspan=2,padx=0,pady=10)
        tv.column(1,anchor=CENTER,width=160)
        tv.heading(1,text="STUDENT ID")
        tv.column(2,anchor=CENTER,width=160)
        tv.heading(2,text="BOOK NUMBER")
        index=0
    
        for i in t:
            tv.insert('','end',values=i)
        index=index+1
        
        win.title("RETURN BOOK")
    
        win.mainloop()
    else:
      messagebox.showinfo("Books", "No Book Issued")    
      conn.commit()
      cur.close()

    
    
    conn.commit()
    cur.close()

    
    win.mainloop()
def deletebook():

    win = Tk()
    win.title('Delete Book')
    win.geometry("400x400+480+180")
    win.resizable(False, False)
    book_name = Label(win, text='BOOK NAME')
    book_name.place(x=100,y=100)
    b_name=Entry(win)
    b_name.place(x=200,y=100)
    b1 = Button(win, height=2, width=21, text=' DELETE FROM DB', command=deletebookdb)
    b1.place(x=200,y=200)
    win.mainloop()

        
def deletebookdb():
    conn=cx_Oracle.connect(user='C##SANJOT',password='6284')
    cur=conn.cursor()
    cur.execute("DELETE  from bookDB where book_name =:1 ")
    win.destroy()
    messagebox.showinfo("Delete", "Book Deleted")
    conn.commit()
    cur.close()

    
    win.mainloop()

#def logout():
 #   win=Tk()
  #  win.destroy()

#    print("Logged Out")

 #   win.mainloop()

labl_0 = Label(win, text="WELCOME TO E-LIBRARY", width=30, font=("bold", 20),bg="Pink")
labl_0.place(x=400,y=80)
var = StringVar()
img=PhotoImage(file='lib.png')
img1=PhotoImage(file='Student.png')
Label(win,image=img,border=0,bg='white').place(x=420,y=200)
btn1=Button(win,text="LIBRARIAN",bg="Sky blue",font=("Arial",15) ,command=Loginlib)
btn1.place(x=120,y=300,relx=0.25,rely=0.3, relwidth=0.1,relheight=0.05)
btn2=Button(win,text="STUDENT",bg="Sky blue",font=("Arial",15) ,command=student)
btn2.place(x=400,y=300,relx=0.25,rely=0.3, relwidth=0.1,relheight=0.05)

win.mainloop()