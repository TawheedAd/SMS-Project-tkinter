def addstudent():
    def submitbtn():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addtime = time.strftime("%H:%M:%S")
        adddate = time.strftime("%d/%m/%Y")
        try:
            str = "insert into studentsdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(str,(id,name,mobile,email,address,gender,dob,addtime,adddate))
            con.commit()
            res = messagebox.askyesnocancel("Notifications","id {} name {} Added Sucessfully ... and want to clean the form".format(id,name),parent=addroot)
            if(res==True):
                idval.set(" ")
                nameval.set(" ")
                mobileval.set(" ")
                emailval.set(" ")
                addressval.set(" ")
                genderval.set(" ")
                dobval.set(" ")
                addtime.set(" ")
                adddate.set(" ")
        except:
           #messagebox.showerror("Notification"," ID Already Exist Try Another ID....", parent=addroot)
           pass


        str = "select * from studentsdata"
        cursor.execute(str)
        data = cursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in data:
         vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
         studenttable.insert('',END,values=vv)




    addroot = Toplevel(master=DataEnteryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='blue')
    # addroot.iconbitmap()
    # addroot.miniloop()
    addroot.resizable(False,False)

    #----------------Add Student Labels______________________

    idlabel = Label(addroot,text="Enter ID",bg='gold2',font=('times,20,bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot, text="Enter Name", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text="Mobile Number", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text="Enter Email", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')

    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text="Enter Address", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text="Gender", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text="Enter D.O.B", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    doblabel.place(x=10, y=370)

    ##________________Entry BOX to Labels___________________________________________
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()


    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    ######_____ADD Button---------
    submitbtn = Button(addroot, text= 'submit', font=('roman',15,'bold'),width=20,bd=5,
                    activebackground='blue',activeforeground='white',bg='red',command=submitbtn)
    submitbtn.place(x=150,y=420)


def searchstudent():
    def searchbtn():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        adddate = time.strftime("%d/%m/%Y")
        if(name != ''):
            str = "select * from studentsdata where Name=%s"
            cursor.execute(str,(name))
            data=cursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        if (id != ''):
            str = "select * from studentsdata where Id=%s"
            cursor.execute(str,id)
            data = cursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in data:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEnteryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+130')
    searchroot.title('Student Management System')
    searchroot.config(bg='blue')
    # searchroot.iconbitmap()
    # searchroot.miniloop()
    searchroot.resizable(False, False)

    # ----------------Add Student Labels______________________

    idlabel = Label(searchroot, text="Enter ID", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text="Enter Name", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text="Mobile Number", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                        width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(searchroot, text="Enter Email", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                       width=12, anchor='w')

    emaillabel.place(x=10, y=190)

    addresslabel = Label(searchroot, text="Enter Address", bg='gold2', font=('times,20,bold'), relief=GROOVE,
                         borderwidth=3,
                         width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(searchroot, text="Gender", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                        width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot, text="Enter D.O.B", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                     width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(searchroot, text="Date", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                     width=12, anchor='w')
    datelabel.place(x=10, y=420)

    ##________________Entry BOX to Labels___________________________________________
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=420)

    ######_____ADD Button---------
    searchbtn = Button(searchroot, text='search', font=('roman', 15, 'bold'), width=20, bd=5,
                       activebackground='blue', activeforeground='white', bg='red', command=searchbtn)
    searchbtn.place(x=150, y=470)


def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]

    str = "select * from studentsdata"
    cursor.execute(str)
    data = cursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in data:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)




def updatestudent():


    def updatebtn():

        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()
        strr = "update studentsdata set Name=%s,Mobile=%s,Email=%s,Address=%s,Gender=%s,DOB=%s,Date=%s,Time=%s where Id=%s"
        cursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        print("last")
        # #messagebox.showinfo("Notification","id {} modified Sucessfully ...".format(id))
        # str = "select * from studentsdata"
        #
        # cursor.execute(str)
        # data = cursor.fetchall()
        # studenttable.delete(*studenttable.get_children())
        # for i in data:
        #     vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        #     studenttable.insert('', END, values=vv)
        #

    updateroot = Toplevel(master=DataEnteryFrame)
    updateroot.grab_set()
    updateroot.geometry('490x590+220+100')
    updateroot.title('Student Management System')
    updateroot.config(bg='blue')
    # updateroot.iconbitmap()
    # updateroot.miniloop()
    updateroot.resizable(False, False)

    # ----------------Add Student Labels______________________

    update_idlabel = Label(updateroot, text="Update ID", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    update_idlabel.place(x=10, y=10)

    update_namelabel = Label(updateroot, text="Update Name", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    update_namelabel.place(x=10, y=70)

    update_mobilelabel = Label(updateroot, text="Update Number", bg='gold2', font=('times,20,bold'), relief=GROOVE,
                        borderwidth=3,
                        width=12, anchor='w')
    update_mobilelabel.place(x=10, y=130)

    update_emaillabel = Label(updateroot, text="Update Email", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                       width=12, anchor='w')

    update_emaillabel.place(x=10, y=190)

    update_addresslabel = Label(updateroot, text="Update Address", bg='gold2', font=('times,20,bold'), relief=GROOVE,
                         borderwidth=3,
                         width=12, anchor='w')
    update_addresslabel.place(x=10, y=250)

    update_genderlabel = Label(updateroot, text="Update Gender", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                        width=12, anchor='w')
    update_genderlabel.place(x=10, y=310)

    update_doblabel = Label(updateroot, text="Update D.O.B", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                     width=12, anchor='w')
    update_doblabel.place(x=10, y=370)

    update_datelabel = Label(updateroot, text="Update Date", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    update_datelabel.place(x=10, y=420)

    update_timelabel = Label(updateroot, text="Update Time", bg='gold2', font=('times,20,bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    update_timelabel.place(x=10, y=470)

    ##________________Entry BOX to Labels___________________________________________
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    update_identry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    update_identry.place(x=250, y=10)

    update_nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    update_nameentry.place(x=250, y=70)

    update_mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    update_mobileentry.place(x=250, y=130)

    update_emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    update_emailentry.place(x=250, y=190)

    update_addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    update_addressentry.place(x=250, y=250)

    update_genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    update_genderentry.place(x=250, y=310)

    update_dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    update_dobentry.place(x=250, y=370)

    update_dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    update_dateentry.place(x=250, y=420)

    update_timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=timeval)
    update_timeentry.place(x=250, y=470)

    ######_____ADD Button---------
    updatebtn = Button(updateroot, text='Update', font=('roman', 15, 'bold'), width=20, bd=5,
                       activebackground='blue', activeforeground='white', bg='red', command=updatebtn)
    updatebtn.place(x=150, y=530)

    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) !=0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])


def showstudent():
    str = "select * from studentsdata"
    cursor.execute(str)
    data = cursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in data:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)


def exportstudent():
    ff =filedialog.asksaveasfilename()
    gg=studenttable.get_children()
    id,name,mobile,email,address,gender,dob,date,time =[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp=content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),address.append(pp[3]),gender.append(pp[4]),email.append(pp[5]),
        dob.append(pp[6]),date.append(pp[7]),time.append(pp[8])
    dd = ['ID','Name','Mobile','Address','Email','Gender','DOB','Date','Time']
    df = pandas.DataFrame(list(zip( id,name,mobile,address,email,gender,dob,date,time)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo("Notifications","Data is saved {}".format(paths))
def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you want to exit')
    if (res == True):
        root.destroy()



####################################CONNECT DB##############
def connectdb():
    def submitdb():
        global  con,cursor
        # host = hostval.get()
        # user = userval.get()
        # password = passwordval.get()
        host = "localhost"
        user = "root"
        password = "root"
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            cursor = con.cursor()
        except:
            messagebox.showerror("Notification","Data is incorrect please try again")
            return
        try:
               str = "create database studentmanagementsys"
               cursor.execute(str)
               str = "use studentmanagementsys"
               cursor.execute(str)
               str = 'create table studentsdata(Id varchar(7),Name varchar(20),Mobile varchar(12),Email varchar(30),Address varchar(100),Gender varchar(50),DOB varchar(50),Date varchar(50),Time varchar(50))'
               cursor.execute(str)
               str = 'alter table studentdataa modify column  id int not null'
               cursor.execute(str)
               str = 'alter table studentdataa modify column  id int primary key'
               cursor.execute(str)
               messagebox.showinfo("Notification","Database created Now You Are  Connected To The DataBase ...",parent=dbroot)

        except:
            str = "use studentmanagementsys"
            cursor.execute(str)
            messagebox.showinfo("Notification", "Now You Are  Connected To The DataBase ...", parent=dbroot)
            dbroot.destroy()
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    #dbroot.iconbitmap()
    dbroot.resizable(False, False)
    dbroot.config(bg="blue")
    ####DBLabels#####
    hostlabel=Label(dbroot,text="Enter Host :", bg="gold2", font=("times",20,"bold"),relief=GROOVE, borderwidth=3,
                    width=13)
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot, text="Enter User :", bg="gold2", font=("times", 20, "bold"), relief=GROOVE, borderwidth=3,
                    width=13)
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text="Enter Password :", bg="gold2", font=("times", 20, "bold"), relief=GROOVE, borderwidth=3,
                    width=13)
    passwordlabel.place(x=10, y=130)
#____________ENTRYBOX_FOR_DB_LABELS
    hostval=StringVar()
    userval=StringVar()
    passwordval=StringVar()

    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

#________ConnectDB---submit Button_________________________________________

    submitbtn = Button(dbroot,text="submit",font=('roman',15,'bold') ,width=20  , activebackground="red", activeforeground="white", command=submitdb)
    submitbtn.place(x=150,y=190)


###################################################################################
def tick():

    time_string = time.strftime("%H:%M:%S")
    date_string= time.strftime("%d/%m/%Y")
    clock.config(text='Date :' + date_string + "\n" +"Time :" + time_string)
    clock.after(200,tick)

#===============================The First Frame
from tkinter import *
import time
import random
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql



root = Tk()
root.title("Student Management System")
# root.config(bg='blue3')
# root.iconbitmap(.ico)
root.geometry('1100x700+140+2')
root.resizable(False, False)


bg = PhotoImage(file="bgp.png")
my_label=Label(root,image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# #create a Canvas
# my_canvas = Canvas(root, width=800, height=500)
# my_canvas.pack(fill="both", expand =True)
# # set Image in Canvas
# my_canvas.create_image(0,0, image=bg)



##########################FIRST FRAMES FOR OPTIONS#######################################

DataEnteryFrame = Frame(root,borderwidth=2)
DataEnteryFrame.place(x=10,y=70,width=500,height=600)
# bg = PhotoImage(file="bgp.png")
# my_label=Label(DataEnteryFrame,image=bg)
# my_label.place(x=1, y=1, relwidth=1, relheight=1)



#############_____Buttons On DataFrame as options ______________________##########33

conntectbutton = Button(DataEnteryFrame,text="Connect to DB",width=25,font=('chiller',20,'bold'),bd=6,bg="skyblue3"
                  ,activebackground="blue", activeforeground="white",command=connectdb) #Connect To DB

conntectbutton.pack(side=TOP,expand=True)

addbtn=Button(DataEnteryFrame,text='1. Add Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE
             ,activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn=Button(DataEnteryFrame,text='2. Search Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE
             ,activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn=Button(DataEnteryFrame,text='3. Delete Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE
             ,activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn=Button(DataEnteryFrame,text='4. Update Student',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE
             ,activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn=Button(DataEnteryFrame,text='5. Show All',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE
             ,activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn=Button(DataEnteryFrame,text='6. Export Data',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE
             ,activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn=Button(DataEnteryFrame,text='7. Exit',width=25,font=('chiller',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE
             ,activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)




##################SECOND FRAME FOR SHOWING THE DATA####################

showDataFrame = Frame(root, relief=GROOVE,borderwidth=2)
showDataFrame.place(x=550,y=80,width=500,height=600)

#________________S H O W __D A T A F R A M E____________________________________________#
style = ttk.Style()
style.configure('TreeView.Heading',font=('chiller',20,'bold'), foreground='blue')
style.configure('TreeView',font=('times', 15,'bold'), foreground='black', background='cyan')
scroll_x = Scrollbar(showDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(showDataFrame, orient=VERTICAL)

studenttable= Treeview(showDataFrame, columns=('ID', 'Name', 'Mobile No.', 'Email', 'Address', 'Gender', 'D.O.B', 'Date', 'Time'),
                       yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('ID',text='ID')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No.',text='Mobile No.')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Date',text='Date')
studenttable.heading('Time',text='Time')
studenttable.pack(fill=BOTH, expand = 1)

studenttable['show'] = 'headings'
studenttable.column('ID',width=100)
studenttable.column('Name',width=100)
studenttable.column('Mobile No.',width=100)
studenttable.column('Email',width=100)
studenttable.column('Address',width=100)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=100)
studenttable.column('Date',width=100)
studenttable.column('Time',width=100)


#######################CLOCK##############################################################

clock = Label(root,font=('times',15,'bold'),width=41)
clock.place(x=550,y=30)
tick()
root.mainloop()