import os
os.system("cls")
from tkinter import *


raiz=Tk()
raiz.title("Proyecto final Intro")
raiz.resizable(10,10)
raiz.geometry("650x650")
raiz.config(background="grey")

miframe=Frame(raiz, width=1000, height=600)
miframe.config(bg="blue")
miframe.pack(side=LEFT, anchor=N)
usuario=StringVar()
clave=StringVar()
Titulo=Label(miframe,text="Programa Proyecto Intro David y Diego",font="80").place(x=15,y=10)

#miimagen=PhotoImage(file="frenguc.gif")
#imagen1=Label(miframe, image=miimagen).place(x=50, y=100)
#imagen2=Label(miframe, image=miimagen).place(x=545, y=100)

entrausuario=Entry(miframe,textvariable=usuario)
entrausuario.place(x=300,y=110)
entrausuario.config(fg="blue",justify="center",font="20")
user=Label(miframe,text="Usuario",font="20").place(x=200,y=110)

entraclave=Entry(miframe,textvariable=clave)
entraclave.place(x=300,y=160)
entraclave.config(show="*",fg="blue",justify="center",font="20")
clave=Label(miframe,text="Clave",font="20").place(x=200,y=160)

piedepag1=Label(miframe,text="Informacion 1 del provedor del programa",font="5").place(x=15,y=450)
piedepag1=Label(miframe,text="Correo electronico para soporte",font="5").place(x=15,y=475)
piedepag1=Label(miframe,text="Version 1.0 / 2023",font="5").place(x=15,y=500)


#def funentrar():
#    usuario=entrausuario.get()
#    clave=entraclave.get()



botonentrar=Button(miframe,text="Entrar") #command=funentrar)
botonentrar.config(fg="Black",font="50")
botonentrar.place(x=350,y=200)









raiz.mainloop()


## minuto 3:40 https://www.youtube.com/watch?v=oIzt6ESA7nU