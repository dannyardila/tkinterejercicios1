from tkinter import *
from tkinter import messagebox

#---------------------
# Funciones de la App
#---------------------

def sumar ():
    z=int(x.get())*(int(x.get())+1)/2
    t_resultado.insert(INSERT, "Resultado:\n El número "+x.get()+"  es igual = "+str(z)+"\n")

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
ventana_principal.title(" Numeros Enteros")

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
z=IntVar()


#---------------------
# Frame Entrada
#---------------------

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="green2", width=780, height=240)
frame_entrada.place(x=10,y=10)

titulo= Label(frame_entrada, text="Numero positivo")
titulo.config(bg="red", fg="black", font=("Arial", 20))
titulo.place(x=240,y=10)

subtitulo2= Label(frame_entrada, text="SUMA DE LOS PRIMEROS POSITIVOS")
subtitulo2.config(bg="dark green", fg="gold", font=("Arial", 15), anchor=CENTER)
subtitulo2.place(x=240,y=70)

logo= PhotoImage(file="Entero2.png")
etiq_logo=Label(frame_entrada, image=logo)
etiq_logo.config(bg="black")
etiq_logo.place(x=10,y=10)

etiq_a=Label(frame_entrada, text="ingrese numero:")
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
frame_operaciones.config(bg="red2", width=780, height=120)
frame_operaciones.place(x=10,y=260)


bt_sum= PhotoImage(file="sumarentero1.png")
bt_sumar= Button(frame_operaciones, image=bt_sum, width=105, height=105, command=sumar)
bt_sumar.place(x=116, y=7)


bt_bor= PhotoImage(file="borrarentero3.png")
bt_borrar= Button(frame_operaciones, image=bt_bor, width=105, height=105, command=borrar)
bt_borrar.place(x=337, y=7)


bt_sal= PhotoImage(file="salirentero.png")
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