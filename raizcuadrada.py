from tkinter import *
from tkinter import messagebox

#---------------------
# Funciones de la App
#---------------------

def sumar ():
    z=pow(int(n.get()),1/int(x.get()))
    t_resultado.insert(INSERT, "Resultados:\n La raiz es "+str(z)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados...")
    x.set("")
    n.set("")
    t_resultado.delete("1.0", "end")

def salir():
    messagebox.showinfo("Suma 1.0", "La App se cerrará...")
    ventana_principal.destroy()


#---------------------
# Ventana Principal
#---------------------

#Se declara una variable que llamamos ventana_principal y que adquiere las caracteristicas de un objeto Tk
ventana_principal=Tk()

#Titulo de la ventana
ventana_principal.title("Raiz cuadrada")

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
n=StringVar()
z=IntVar()

#---------------------
# Frame Entrada
#---------------------

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="white", width=780, height=240)
frame_entrada.place(x=10,y=10)

titulo= Label(frame_entrada, text="Raiz cuadrada de un número n")
titulo.config(bg="red", fg="black", font=("Times New Roman", 25))
titulo.place(x=240,y=5)

subtitulo2= Label(frame_entrada, text="Hallar la raíz X de un Número enésimo,\n")
subtitulo2.config(bg="yellow", fg="black", font=("Arial", 15), anchor=CENTER)
subtitulo2.place(x=240,y=70)

logo= PhotoImage(file="raizcuadradaicono1.png")
etiq_logo=Label(frame_entrada, image=logo)
etiq_logo.config(bg="ivory2")
etiq_logo.place(x=10,y=10)

logo1= PhotoImage(file="BUCARA1.png")
etiq_logo1=Label(frame_entrada, image=logo1)
etiq_logo1.config(bg="ivory2")
etiq_logo1.place(x=600,y=50)

etiq_a=Label(frame_entrada, text="Valor de (x): = ")
etiq_a.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
etiq_a.place(x=280, y=125)

entry_a=Entry(frame_entrada, width=7, textvariable=x)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=480,y=125)

etiq_b=Label(frame_entrada, text="Valor  N = ")
etiq_b.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
etiq_b.place(x=280, y=180)

entry_b=Entry(frame_entrada, width=7, textvariable=n)
entry_b.config(font=("Arial", 20), justify=CENTER)
entry_b.focus_set()
entry_b.place(x=480,y=155)


#---------------------
# Frame Operaciones
#---------------------

frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="blue", width=780, height=120)
frame_operaciones.place(x=10,y=260)


bt_sum= PhotoImage(file="raizopera.png")
bt_sumar= Button(frame_operaciones, image=bt_sum, width=105, height=105, command=sumar)
bt_sumar.place(x=116, y=7)


bt_bor= PhotoImage(file="borrarraiz2.png")
bt_borrar= Button(frame_operaciones, image=bt_bor, width=105, height=105, command=borrar)
bt_borrar.place(x=337, y=7)


bt_sal= PhotoImage(file="raizsalir1.png")
bt_salir= Button(frame_operaciones, image=bt_sal, width=105, height=105, command=salir)
bt_salir.place(x=585, y=7)


#---------------------
# Frame Resultados
#---------------------

frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="black", width=780, height=100)
frame_resultados.place(x=10,y=390)

t_resultado=Text(frame_resultados, width=77, height=5)
t_resultado.config(bg="red", fg="white", font=("Arial", 15))
t_resultado.pack(expand=True)


ventana_principal.mainloop()