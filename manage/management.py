from tkinter import *
import sqlite3
from tkinter import messagebox

class er(Exception):
    def __init__(self):
        pass

class en(Exception):
    def __init__(self):
        pass

class et(Exception):
    def __init__(self):
        pass

class em(Exception):
    def __init__(self):
        pass

root = Tk()
root.title("HOTEL MANAGEMENT SYSTEM")
root.geometry("1600x800+00+00")
#root.configure(bg="purple")

C = Canvas(root, bg="black", height=250, width=300)
filename = PhotoImage(file="C:\\Users\\vishwanath honawad\\Pictures\\Screenshots\\Screenshot (3).png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.place()

kgg=IntVar()
str1=StringVar()
str2=StringVar()
str3=IntVar()
num=IntVar()
room=IntVar()
pay=StringVar()
pas1=StringVar()
pas2=StringVar()
pd=StringVar()
psd=StringVar()
st=IntVar()
uprn=IntVar()
st1=IntVar()
nday=IntVar()
rmno=IntVar()
phno=IntVar()
ps1=StringVar()
ps2=StringVar()
fe1=IntVar()
fe2=StringVar()
fe3=StringVar()

def printm():
    try:
        conn = sqlite3.connect('management.db')
        cur = conn.cursor()
        query = """create table if not exists "manage"(roomno int primary key,name text , addr text,phoneno int,noofdays int,
        typ text,brkf text,pas text) """
        cur.execute(query)
        conn.commit()
        roomn = kgg.get()
        name =str1.get()
        addr = str2.get()
        phoneno =str3.get()
        noofdays = num.get()
        pass1=pas1.get()
        pass2=pas2.get()
        tn=room.get()

        if pass1 !=pass2:
            raise em

        if roomn>= 1 and roomn<=25:
            typ = "DELUX"
        elif roomn>= 26 and roomn<=50:
            typ = "GENERAL"
        elif roomn>= 51 and roomn<=75:
            typ = "JOINT"
        elif roomn>= 76 and roomn<=100:
            typ = "FULL_DELUX"

        if ((roomn<=0 or roomn >100)  or name=="" or addr=="" or phoneno<=0 or noofdays<=0 or pass1=="" or pass2=="" ):
            raise en
        c = 0
        n = phoneno
        while n != 0:
            n //= 10
            c += 1
        if c != 10:
            raise er

        if tn == 1:
            brkf = "with_food_delivery"
        elif tn == 2:
            brkf = "with_out_food_delivery"
        else:
            raise et
        query1 = "insert into manage (roomno,name,addr,phoneno,noofdays,typ,brkf,pas) values(?,?,?,?,?,?,?,?) "
        data = (roomn, name, addr, phoneno, noofdays,typ,brkf,pass1)
        cur.execute(query1, data)
        conn.commit()
        top2 = Toplevel()
        top2.geometry("1600x800+00+00")

        C = Canvas(top2, bg="black", height=250, width=300)
        filename = PhotoImage(file="C:\\Users\\vishwanath honawad\\Pictures\\Screenshots\\Screenshot (3).png")
        background_label = Label(top2, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.place()

        T = Text(top2, height=10, width=80)
        T.place(x=00,y=00)
        T.insert(END, "YOUR ROOM NUMBER IS     :"+ str(data[0])+"\nNAME                    :"+data[1]+"\nADDRESS                 :"+data[2]+
                 "\nPHONE  NUMBER           :"+str(data[3])+"\nNUMBER OF DAYS          :"+str(data[4])+"\nTYPE OF ROOM            :"+data[5]+
                 "\nBREAKFAST AVAILIBILITY  :"+data[6]+"\nYOUR PASSWARD IS        :"+data[7]+"\n")
        lab = Label(top2, text=" YOU HAVE SUCCESSFULLY BOOKED THE ROOM !!!",bg="#876543",fg="#132333",
                    font="Verdana 15 bold italic"    ).place(x=50,y=250)
        bb = Button(top2, text="Okay", command=top2.destroy, fg="white", bg="green", bd=5, height=2, width=50,
                    font="Verdana 10 bold italic").place(x=100, y=300)
        cur.close()
        top2.mainloop()
    except em:
        messagebox.showinfo("PASSWARD ERROR", "PLEASE ENTER SAME PASSWARD AS ABOVE")
    except et:
        messagebox.showinfo("OPTION ERROR", "PLEASE SELECT THE GIVEN OPTION")
    except en:
        messagebox.showinfo("DETAILS ERROR", "PLEASE ENTER ALL DETAILS ")
    except er:
        messagebox.showinfo("DIGIT ERROR", "PLEASE ENTER 10 DIGIT PHONE NUMBER")
    except sqlite3.IntegrityError:
        messagebox.showinfo("ENGAGED ERROR", "\t\tSORRY  \n THIS ROOM HAS BEEN ALREADY ENGAGED")
    except:
        messagebox.showinfo("PROPER INFORMATION ERROR", "PLEASE ENTER PROPER INFORMATION ")

def fun1():
    try:
        top1 = Toplevel()
        top1.geometry("1600x800+00+00")
        C = Canvas(top1, bg="black", height=250, width=300)
        filename = PhotoImage(file="C:\\Users\\vishwanath honawad\\Pictures\\Screenshots\\Screenshot (6).png")
        background_label = Label(top1, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.place()

        l  = Label(top1, text=" SELECT THE ROOM NUMBER\n\nDELUX:1-25\tGENERAL:26-50\tJOINT:51-75\tFULL_DELUX:76-100",
                   font="Verdana 10 bold italic" ).place(x=250,y=20)
        e  = Entry(top1, textvariable=kgg,   width=53,font="large_font").place(x=250,y=90)
        l1 = Label(top1, text=" ENTER YOUR NAME :",font="Verdana 15 bold italic"    ).place(x=250,y=150)
        e1 = Entry(top1, width=17,textvariable=str1 ,font="large_font"   ).place(x=650,y=150)
        l2 = Label(top1, text=" ENTER YOUR ADDRESS :",font="Verdana 15 bold italic" ).place(x=250,y=200)
        e2 = Entry(top1, width=17,textvariable=str2 ,font="large_font"   ).place(x=650,y=200)
        l3 = Label(top1, text=" ENTER YOUR PHONE NUMBER :",font="Verdana 15 bold italic").place(x=250,y=250)
        e3 = Entry(top1, width=17,textvariable=str3 ,font="large_font"   ).place(x=650,y=250)
        l4 = Label(top1, text=" NUMBER OF DAYS ",font="Verdana 15 bold italic"      ).place(x=250,y=300)
        e4 = Entry(top1, width=17,textvariable=num  ,font="large_font"   ).place(x=650,y=300)
        l5 = Label(top1, text="     FOOD DELIVERY     ",font="Verdana 15 bold italic").place(x=375,y=350)
        r1 = Radiobutton(top1, text="with_food_delivery",font="Verdana 15 bold italic", variable=room, value=1).place(x=250,y=400)
        r2 = Radiobutton(top1, text="with_out_food_delivery",font="Verdana 15 bold italic" ,variable=room, value=2).place(x=535,y=400)
        l6 = Label(top1, text=" ENTER YOUR PASSWARD  :", font="Verdana 15 bold italic").place(x=250, y=450)
        e6 = Entry(top1, width=17, textvariable=pas1,show='*', font="large_font").place(x=650, y=450)
        l7 = Label(top1, text=" CONFIRM YOUR PASSWARD  ", font="Verdana 15 bold italic").place(x=250, y=500)
        e7 = Entry(top1, width=17, textvariable=pas2,show='*', font="large_font").place(x=650, y=500)
        b1 = Button(top1, text="SUBMIT", command=printm,       fg="white",bg="green",  bd=5,height=2, width=64,font="Verdana 10 bold italic")\
            .place(x=250,y=550)
        bb = Button(top1, text="Go back", command=top1.destroy,fg="white",bg="red",    bd=5,height=2, width=64,font="Verdana 10 bold italic")\
            .place(x=250,y=600)
        top1.mainloop()
    except:
        messagebox.showinfo("ERROR", "ERROR CLICK ON CORRECT BUTTON")

def fun2():
    try:

        conn = sqlite3.connect('management.db')
        cur = conn.cursor()
        query = """select * from "manage" order by roomno """
        cur.execute(query)
        r = cur.fetchall()
        if r==[]:
            raise er
        top4 = Toplevel()
        top4.geometry("1600x800+00+00")
        C = Canvas(top4, bg="black", height=250, width=300)
        filename = PhotoImage(file="C:\\Users\\vishwanath honawad\\Pictures\\Screenshots\\Screenshot (3).png")
        background_label = Label(top4, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.place()

        b = Button(top4, text="OKAY", height=2, width=10, command=top4.destroy, fg="white", bg="green").place(x=300,y=700)
        T1 = Text(top4, height=40, width=12)
        T1.place(x=00,y=00)
        T2 = Text(top4, height=40, width=12)
        T2.place(x=120,y=00)
        T3 = Text(top4, height=40, width=12)
        T3.place(x=240,y=00)
        T4 = Text(top4, height=40, width=12)
        T4.place(x=360,y=00)
        T5 = Text(top4, height=40, width=14)
        T5.place(x=480,y=00)
        T6 = Text(top4, height=40, width=12)
        T6.place(x=620,y=00)
        T7 = Text(top4, height=40, width=25)
        T7.place(x=740,y=00)
        T1.insert(END, "ROOM NUMBER\n============\n")
        T2.insert(END, "NAME\n============\n")
        T3.insert(END, "ADDRESS\n============\n")
        T4.insert(END, "PHONE NUMBER\n============\n")
        T5.insert(END, "NUMBER OF DAYS\n==============\n")
        T6.insert(END, "TYPE OF ROOM\n============\n")
        T7.insert(END, "FOOD DELIVERY\n=========================\n")
        for row in r:
            T1.insert(END, str(row[0])+"\n____________\n")
            T2.insert(END,row[1]+"\n____________\n")
            T3.insert(END, row[2]+"\n____________\n")
            T4.insert(END, str(row[3])+"\n____________\n")
            T5.insert(END, str(row[4])+"\n______________\n")
            T6.insert(END, row[5]+"\n____________\n")
            T7.insert(END, row[6]+"\n_________________________\n")
        top4.mainloop()
        cur.close()

    except er:
        messagebox.showinfo("NOT OCCUPIED", "NONE OF THE ROOMS ARE OCCUPIED")
    except:
        messagebox.showinfo("NOT OCCUPIED", "NONE OF THE ROOMS ARE OCCUPIED")


def ft():
    try:
        conn = sqlite3.connect('management.db')
        cur = conn.cursor()
        rn = st.get()
        ps=pd.get()
        if (rn<=0 or rn>100):
            raise en
        cur.execute("""select * from manage where roomno=?""", (rn,))
        r = cur.fetchall()
        if r==[]:
            raise er
        if ps !=r[0][7]:
            raise et
        cur.execute("delete from manage where roomno=?", (rn,))
        conn.commit()
        print("row deleted")
        messagebox.showinfo("DELETED", "YOU HAVE BEEN CHECKED OUT FROM THE HOTEL\nTHANK YOU FOR VISITING US")
        cur.close()

    except er:
         messagebox.showinfo("ERROR", "PLEASE ENTER PROPER ROOM NUMBER")
    except en:
         messagebox.showinfo("ERROR", " ROOM DOES NOT EXIST")
    except et:
         messagebox.showinfo("ERROR", " PLEASE ENTER CORRECT PASSWARD ")
    except:
         messagebox.showinfo("ERROR", "UNKNOWN ERROR PLEASE TRY AGAIN LATER")


def fun3():
    try:
        top3 = Toplevel()
        top3.geometry("1600x800+00+00")
        C = Canvas(top3, bg="black", height=250, width=300)
        filename = PhotoImage(file="C:\\Users\\vishwanath honawad\\Pictures\\Screenshots\\Screenshot (9).png")
        background_label = Label(top3, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.place()

        l1 = Label(top3, text=" PLEASE ENTER YOUR ROOM NUMBER TO EXIT  :", fg="green",font="Verdana 20 bold italic").place(x=00, y=50)
        e1 = Entry(top3, width=40,textvariable=st,font="large_font").place(x=00,y=100)
        l2 = Label(top3, text=" PLEASE ENTER YOUR PASSWARD  :", fg="green",
                  font="Verdana 20 bold italic").place(x=00, y=150)
        e2 = Entry(top3, width=40, textvariable=pd,show='*', font="large_font").place(x=00, y=200)
        b1  = Button(top3, text="FORGOT PASSWARD", command=passwardset,fg="white",bg="red",   bd=5,height=1, width=15,
                     font="Verdana 8 bold italic").place(x=200,y=250)
        b2 = Button(top3, text="CLICK HERE TO EXIT",command=ft,fg="white",bg="grey",  bd=5,height=2, width=50,
                    font="Verdana 10 bold italic").place(x=100,y=300)
        b3  = Button(top3, text="GO BACK", command=top3.destroy,fg="white",bg="red",   bd=5,height=2, width=20,
                     font="Verdana 10 bold italic").place(x=00,y=400)
        top3.mainloop()
    except:
        messagebox.showinfo("ERROR", "ERROR")

def fun4():
    try:
        top5 = Toplevel()
        top5.geometry("1600x800+00+00")
        C = Canvas(top5, bg="black", height=250, width=300)
        filename = PhotoImage(file="C:\\Users\\vishwanath honawad\\Pictures\\Screenshots\\Screenshot (3).png")
        background_label = Label(top5, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.place()

        lb1 = Label(top5, text=" PLEASE ENTER THE ROOM NUMBER ",font="Verdana 10 bold italic" ).place(x=00, y=50)
        e1 = Entry(top5, width=30,textvariable=st1,font="large_font" ).place(x=280,y=50)
        b1 = Button(top5, text=" CHECK ", command=ft4,fg="white",bg="GREEN",height=2, width=20,font="Verdana 10 bold italic").place(x=200,y=100)
        b = Button(top5, text="GO BACK", command=top5.destroy,fg="white",bg="RED",height=2, width=20,font="Verdana 10 bold italic")\
            .place(x=00,y=200)
        top5.mainloop()
    except:
        messagebox.showinfo("ERROR", "ERROR")

def ft4():
    try:
        rn = st1.get()
        if (rn <= 0 or rn>100):
            raise en
        conn = sqlite3.connect('management.db')
        cur = conn.cursor()
        cur.execute("""select * from manage where roomno=?""", (rn,))
        r = cur.fetchall()
        if r == []:
            raise er
        else:
            top6 = Toplevel()
            top6.geometry("1600x800+00+00")
            C = Canvas(top6, bg="black", height=250, width=300)
            filename = PhotoImage(file="C:\\Users\\vishwanath honawad\\Pictures\\Screenshots\\Screenshot (3).png")
            background_label = Label(top6, image=filename)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            C.place()

            T1 = Text(top6, height=4, width=12)
            T1.place(x=00, y=00)
            T2 = Text(top6, height=4, width=12)
            T2.place(x=120, y=00)
            T3 = Text(top6, height=4, width=12)
            T3.place(x=240, y=00)
            T4 = Text(top6, height=4, width=12)
            T4.place(x=360, y=00)
            T5 = Text(top6, height=4, width=14)
            T5.place(x=480, y=00)
            T6 = Text(top6, height=4, width=12)
            T6.place(x=620, y=00)
            T7 = Text(top6, height=4, width=25)
            T7.place(x=740, y=00)
            T1.insert(END, "ROOM NUMBER\n============\n")
            T2.insert(END, "NAME\n============\n")
            T3.insert(END, "ADDRESS\n============\n")
            T4.insert(END, "PHONE NUMBER\n============\n")
            T5.insert(END, "NUMBER OF DAYS\n==============\n")
            T6.insert(END, "TYPE OF ROOM\n============\n")
            T7.insert(END, "FOOD DELIVERY\n=========================\n")
            for row in r:
                T1.insert(END, str(row[0]))
                T2.insert(END, row[1])
                T3.insert(END, row[2])
                T4.insert(END, str(row[3]) )
                T5.insert(END, str(row[4]) )
                T6.insert(END, row[5] )
                T7.insert(END, row[6])

            b = Button(top6, text="OKAY", command=top6.destroy,fg="white",bg="green",height=2, width=50,font="Verdana 10 bold italic")\
                .place(x=200,y=80)
            conn.commit()
            cur.close()

            top6.mainloop()

    except er:
        messagebox.showinfo("ERROR", "THE ROOM IS NOT OCCUPIED")
    except en:
        messagebox.showinfo("ERROR", "ENTER THE PROPER ROOM NUMBER")
    except :
        messagebox.showinfo("ERROR", "ENEXPECTED ERROR")


def ft5():
    try:
        ron=uprn.get()
        nd=nday.get()
        ps=psd.get()
        if ron<=0 or ron>100 :
            raise en
        if nd<=0 :
            raise et
        conn = sqlite3.connect('management.db')
        cur = conn.cursor()
        cur.execute("""select * from manage where roomno=?""", (ron,))
        r = cur.fetchall()
        if r==[]:
            raise er
        if ps !=r[0][7]:
            raise em
        for row in r:
            m=nd + row[4]
            cur.execute("""update manage set noofdays=? where roomno=?""", (m,ron,))
        conn.commit()

        cur.execute("""select * from manage where roomno=?""", (ron,))
        r1 = cur.fetchall()
        for i in r1:
            n1=i[0]
            n2=i[4]

        top8 = Toplevel()
        top8.geometry("1600x800+00+00")
        C = Canvas(top8, bg="black", height=250, width=300)
        filename = PhotoImage(file="C:\\Users\\vishwanath honawad\\Pictures\\Screenshots\\Screenshot (3).png")
        background_label = Label(top8, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.place()

        T1 = Text(top8, height=4, width=12)
        T1.place(x=00, y=00)
        T2 = Text(top8, height=4, width=18)
        T2.place(x=100, y=00)
        T1.insert(END,"ROOM NUMBER\n____________\n")
        T2.insert(END, "NUMBER OF DAYS\n______________\n")
        T1.insert(END, n1)
        T2.insert(END, n2)

        lb1 = Label(top8, text=" YOU HAVE SUCCESSFULLY UPDATED YOUR NUMBER OF DAYS TO LIVE ", font="Verdana 10 bold italic").place(x=00, y=100)
        b1 = Button(top8, text=" OKAY ", command=top8.destroy, fg="white", bg="GREEN", height=2, width=20,
                        font="Verdana 10 bold italic").place(x=00, y=200)
        cur.close()

        top8.mainloop()


    except em:
        messagebox.showinfo("ERROR", "INCORRECT PASSWARD OR ROOM NUMBER")
    except en:
        messagebox.showinfo("ERROR", "ENTER THE PROPER ROOM NUMBER")
    except er:
        messagebox.showinfo("ERROR", "THE ROOM IS NOT OCCUPIED")
    except et:
        messagebox.showinfo("ERROR", "PLEASE ENTER PROPER NUMBER OF DAYS")
    except :
        messagebox.showinfo("ERROR", "ENTER PROPER INFORMATION")

def setp():
    try:

        rn=rmno.get()
        pn=phno.get()
        psd1=ps1.get()
        psd2=ps2.get()
        print(psd1)
        print(psd2)

        if psd1!=psd2:
            raise en
        conn = sqlite3.connect('management.db')
        cur = conn.cursor()
        cur.execute("""select * from manage where roomno=?""", (rn,))
        r = cur.fetchall()
        if r[0][3] != pn:
            raise er
        cur.close()


        conn = sqlite3.connect('management.db')
        cur = conn.cursor()
        cur.execute("""update manage set pas=? where roomno=?""", (psd1,rn,))
        conn.commit()
        top10 = Toplevel()
        top10.geometry("1600x800+00+00")
        C = Canvas(top10, bg="black", height=250, width=300)
        filename = PhotoImage(file="C:\\Users\\vishwanath honawad\\Pictures\\Screenshots\\Screenshot (3).png")
        background_label = Label(top10, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.place()

        lb1 = Label(top10, text=" YOU HAVE SUCCESSFULLY CHANGED YOUR PASSWARD  ", font="Verdana 10 bold italic").place(x=00, y=00)
        b1 = Button(top10, text=" OKAY ", command=top10.destroy, fg="white", bg="GREEN", height=2, width=10,
                    font="Verdana 10 bold italic").place(x=00, y=200)
        top10.mainloop()
        cur.close()


    except en:
        messagebox.showinfo("ERROR", "PLEASE ENTER SAME PASSWARD AS ABOVE")
    except er:
        messagebox.showinfo("ERROR", "INNCORRECT PHONE NUMBER ")
    except :
        messagebox.showinfo("ERROR", "PLEASE ENTER ALL INFORMATION CORRECTLY")
def ft45():
    pass

def passwardset():
    try:
        top11 = Toplevel()
        top11.geometry("1600x800+00+00")
        C = Canvas(top11, bg="black", height=250, width=300)
        filename = PhotoImage(file="C:\\Users\\vishwanath honawad\\Pictures\\Screenshots\\Screenshot (3).png")
        background_label = Label(top11, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.place()

        lb1 = Label(top11, text=" ENTER YOUR ROOM NUMBER ", font="Verdana 10 bold italic").place(x=00, y=00)
        e1 = Entry(top11, width=30, textvariable=rmno, font="large_font").place(x=00, y=50)
        lb2 = Label(top11, text="  ENTER YOUR PHONE NUMBER ", font="Verdana 10 bold italic").place(x=00, y=100)
        e2 = Entry(top11, width=30, textvariable=phno, font="large_font").place(x=00, y=150)
        lb3 = Label(top11, text=" ENTER YOUR NEW PASSWARD ", font="Verdana 10 bold italic").place(x=00, y=200)
        e3= Entry(top11, width=30, textvariable=ps1,show='*', font="large_font").place(x=00, y=250)
        lb4 = Label(top11, text=" CONFIRM YOUR NEW PASSWARD", font="Verdana 10 bold italic").place(x=00, y=300)
        e4 = Entry(top11, width=30, textvariable=ps2,show='*', font="large_font").place(x=00, y=350)
        b1 = Button(top11, text="SET PASSWARD", command=setp, fg="white", bg="green", bd=5, height=2, width=64,
                    font="Verdana 10 bold italic").place(x=00, y=550)
        b2 = Button(top11, text="Go back", command=top11.destroy, fg="white", bg="red", bd=5, height=2, width=30,
                    font="Verdana 7 bold italic").place(x=150, y=620)

        top11.mainloop()
    except:
        messagebox.showinfo("ERROR", "ERROR")


def fun5():
    try:
        top7 = Toplevel()
        top7.geometry("1600x800+00+00")
        C = Canvas(top7, bg="black", height=250, width=300)
        filename = PhotoImage(file="C:\\Users\\vishwanath honawad\\Pictures\\Screenshots\\Screenshot (3).png")
        background_label = Label(top7, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.place()

        lb1 = Label(top7, text=" PLEASE ENTER YOUR ROOM NUMBER ", font="Verdana 10 bold italic").place(x=00, y=50)
        e1 = Entry(top7, width=30, textvariable=uprn, font="large_font").place(x=00, y=100)
        lb2 = Label(top7, text=" PLEASE ENTER THE NUMBER OF DAYS TO BE INCREASED ", font="Verdana 10 bold italic").place(x=00, y=150)
        e2 = Entry(top7, width=30, textvariable=nday, font="large_font").place(x=00, y=200)
        l2 = Label(top7, text=" PLEASE ENTER YOUR PASSWARD  :", fg="green",
                   font="Verdana 20 bold italic").place(x=00, y=250)
        e3 = Entry(top7, width=40, textvariable=psd,show='*', font="large_font").place(x=00, y=300)
        b1 = Button(top7, text="FORGOT PASSWARD", command=passwardset, fg="white", bg="red", bd=5, height=1, width=15,
                    font="Verdana 8 bold italic").place(x=200, y=350)
        b2 = Button(top7, text=" ENTER ", command=ft5, fg="white", bg="GREEN", height=2, width=20,
                    font="Verdana 10 bold italic").place(x=00, y=400)
        b3 = Button(top7, text="GO BACK", command=top7.destroy, fg="white", bg="RED", height=2, width=20,
                   font="Verdana 10 bold italic").place(x=00, y=500)
        top7.mainloop()
    except:
        messagebox.showinfo("ERROR", "ERROR")


def fun6():
    try:
        conn = sqlite3.connect('management.db')
        cur = conn.cursor()
        cur.execute("""select * from manage order by roomno """)
        r = cur.fetchall()
        if r == []:
            raise er
        top9 = Toplevel()
        top9.geometry("200x430+1200+200")
        T1 = Text(top9, height=24, width=12)
        T1.place(x=00, y=00)
        T2 = Text(top9, height=24, width=18)
        T2.place(x=100, y=00)
        T1.insert(END, "ROOM NUMBER\n____________\n")
        T2.insert(END, "PASSWARD\n______________\n")
        for row in r:
            T1.insert(END, str(row[0])+"\n____________\n")
            T2.insert(END, row[7]+"\n______________\n")
        conn.commit()

        b1 = Button(top9, text=" OKAY ", command=top9.destroy, fg="white", bg="GREEN", height=2, width=22,
                        font="Verdana 10 bold italic").place(x=00, y=390)

        cur.close()
        top9.mainloop()
    except er:
        messagebox.showinfo("ERROR", "NO ROOMS ARE OCCUPIED")
    except:
        messagebox.showinfo("ERROR", "ERROR")


def sfeed():
    try:
        s1=fe1.get()
        s2=fe2.get()
        s3=fe3.get()
        conn = sqlite3.connect('management.db')
        cur = conn.cursor()
        cur.execute("""select * from manage """)
        m = cur.fetchall()
        n=0
        for row in m:
            if s1==row[0] :
                n=1
                if s2!=row[7]:
                    raise en
        if n==0:
            raise er

        #cur.execute("""drop table  feedb """)

        cur.execute("create table if not exists  feedb(fnum int primary key, fb text,roomn int  references  manage (roomno)  ); ")
        cur.execute("""select * from feedb """)
        r = cur.fetchall()
        s=0
        for row in r:
            s=row[0]
        s=s+1
        query1 = "insert into feedb (fnum,fb,roomn) values(?,?,?) "
        data = (s,s3,s1)
        cur.execute(query1, data)

        conn.commit()
        messagebox.showinfo("FEEDBACK", "YOY HAVE SUCCESSFULLY GIVEN FEEDBACK")
        cur.close()
        conn.close()
    except en:
        messagebox.showinfo("ERROR", "PLEASE ENTER CORRECT PASSWORD")
    except er:
        messagebox.showinfo("ERROR", "YOU ARE NOT ACCESSED TO IT")
    except:
        messagebox.showinfo("ERROR", "ERROR")


def gfeed():
    try:
        topg = Toplevel()
        topg.geometry("1600x800+00+00")
        C = Canvas(topg, bg="black", height=250, width=300)
        filename = PhotoImage(file="C:\\Users\\vishwanath honawad\\Pictures\\Screenshots\\Screenshot (3).png")
        background_label = Label(topg, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.place()
        l1 = Label(topg, text=" ENTER YOUR ROOM NUMBER :", font="Verdana 15 bold italic").place(x=50, y=20)
        e1 = Entry(topg, width=17, textvariable=fe1, font="large_font").place(x=500, y=20)
        l2 = Label(topg, text=" ENTER YOUR PASSWORD :",font="Verdana 15 bold italic"    ).place(x=50,y=140)
        e2 = Entry(topg, width=17,textvariable=fe2 ,show="*",font="large_font"   ).place(x=500,y=140)
        l3 = Label(topg, text=" PLEASE GIVE THE FEEDBACK :",font="Verdana 15 bold italic"    ).place(x=50,y=260)
        e3 = Entry(topg, width=17,textvariable=fe3 ,font="large_font"   ).place(x=500,y=260)
        bt1 = Button(topg, text="SEND FEEDBACK", fg="white", bg="green", command=sfeed, bd=5, height=2, width=20,
                     font="Verdana 10 bold italic").place(x=100, y=365)
        bt2 = Button(topg, text="FORGOT PASSWORD", fg="white", bg="purple", command=passwardset, bd=5, height=2, width=20,
                     font="Verdana 10 bold italic").place(x=00, y=465)
        bt3 = Button(topg, text="GO BACK", fg="white", bg="red", command=topg.destroy, bd=5, height=2, width=20,
                     font="Verdana 10 bold italic").place(x=100, y=565)
        topg.mainloop()
    except:
        messagebox.showinfo("ERROR", "ERROR")

def feedback():
    try:
        topf = Toplevel()
        topf.geometry("1600x800+00+00")
        C = Canvas(topf, bg="black", height=250, width=300)
        filename = PhotoImage(file="C:\\Users\\vishwanath honawad\\Pictures\\Screenshots\\Screenshot (3).png")
        background_label = Label(topf, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.place()
        conn = sqlite3.connect('management.db')
        cur = conn.cursor()
        cur.execute("create table if not exists  feedb(fnum int primary key, fb text,roomn int  references  manage (roomno)  ); ")

        cur.execute("""select * from  manage,feedb where manage.roomno=feedb.roomn""")
        m = cur.fetchall()
        T1 = Text(topf, height=24, width=42)
        T1.place(x=00, y=00)
        for row in m:
            T1.insert(END, "ROOM NUMBER    :")
            T1.insert(END, str(row[0]) + "\n")
            T1.insert(END, "NAME           :")
            T1.insert(END,row[1]+"\n")
            T1.insert(END, "FEEDBACK       :")
            T1.insert(END,str(row[10])+"\n")
            T1.insert(END,"============================\n")

        bt1 = Button(topf, text="GIVE FEEDBACK", fg="white", bg="green", command=gfeed, bd=5, height=2, width=20,
                     font="Verdana 10 bold italic").place(x=00, y=425)
        bt2 = Button(topf, text="      GO BACK          ", fg="white", bg="red", command=topf.destroy, bd=5, height=2,
                     width=20,
                     font="Verdana 10 bold italic").place(x=260, y=425)
        topf.mainloop()
        conn.commit()
        cur.close()
        conn.close()
    except:
        messagebox.showinfo("ERROR", "ERROR")


lb1 = Label(root, text="WELCOME TO THE GOLDEN EDGE HOTEL!!!",bg="pink", fg="#444999",width=35,font="Verdana 30 bold italic").place(x=00,y=25)
mb2 = Label(root, text=" PLEASE SELECT THE DESIRED OPTION! ",bg="pink", fg="#333666",width=35,font="Verdana 16 bold ").place(x=200,y=100)
bt1 = Button(root, text="     CHECK INN      ",fg="white", bg="green",command=fun1,        bd=5,height=2, width=20,
             font="Verdana 10 bold italic").place(x=400,y=200)
bt2 = Button(root, text="DETAILS OF ALL GUEST",fg="white", bg="green",command=fun2,        bd=5,height=2, width=20,
             font="Verdana 10 bold italic").place(x=400,y=255)
bt3 = Button(root, text="     CHECK  OUT     ",fg="white", bg="green",command=fun3,        bd=5,height=2, width=20,
             font="Verdana 10 bold italic").place(x=400,y=310)
bt4 = Button(root, text="    FIND GUEST      ",fg="white", bg="green",command=fun4,        bd=5,height=2, width=20,
             font="Verdana 10 bold italic").place(x=400,y=365)
bt5 = Button(root,text="EXTEND NUMBER OF DAYS",fg="white", bg="green",command=fun5,        bd=5,height=2, width=20,
             font="Verdana 10 bold italic").place(x=400,y=425)
bt6 = Button(root, text="      EXIT          ",fg="white", bg="red"  ,command=root.destroy,bd=5,height=2, width=20,
             font="Verdana 10 bold italic").place(x=400,y=485)
bt7 = Button(root,text="ROOMS AND PASSWARDS ",fg="white",bg="#985634",command=fun6,        bd=5,height=1, width=20,
             font="Verdana 5 bold italic").place(x=00,y=750)

bt8 = Button(root, text="    FEEDBACK       ",fg="white", bg="purple",command=feedback,bd=5,height=2, width=20,
             font="Verdana 10 bold italic").place(x=400,y=545)
root.mainloop()