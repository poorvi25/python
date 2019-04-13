from tkinter import*
from tkinter.messagebox import*
import sqlite3

con=sqlite3.Connection('hrdb')
cur=con.cursor()
root=Tk()
cur.execute("create table if not exists sales(ID number primary key not null,first_name  varchar(10),last_name varchar(10),district varchar(20))")
Label(root,text="Marvel Sales management M.P.",relief="sunken",font="times 25 bold italic",bg="green").grid(row=0,column=1,columnspan=1)

Label(root,text="Enter Sales manager Id").grid(row=1,column=0)
e=Entry(root)
e.grid(row=1,column=1)
Label(root,text="Enter First Name").grid(row=2,column=0)
f=Entry(root)
f.grid(row=2,column=1)
Label(root,text="Enter Last Name").grid(row=3,column=0)
g=Entry(root)
g.grid(row=3,column=1)
Label(root,text="Enter working district").grid(row=4,column=0)
h=Entry(root)
h.grid(row=4,column=1)
v1=IntVar()
l=[]
Label(root,text="SELECT EACH OF TEA ONE BY ONE TO SEE EMPLOYEE ORDER",font="times 15 bold",bg="yellow").grid(row=5,column=1)
Radiobutton(root,text='Marvel green tea',variable=v1,value='1').grid(row=6,column=0)
Radiobutton(root,text='Marvel masala tea',variable=v1,value='2').grid(row=7,column=0)
Radiobutton(root,text='Marvel yellow tea',variable=v1,value='3').grid(row=8,column=0)
Radiobutton(root,text='Marvel premium tea',variable=v1,value='4').grid(row=9,column=0)
def insert():
    
    i=0
    l.append(e.get())
    for i in range(len(l)-1):
            if l[i]==e.get():
                i=i+1
                showerror('error','Duplicate data')
                break;
            if i==0:
                b=[(e.get(),f.get(),g.get(),h.get())]
                if (int(e.get())>156 or int(e.get())<152):
                    showerror('wrong id','enter id in range of 152 to 155 as emp of mp exist in it')
                else:
                    cur.executemany("insert into sales values(?,?,?,?)",b)
                    con.commit()
                    showinfo('Database','data successfully inserted')
Button(root,text="INSERT",command=insert).grid(row=10,column=3)
def pri():
    
     a=int(e.get())
     b=int(v1.get())
     if(b==0):
         if v1.get()!=1 and v1.get()!=2 and v1.get()!=3 and v1.get()!=4:
             showinfo('Field!','No tea type selected')
     if(b==1):
           if(a==152):    
               sales1=50
               Label(root,text="Marvel green tea sold by employee is:").grid(row=11,column=0)
               Label(root,text=sales1).grid(row=11,column=1)
               Label(root,text="kg").grid(row=11,column=2)
           elif(a==153):  
               sales1=150
               Label(root,text="Marvel green tea sold by employee is:").grid(row=11,column=0)
               Label(root,text=sales1).grid(row=11,column=1)
               Label(root,text="kg").grid(row=11,column=2)
           elif(a==154):
               sales1=100
               Label(root,text="Marvel green tea sold by employee is:").grid(row=11,column=0)
               Label(root,text=sales1).grid(row=11,column=1)
               Label(root,text="kg").grid(row=11,column=2)
           elif(a==155):
               sales1=105
               Label(root,text="Marvel green tea sold by employee is:").grid(row=11,column=0)
               Label(root,text=sales1).grid(row=11,column=1)
               Label(root,text="kg").grid(row=11,column=2)
           elif(a==156):
               sales1=120
               Label(root,text="Marvel green tea sold by employee is:").grid(row=11,column=0)
               Label(root,text=sales1).grid(row=11,column=1)
               Label(root,text="kg").grid(row=11,column=2)
     if(b==2):
         
         if(a==152):           
             sales2=250
             Label(root,text="Marvel masala tea sold by employee is:").grid(row=12,column=0)
             Label(root,text=sales2).grid(row=12,column=1)
             Label(root,text="kg",font="times 10 bold").grid(row=12,column=2)
         elif(a==153):  
             sales2=155
             Label(root,text="Marvel masala tea sold by employee is:").grid(row=12,column=0)
             Label(root,text=sales2).grid(row=12,column=1)
             Label(root,text="kg").grid(row=12,column=2)
         elif(a==154):
             sales2=120
             Label(root,text="Marvel masala tea sold by employee is:").grid(row=12,column=0)
             Label(root,text=sales2).grid(row=12,column=1)
             Label(root,text="kg").grid(row=12,column=2)
         elif(a==155):
             sales2=110
             Label(root,text="Marvel masala tea sold by employee is:").grid(row=12,column=0)
             Label(root,text=sales2).grid(row=12,column=1)
             Label(root,text="kg").grid(row=12,column=2)
         elif(a==156):
             sales2=120
             Label(root,text="Marvel masala tea sold by employee is:").grid(row=12,column=0)
             Label(root,text=sales2).grid(row=12,column=1)
             Label(root,text="kg").grid(row=12,column=2)
             
     if(b==3):
         
         if(a==152):           
             sales3=500
             Label(root,text="Marvel yellow tea sold by employee is:").grid(row=13,column=0)
             Label(root,text=sales3).grid(row=13,column=1)
             Label(root,text="kg").grid(row=13,column=2)
         elif(a==153):  
             sales3=450
             Label(root,text="Marvel yellow tea sold by employee is:").grid(row=13,column=0)
             Label(root,text=sales3).grid(row=13,column=1)
             Label(root,text="kg").grid(row=13,column=2)
         elif(a==154):
             sales3=220
             Label(root,text="Marvel yellow tea sold by employee is:").grid(row=13,column=0)
             Label(root,text=sales3).grid(row=13,column=1)
             Label(root,text="kg").grid(row=13,column=2)
         elif(a==155):
             sales3=320
             Label(root,text="Marvel yellow tea sold by employee is:").grid(row=13,column=0)
             Label(root,text=sales3).grid(row=13,column=1)
             Label(root,text="kg").grid(row=13,column=2)
         elif(a==156):
             sales3=120
             Label(root,text="Marvel yellow tea sold by employee is:").grid(row=13,column=0)
             Label(root,text=sales3).grid(row=13,column=1)
             Label(root,text="kg").grid(row=13,column=2)
           
     if(b==4):
         
         if(a==152):           
             sales4=123
             Label(root,text="Marvel premium tea sold by employee is:").grid(row=14,column=0)
             Label(root,text=sales4).grid(row=14,column=1)
             Label(root,text="kg").grid(row=14,column=2)
         elif(a==153):  
             sales4=145
             Label(root,text="Marvel premium tea sold by employee is:").grid(row=14,column=0)
             Label(root,text=sales4).grid(row=14,column=1)
             Label(root,text="kg").grid(row=14,column=2)
         elif(a==154):
             sales4=223
             Label(root,text="Marvel premium tea sold by employee is:").grid(row=14,column=0)
             Label(root,text=sales4).grid(row=14,column=1)
             Label(root,text="kg").grid(row=14,column=2)
         elif(a==155):
             sales4=323
             Label(root,text="Marvel premium tea sold by employee is:").grid(row=14,column=0)
             Label(root,text=sales4).grid(row=14,column=1)
             Label(root,text="kg").grid(row=14,column=2)
         elif(a==156):
             sales4=420
             Label(root,text="Marvel premium tea sold by employee is:").grid(row=14,column=0)
             Label(root,text=sales4).grid(row=14,column=1)
             Label(root,text="kg").grid(row=14,column=2)
Label(root,text="AFTER PRESSING ALL RADIOBUTTON ONCE",font="times 15 bold",bg="yellow").grid(row=15,column=1)
Label(root,text="Enter the orders you observed for Green Tea").grid(row=16,column=0)
I=Entry(root)
I.grid(row=16,column=1)
Label(root,text="Enter the orders you observed for Masala Tea").grid(row=17,column=0)
J=Entry(root)
J.grid(row=17,column=1)
Label(root,text="Enter the orders you observed for Yellow Tea").grid(row=18,column=0)
K=Entry(root)
K.grid(row=18,column=1)
Label(root,text="Enter the orders you observed for Premium Tea").grid(row=19,column=0)
L=Entry(root)
L.grid(row=19,column=1)
    
def total():
    t=int(I.get())
    u=int(J.get())
    v=int(K.get())
    w=int(L.get())
    a=t+u+v+w
    Label(root,text="total order of employee is").grid(row=20,column=0)
    Label(root,text=a).grid(row=20,column=1)
Button(root,text="TOTAL",command=total).grid(row=21,column=0)

       
def exit():
    root.destroy()
def show():  
    cur.execute('select *from sales')
    t=cur.fetchall()
    Label(root,text=t).grid(row=22,column=1)
    if len(t)==0:
        showerror('error','No database exists')
    else:
        print (t);

        
Button(root,text="SHOW",command=show).grid(row=10,column=2)   
Button(root,text="EXIT",command=exit).grid(row=10,column=1,sticky=E)
Button(root,text="DETAILS",command=pri).grid(row=10,column=0,sticky=E)

root.mainloop()            
