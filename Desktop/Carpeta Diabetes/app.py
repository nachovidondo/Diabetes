from tkinter import*
import datetime
import locale
from datetime import datetime
from tkinter import messagebox
from consulta import *
from tkinter import*
from datetime import datetime
from tkinter.ttk import Treeview
from consulta import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import tkinter.ttk as ttk

app=Tk()
app.geometry("600x450")
app.iconbitmap("corazon.ico")
app.title("Sistema de Control Personalizado")
app.resizable(height = False, width = False)

def nuevo():
    txt_glucemia.config(state='normal')
    txt_tensionSistolica.config(state='normal')
    txt_tensionDiastolica.config(state='normal')
    
def persist(savedTime, txtGlucemia, txtTensionSistolica, txtTensionDiastolica):
    dbConnection = Conect()
    print("Conexion : ", dbConnection.con)
    dbConnection.insertData(savedTime, txtGlucemia, txtTensionSistolica, txtTensionDiastolica)
    
    
    
def guardar():
    txtGlucemia = txt_glucemia.get()
    txtTensionSistolica = txt_tensionSistolica.get()
    txtTensionDiastolica = txt_tensionDiastolica.get()
    
    if (int(txtGlucemia) > 500) or (int(txtGlucemia )<20):
         messagebox.showinfo("Error numerico ", " Verifique su Glucemia ")
    
    elif (int(txtTensionSistolica)> 200 ) or (int(txtTensionSistolica) <80) or (int(txtTensionDiastolica)> 200 ) or (int(txtTensionDiastolica) <80):
        message:" Verifique su Tension Arterial "
        messagebox.showinfo("Error numerico ", " Verifique su Tension Arterial ")
        
    else:
        message = "Glucemia: " + txtGlucemia + "mg/dl" + '\n' +'\n' + "Tension Arterial : " + txtTensionSistolica + "/"+ txtTensionDiastolica + "mmHg"
        messagebox.showinfo("Resultados  registrados : " , message)
        savedtime= currentDate + currentTime
        persist(savedtime,txtGlucemia, txtTensionSistolica, txtTensionDiastolica)
        
    
def showInfo():
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM CONTROL")
        data = (row for row in cursor.fetchall())

        ventana = tk.Tk()
        table = Table(ventana, headings=('N° CONTROL','Fecha', 'NIVEL GLUCEMICO','TENSION ARTERIAL(SISTOLICA)','TENSION ARTERIAL (DIASTOLICA'), rows=data)
        table.pack(expand=tk.YES, fill=tk.BOTH)

imagen=PhotoImage(file="tension.png")
label_imagen=Label(app,image=imagen)
label_imagen.pack()

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

dateTimeNow = datetime.now()
currentDate = dateTimeNow.strftime("%A %d, %B %Y")
currentTime = dateTimeNow.strftime("%I:%M %p")

label_HoraFecha=Label(app,text=str (currentDate)+ "    " + (currentTime))
label_HoraFecha.place(x = 350, y = 10)
label_HoraFecha.config(bg = "white", fg = "black", fon = ("Century Schoolbook",10))

label_glucemia=Label(app,text="Ingrese su Registro Glucemico ( mg/dl)")
label_glucemia.pack()
label_glucemia.config(bg="white", fg = "black", fon = ("Arial Rounded MT Bold",10))
label_glucemia.place(x = 20, y = 150)
                     
label_tensionSistolica=Label(app,text="Ingrese la tension sistolica Arterial (mmHg) ")
label_tensionSistolica.pack()
label_tensionSistolica.config(bg="white", fg = "black", fon = ("Arial Rounded MT Bold",10))
label_tensionSistolica.place(x=20, y = 200)

label_tensionDiastolica=Label(app,text="Ingrese la tension diastolica Arterial (mmHg) ")
label_tensionDiastolica.pack()
label_tensionDiastolica.config(bg="white", fg = "black", fon = ("Arial Rounded MT Bold",10))
label_tensionDiastolica.place(x=20, y = 250)

txt_glucemia = Entry(app)
txt_glucemia.place(x = 350, y = 150)
txt_glucemia.config(state='readonly')

txt_tensionSistolica= Entry(app)
txt_tensionSistolica.place( x = 350, y = 200)
txt_tensionSistolica.config(state='readonly')

txt_tensionDiastolica= Entry(app)
txt_tensionDiastolica.place( x = 350, y = 250)
txt_tensionDiastolica.config(state='readonly')


boton_nuevo=Button(app, text = "Nuevo Registro",command=nuevo)
boton_nuevo.config(bg="white", fg = "black", fon = ("Arial Rounded MT Bold",10))
boton_nuevo.place( x= 250, y = 400)

boton_guardar=Button(app, text = "Guardar ",command=guardar)
boton_guardar.config(bg="white", fg = "black", fon = ("Arial Rounded MT Bold",10))
boton_guardar.place( x= 400, y = 400)

menuMostrar=Menu(app)
app.config(menu=menuMostrar)
Mostrarmenu=Menu(menuMostrar,tearoff=0)
menuMostrar.add_cascade(label="Menu",menu = Mostrarmenu)

Mostrarmenu.add_command(label="Mostrar Datos",command=showInfo)
Mostrarmenu.add_separator

class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)
  
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings
  
        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)
  
        for row in rows:
            table.insert('', tk.END, values=tuple(row))
  
        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)


app.mainloop()