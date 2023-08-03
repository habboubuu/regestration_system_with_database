#import recuired module
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Student:
    #nsawbu lwajiha dyal program
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x6690+1+1')
        self.root.title('school management system')
        self.root.resizable(False, False)
        title = Label(self.root,
        text='Student Registration System',
        bg='#2C2C2C',
        font=('Segoe UI Symbol',14),
        fg='white'
        )
        title.pack(fill=X)
        #------ vriable -----------   //// للتعامل مع حقول الادخال يجب انشاء متغيرات
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.qualification_var = StringVar()
        self.gender_var = StringVar()
        self.email_var = StringVar()
        self.phone_var = StringVar()
        self.address_var = StringVar()
        self.se_var = StringVar()
        self.dell_var = StringVar()
        self.se_by = StringVar()

        #ادوات التكم في البرنامج
        manage_frame = Frame(self.root, bg='white')
        manage_frame.place(x=1, y=32, width=210, height=400)

        lbl_ID = Label(manage_frame, text='ID NUMBER', bg='white')
        lbl_ID.pack()
        ID_Entry = Entry(manage_frame, textvariable=self.id_var, bd='2')
        ID_Entry.pack()

        lbl_Fname = Label(manage_frame, text='FIRST NAME ', bg='white')
        lbl_Fname.pack()
        Fname_Entry = Entry(manage_frame,textvariable=self.firstname_var, bd='2')
        Fname_Entry.pack() 

        lbl_Lname = Label(manage_frame, text='LAST NAME', bg='white')
        lbl_Lname.pack()
        Lname_Entry = Entry(manage_frame, textvariable=self.lastname_var, bd='2')
        Lname_Entry.pack()                

        lbl_q = Label(manage_frame, text='QUALIFICATIONS', bg='white')
        lbl_q.pack()
        q_Entry = Entry(manage_frame, textvariable=self.qualification_var, bd='2')
        q_Entry.pack() 

        lbl_gender = Label(manage_frame, text='GENDER', bg='white')
        lbl_gender.pack()
        gender_combo= ttk.Combobox(manage_frame,textvariable=self.gender_var,
        value = ('famele', 'male'), state='readonly'
        )
        gender_combo.pack()       

        lbl_email = Label(manage_frame, text='EMAIL', bg='white')
        lbl_email.pack()
        email_Entry = Entry(manage_frame, textvariable=self.email_var, bd='2')
        email_Entry.pack()

        lbl_phone = Label(manage_frame, text='PHONE', bg='white')
        lbl_phone.pack()
        phone_Entry = Entry(manage_frame, textvariable=self.phone_var, bd='2')
        phone_Entry.pack()

        lbl_address = Label(manage_frame, text='ADDRESS', bg='white')
        lbl_address.pack()
        address_Entry = Entry(manage_frame, textvariable=self.address_var, bd='2')
        address_Entry.pack()   

        lbl_delete = Label(manage_frame, text='DELETE BY ID', fg='red', bg='white')
        lbl_delete.pack()
        delete_Entry = Entry(manage_frame, textvariable=self.dell_var, bd='2')
        delete_Entry.pack()
        # -------- Buttons الازرار ------------
        btn_frame = Frame(self.root, bg='white')
        btn_frame.place(x=1, y=438, width=210, height=450)
        title1 = Label(btn_frame, text='dashboard', font=('Deco', 14), fg='white', bg='#2C2C2C')
        title1.pack(fill=X)

        add_btn = Button(btn_frame, text='ADD STUDENT', bg='#5D5D5D', fg='white', command=self.add_student)
        add_btn.place(x=33, y=45, width=150, height=30)

        delete_btn = Button(btn_frame, text='DELETE STUDENT', bg='#5D5D5D', fg='white', command=self.delete)
        delete_btn.place(x=33, y=80, width=150, height=30)        

        modifi_btn = Button(btn_frame, text='MODIFICATION DATA', bg='#5D5D5D', fg='white', command=self.update)
        modifi_btn.place(x=33, y=115, width=150, height=30)

        empty_btn = Button(btn_frame, text='EMPTY', bg='#5D5D5D', fg='white', command=self.clear)
        empty_btn.place(x=33, y=150, width=150, height=30)

        about_btn = Button(btn_frame, text='ABOUT', bg='#5D5D5D', fg='white', command=self.about)
        about_btn.place(x=33, y=185, width=150, height=30)

        exit_btn = Button(btn_frame, text='EXIT', bg='#5D5D5D', fg='white', command=root.quit)
        exit_btn.place(x=33, y=220, width=150, height=30)

        # ---------- search manage البحث --------
        search_frame = Frame(self.root, bg='white')
        search_frame.place(x=209, y=32, width=1150, height=50)

        lbl_search = Label(search_frame, text='SEARCH', bg='white')
        lbl_search.place(x=50, y=12)

        search_combo= ttk.Combobox(search_frame, textvariable=self.se_by,
        value = ('id', 'last_name', 'email'), state='readonly'
        )
        search_combo.place(x=110, y=12 ) 

        search_entry = Entry(search_frame, textvariable=self.se_var, bd='2')
        search_entry.place(x=280, y=12, width=150, height=23)

        se_btn = Button(search_frame, text='search', bg='#5D5D5D', fg='white', command=self.search)
        se_btn.place(x=440, y=12, width=50, height=22)

        #dietals عرض البيانات
        dietals_frame = Frame(self.root, bg='silver')
        dietals_frame.place(x=210, y=80, width=1140, height=700)
    
        #scroll
        scroll_x = Scrollbar(dietals_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(dietals_frame, orient=VERTICAL)
        #treeview
        self.student_table = ttk.Treeview(dietals_frame, 
        columns=('id','first_name', 'last_name', 'qualification', 'gender', 'email', 'phone', 'address'),
        xscrollcommand = scroll_x.set,
        yscrollcommand = scroll_y.set)
        self.student_table.place(x=1, y=1, width=1123, height=595)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        #اظهار الحقول                
        self.student_table['show'] = 'headings'
        self.student_table.heading('address', text='ADDRESS')
        self.student_table.heading('phone', text='PHONE')
        self.student_table.heading('email', text='EMAIL')
        self.student_table.heading('gender', text='GENDER')
        self.student_table.heading('qualification', text='QUALIFICATION')
        self.student_table.heading('last_name', text='LAST NAME')
        self.student_table.heading('first_name', text='FIRST NAME')
        self.student_table.heading('id', text='ID')
        #Nsghru colums bach manst3mluch scroll
        self.student_table.column('address', width=110)
        self.student_table.column('phone', width=35)
        self.student_table.column('email', width=60)
        self.student_table.column('gender', width=25)
        self.student_table.column('qualification', width=25)
        self.student_table.column('last_name', width=12)
        self.student_table.column('first_name', width=12)
        self.student_table.column('id', width=17)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        
    #connection with database and active button add -------------
        self.fetch_all()
    def add_student(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='stud')  #CONNECTION WITH DATABASE
        cur = con.cursor()        #A cursor is an object which helps to execute the query and fetch the records from the database.
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s)",(  #This method executes the given database operation (query or command) ////             
                                                                # %s kndiruha 3la 9d l79ul li3andna
                                                                # kul mtaghyer  dawr dyalu y7fad lbyanat ldakhlha lmostakhdem 
                                                                self.id_var.get(),    
                                                                self.firstname_var.get(),
                                                                self.lastname_var.get(),
                                                                self.qualification_var.get(),
                                                                self.gender_var.get(),
                                                                self.email_var.get(),
                                                                self.phone_var.get(),
                                                                self.address_var.get()
                                                                
                                                                ))
        con.commit() #The commit() method is used to make sure the changes made to the database are consistent.
        self.fetch_all()
        self.clear()
        con.close()
        # add_btn command=self.add_student


    #treevie // ntl3u data f treeview                جلب البيانات fetchall
    def fetch_all(self): 
        con = pymysql.connect(host='localhost', user='root', password='', database='stud')
        cur = con.cursor()
        cur.execute('select * from students')
        rows = cur.fetchall() #The method fetches all (or all remaining) rows of a query result set and returns a list of tuples. If no more rows are available, it returns an empty list.
        if len(rows) !=0:
            self.student_table.delete(* self.student_table.get_children())  # dar self.student_table z3ma ytla3 f treeview
            for row in rows:
                self.student_table.insert("", END, value=row)
            con.commit()
        con.close()

    #delete student ------- حدف طالب ------
    def delete(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='stud')
        cur = con.cursor()
        cur.execute('delete from students where id=%s',self.dell_var.get())
        con.commit()
        self.fetch_all()
        con.colose()

        #del_btn command=self.delete
    #----------- button empty افراغ الحقول -----------
    def clear(self):
        self.id_var.set('')
        self.firstname_var.set('')
        self.lastname_var.set('')
        self.qualification_var.set('')
        self.gender_var.set('')
        self.email_var.set('')
        self.phone_var.set('')
        self.address_var.set('')
        #btn empty command = self.clear
    
    # ------ Button modification data student ---------
    def get_cursor(self,ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.address_var.set(row[7])
        self.phone_var.set(row[6])
        self.email_var.set(row[5])
        self.gender_var.set(row[4])       
        self.qualification_var.set(row[3])
        self.lastname_var.set(row[2])
        self.firstname_var.set(row[1])
        self.id_var.set(row[0])
    
    def update(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='stud')
        cur = con.cursor()
        cur.execute('UPDATE students SET address=%s, phone=%s, email=%s, gender=%s, qualification=%s, last_name=%s, first_name=%s WHERE id=%s', (
                self.address_var.get(),
                self.phone_var.get(),
                self.email_var.get(),
                self.gender_var.get(),
                self.qualification_var.get(),
                self.lastname_var.get(),
                self.firstname_var.get(),
                self.id_var.get()
                ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
        #update_btn command=self.update

    def search(self): #serach matsawbax b smiya w kniya !
        con = pymysql.connect(host='localhost', user='root', password='', database='stud')
        cur = con.cursor()
        cur.execute("select * from students where " + 
        str(self.se_by.get()) + " LIKE '%"+str(self.se_var.get())+"%'")
        
        rows=cur.fetchall()
        if len(rows) !=0:
            self.student_table.delete(* self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
            con.commit()
        con.close()         #se_btn  command=self.search
    
    #-------   button about -----------
    def about(self):
        messagebox.showinfo("devloper houssam ", "welcome to proj")
        #about_btn command=self.about
    
        


        










root = Tk()
ob = Student(root)
root.mainloop()
