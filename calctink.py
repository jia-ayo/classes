from tkinter import*

ttk=Tk()
ttk.geometry("354x460")
ttk.title("CALCULATOR")
melabel = Label(ttk,text="CALCULATOR",bg='dark gray',font=("Times",30,'bold'))
melabel.pack(side=TOP)
ttk.config(background='Dark gray')
   
metext=Entry(ttk,font=("Courier New",12,'bold'),width=25,bd=5,bg='powder blue')
metext.pack()

but1=Button(ttk,padx=10,pady=10,bd=4,bg='white',text="1",font=("Courier New",16,'bold'))
but1.place(x=10,y=100)

but2=Button(ttk,padx=10,pady=10,bd=4,bg='white',text="2",font=("Courier New",16,'bold'))
but2.place(x=10,y=170)

but3=Button(ttk,padx=10,pady=10,bd=4,bg='white',text="3",font=("Courier New",16,'bold'))
but3.place(x=10,y=240)

but4=Button(ttk,padx=10,pady=10,bd=4,bg='white',text="4",font=("Courier New",16,'bold'))
but4.place(x=75,y=100)

but5=Button(ttk,padx=10,pady=10,bd=4,bg='white',text="5",font=("Courier New",16,'bold'))
but5.place(x=75,y=170)

but6=Button(ttk,padx=10,pady=10,bd=4,bg='white',text="6",font=("Courier New",16,'bold'))
but6.place(x=75,y=240)

but7=Button(ttk,padx=14,pady=14,bd=4,bg='white',text="7",font=("Courier New",16,'bold'))
but7.place(x=140,y=100)

but8=Button(ttk,padx=10,pady=10,bd=4,bg='white',text="8",font=("Courier New",16,'bold'))
but8.place(x=140,y=170)

but9=Button(ttk,padx=14,pady=14,bd=4,bg='white',text="9",font=("Courier New",16,'bold'))
but9.place(x=140,y=240)

but0=Button(ttk,padx=14,pady=10,bd=4,bg='white',text="0",font=("Courier New",16,'bold'))
but0.place(x=10,y=310)

butdot=Button(ttk,padx=47,pady=10,bd=4,bg='white',text=".",font=("Courier New",16,'bold'))
butdot.place(x=75,y=310)

butpl=Button(ttk,padx=10,pady=10,bd=4,bg='white',text="+",font=("Courier New",16,'bold'))
butpl.place(x=205,y=100)

butsub=Button(ttk,padx=10,pady=10,bd=4,bg='white',text="-",font=("Courier New",16,'bold'))
butsub.place(x=205,y=170)

butml=Button(ttk,padx=10,pady=10,bd=4,bg='white',text="*",font=("Courier New",16,'bold'))
butml.place(x=205,y=240)

butdiv=Button(ttk,padx=10,pady=10,bd=4,bg='white',text="/",font=("Courier New",16,'bold'))
butdiv.place(x=205,y=310)

butclear=Button(ttk,padx=10,pady=119,bd=4,bg='white',text="CE",font=("Courier New",16,'bold'))
butclear.place(x=270,y=100)

butequal=Button(ttk,padx=151,pady=14,bd=4,bg='white', text="=",font=("Courier New",16,'bold'))
butequal.place(x=10,y=380)
ttk.mainloop()