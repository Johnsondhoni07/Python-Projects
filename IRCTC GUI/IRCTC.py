from tkinter import *
from PIL import ImageTk
import pymysql
import time


root=Tk()
root.title('IRCTC')
root.geometry('1366x700')
root.resizable('False','False')

def proceed():
    root.title('Personal details')
    frame2=Frame(root,bg='white',height=500,width=500).place(x=100,y=100)
    label21=Label(frame2,text='enter',fg='white',bg='black').place(x=150,y=150)
    label22=Button(frame2,text='Quit',fg='white',bg='black',command=printt).place(x=250,y=450)

    
bg=ImageTk.PhotoImage(file="indian-railways.png")
label_img=Label(root,image=bg).pack(padx=0,pady=0)
label1=Button(root,text='LOGIN',bg='red',font='aerial',command='log_but').place(x=50,y=10)

label2=Button(root,text='REGISTER',fg='red',bg='black',command='reg_but').place(x=150,y=10.5)

label3=Button(root,text='AGENT LOGIN',fg='red',bg='black',command='ag_but').place(x=225,y=10.5)

label4=Button(root,text='Contact Us',fg='red',bg='black',command='con_but').place(x=325,y=10.5)
        
display_time=time.strftime('%d/%m/%Y %H:%M:%S (%A)')
        
label5=Label(root,text=display_time,bg='black',fg='red',height=2,width=25).place(x=1100,y=10.5)

label6=Button(root,text='Alert',fg='red',bg='black',command='alt_but').place(x=400,y=10.5)

label7=Button(root,text='IRCTC EXCLUSIVE',bg='blue',fg='black',command='ex_but').place(x=50,y=50)

label8=Button(root,text='Buses',fg='red',bg='black',command='buses').place(x=175,y=50)

label9=Button(root,text='Flight',fg='red',bg='black',command='flight').place(x=225,y=50)

label10=Button(root,text='Hotel',fg='red',bg='black',command='hotel').place(x=280,y=50)

label11=Button(root,text='Holidays',fg='red',bg='black',command='holiday').place(x=330,y=50)

label12=Button(root,text='Meals',fg='red',bg='black',command='meals').place(x=400,y=50)

frame1=Frame(root,bg='black',height='550',width='600').place(x=150,y=130)
label13=Label(frame1,text='BOOK TICKET',font=('aerial',25,'bold'),relief='solid',fg='red',bg='black').place(x=325,y=200)
frm=StringVar()
to=StringVar()
dob=StringVar()
cls=StringVar()
typ=StringVar()
def printt():
    From_=frm.get()
    To_=to.get()
    Travel_date=dob.get()
    Class_=cls.get()
    Type_=typ.get()
    print('Departure Point',From_)
    print('Arrival Point',To_)
    print('Date Of Birth',Travel_date)
    print('Type of Class',Class_)
    print('Type of Ticket',Type_)
    
    dbc=pymysql.connect(host='localhost',user='root',passwd='',db='IRCTC')
    c=dbc.cursor()
    #sql='insert into IRCTC_Details (Departure_Point,Arrival_Point,Traveling_date,Class_Need,Type_Need) values(From_,To_,Travel_date,Class_,Type_)'
    sql = "INSERT INTO IRCTC_Details (Departure_Point,Arrival_Point,Traveling_date,Class_Need,Type_Need) VALUES (%s, %s,%s, %s,%s)"
    val = (From_,To_,Travel_date,Class_,Type_)
    c.execute(sql,val)
    dbc.commit()
    root.destroy()
    

label14=Label(frame1,text='FROM',fg='red',bg='black',font=('aerial',12,'bold')).place(x=200,y=277)
entry1=Entry(frame1,textvar=frm,width=25).place(x=300,y=280)

label15=Label(frame1,text='TO',fg='red',bg='black',font=('aerial',12,'bold')).place(x=200,y=327)
entry2=Entry(frame1,textvar=to,width=25).place(x=300,y=330)
label16=Label(frame1,text='DATE',fg='red',bg='black',font=('aerial',12,'bold')).place(x=200,y=377)
label17=Label(frame1,text='(DD-MM-YYYY)',fg='red',bg='black',font=('aerial',12)).place(x=500,y=377)
entry2=Entry(frame1,textvar=dob,width=25).place(x=300,y=380)

label18=Label(frame1,text='CLASS',fg='red',bg='black',font=('aerial',12,'bold')).place(x=200,y=430)
list1=['Exec. Chair Car (EC)','AC 2 Tier (2A)','First Class (FC)','AC 3 Tier (3A)','AC 3 Economy (3E)','AC Chair car (CC)','Sleeper (SL)','Second Sitting (2S)']
opmenu=OptionMenu(frame1,cls,*list1).place(x=300,y=430)
cls.set('SELECT CLASS')
        
label19=Label(frame1,text='TYPE',fg='red',bg='black',font=('aerial',12,'bold')).place(x=200,y=480)
list2=['GENERAL','LADIES','LOWER BERTH/SR.CITIZEN','DIVYAANG','TATKAL','PREMIUM TATKAL']
opmenu=OptionMenu(frame1,typ,*list2).place(x=300,y=480)
typ.set('SELECT TYPE')


    
    
chk_1=Checkbutton(frame1,text='Divyaang concession',fg='red',bg='black',font=('aerial',12,'bold')).place(x=200,y=530)
chk_2=Checkbutton(frame1,text='Railway Pass concession',fg='red',bg='black',font=('aerial',12,'bold')).place(x=400,y=530)
chk_3=Checkbutton(frame1,text='Train with available Berth',fg='red',bg='black',font=('aerial',12,'bold')).place(x=200,y=560)
label20=Button(frame1,text='Proceed',fg='red',bg='black',font=('aerial',20,'bold'),command=printt).place(x=350,y=600)


root.mainloop()


    
        
        
    

