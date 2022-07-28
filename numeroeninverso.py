from tkinter import *
from tkinter import messagebox

#---------------------
# Funciones de la App
#---------------------

def sumar ():
    a=int(x.get())%10
    a1=int(x.get())//10
    a2=a*1000
    b=a1%10
    b1=a1//10
    b2=b*100
    c=b1%10
    c1=b1//10
    c2=c*10

    z=a2+b2+c2+c1

    t_resultado.insert(INSERT, "Resultado:\n El número "+str()+" a la inversa es "+str(z)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados...")
    x.set("")
    t_resultado.delete("1.0", "end")

def salir():
    messagebox.showinfo("Suma 1.0", "La App se cerrará...")
    ventana_principal.destroy()


#---------------------
# Ventana Principal
#---------------------

#Se declara una varaiable que llamamos ventana_principal y que adquiere las caracteristicas de un objeto Tk
ventana_principal=Tk()

#Titulo de la ventana
ventana_principal.title("")

#Establecer tamaño a la pantalla
ventana_principal.geometry("800x500")

#Icono de la ventana principal

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#Color de fondo de la ventana principal
ventana_principal.config(bg="snow")

#---------------------
# Variables Globales
#---------------------  
x=StringVar()
a=IntVar()
a1=IntVar()
a2=IntVar()

b=IntVar()
b1=IntVar()
b2=IntVar()

c=IntVar()
c1=IntVar()
c2=IntVar()
z=IntVar()

#---------------------
# Frame Entrada
#---------------------

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="black", width=780, height=240)
frame_entrada.place(x=10,y=10)

titulo= Label(frame_entrada, text="Número Inverso")
titulo.config(bg="red", fg="white", font=("Arial", 20))
titulo.place(x=240,y=10)

subtitulo2= Label(frame_entrada, text="Devolver número de 4 digitos inverso\n")
subtitulo2.config(bg="dark green", fg="gold", font=("Arial", 15), anchor=CENTER)
subtitulo2.place(x=240,y=70)

logo= PhotoImage(file="inversoicono.png")
etiq_logo=Label(frame_entrada, image=logo)
etiq_logo.config(bg="black")
etiq_logo.place(x=10,y=10)

etiq_a=Label(frame_entrada, text="Número de 4 dígitos = ")
etiq_a.config(bg="red", fg="white", font=("Arial", 20), anchor=CENTER)
etiq_a.place(x=240, y=130)

entry_a=Entry(frame_entrada, width=7, textvariable=x)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=530,y=130)


#---------------------
# Frame Operaciones
#---------------------

frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="blue", width=780, height=120)
frame_operaciones.place(x=10,y=260)


bt_sum= PhotoImage(file="sumarinverso.png")
bt_sumar= Button(frame_operaciones, image=bt_sum, width=105, height=105, command=sumar)
bt_sumar.place(x=116, y=7)


bt_bor= PhotoImage(file="borrarinverso.png")
bt_borrar= Button(frame_operaciones, image=bt_bor, width=105, height=105, command=borrar)
bt_borrar.place(x=337, y=7)


bt_sal= PhotoImage(file="salirinverso.png")
bt_salir= Button(frame_operaciones, image=bt_sal, width=105, height=105, command=salir)
bt_salir.place(x=585, y=7)


#---------------------
# Frame Resultados
#---------------------

frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="blue2", width=780, height=100)
frame_resultados.place(x=10,y=390)

t_resultado=Text(frame_resultados, width=77, height=5)
t_resultado.config(bg="blue2", fg="white", font=("Arial", 22))
t_resultado.pack(expand=True)


ventana_principal.mainloop()