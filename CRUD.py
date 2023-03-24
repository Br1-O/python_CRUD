from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

###############################################################################################################################################
#Tkinter GUI - Root, Frame, Labels y Entries:
###############################################################################################################################################

#Deficiones del Root:
root=Tk()
root.title("Base de Datos · Clientes v1.0")
root.geometry("1000x1050")
root.configure(background="#9090ff")
# root.iconbitmap(r"E:\Python - Projects\Proyecto 415 - 2.0\Images\com_93620.ico")

#Main Frame:
mainFrame = LabelFrame(root, text= """  Ingrese los datos del cliente:  """, fg="#3030ff", padx=5, pady=5, bg="#ffffff", borderwidth=5, bd=5, font=("", 13))
mainFrame.grid(row=1, column=0, pady=15, padx=(150,0))

#Notifications Frame:
notificationFrame = LabelFrame(root, fg="#3030ff", padx=5, pady=5, borderwidth=5, bg="#ffffff", bd=5, font=("", 13))
notificationFrame.grid(row=2,column=0, pady=10, padx=(150,0))

#Selector Frame:
secondFrame = LabelFrame(root, text= """  Ingrese nombre completo o ID del cliente:  """, fg="#3030ff", padx=5, pady=5, borderwidth=5, bg="#ffffff", bd=5, font=("", 13))
secondFrame.grid(row=3, column=0, pady=10, padx=(150,0))

#Data Frame:
thirdFrame = LabelFrame(root, text= """  Los datos en el registro de ese cliente son:  """, fg="#3030ff", padx=5, pady=5, borderwidth=5, bg="#ffffff", bd=5, font=("", 13))
thirdFrame.grid(row=4, column=0, pady=5,padx=(150,0))

#Etiquetas del Formulario de Entrada:

Fecha= Label(mainFrame, text="Fecha:", fg=("#3030ff"), bg=("#fff"), font=("", 11))
Fecha.grid(row=0, column=0, pady=(20,10))

Nombre= Label(mainFrame, text="Nombre:", fg=("#3030ff"), bg=("#fff"), font=("", 11))
Nombre.grid(row=1, column=0, pady=10)

Telefono= Label(mainFrame, text="Telefono:", fg=("#3030ff"), bg=("#fff"), font=("", 11))
Telefono.grid(row=2, column=0, pady=10)

Gb= Label(mainFrame, text="Gb:", fg=("#3030ff"), bg=("#fff"), font=("", 11))
Gb.grid(row=3, column=0, pady=10)

Localidad= Label(mainFrame, text="Localidad:", fg=("#3030ff"), bg=("#fff"), font=("", 11))
Localidad.grid(row=4, column=0, pady=10)

PinDni= Label(mainFrame, text="PinDni:", fg=("#3030ff"), bg=("#fff"), font=("", 11))
PinDni.grid(row=5, column=0, pady=10)

Observaciones= Label(mainFrame, text="Observaciones:", fg=("#3030ff"), bg=("#fff"), font=("", 11))
Observaciones.grid(row=6, column=0, pady=10)

# Formulario de Entrada:
fecha= Entry(mainFrame, width=50, fg="#3030ff", borderwidth=2, font=("", 11))
fecha.grid(row=0, column=1, padx=20, pady=(20, 10), ipadx=50)

nombre= Entry(mainFrame, width=50, fg="#3030ff", borderwidth=2, font=("", 11))
nombre.grid(row=1, column=1, padx=20, pady= 10, ipadx=50)

telefono= Entry(mainFrame, width=50, fg="#3030ff", borderwidth=2, font=("", 11))
telefono.grid(row=2, column=1, padx=20, pady=10, ipadx=50)

gb= Entry(mainFrame, width=50, fg="#3030ff", borderwidth=2, font=("", 11))
gb.grid(row=3, column=1, padx=20, pady=10, ipadx=50)

localidad= Entry(mainFrame, width=50, fg="#3030ff", borderwidth=2, font=("", 11))
localidad.grid(row=4, column=1, padx=20, pady=10, ipadx=50)

pinDni= Entry(mainFrame, width=50, fg="#3030ff", borderwidth=2, font=("", 11))
pinDni.grid(row=5, column=1, padx=20, pady=10, ipadx=50)

observaciones= Entry(mainFrame, width=50, fg="#3030ff", borderwidth=2, font=("", 11))
observaciones.grid(row=6, column=1, padx=20, pady=10, ipadx=50)

#Entry del selector:
selector= Entry(secondFrame, width=40, fg="#3030ff", borderwidth=2, font=("", 11))
selector.grid(row=0, column=1, padx=20, pady= (20, 10), ipadx=30, columnspan=1)

###############################################################################################################################################
#Funciones de Widgets - Base de datos:
###############################################################################################################################################

#Crear base de datos:

#Crear/Conectar a la base de datos:
# conn = sqlite3.connect("clientes_db.db")
# #Crear Cursor:
# c = conn.cursor()   

# # #Crear Tabla de "clientes":
# c.execute("""CREATE TABLE clientes (
#     Fecha text,
#     Nombre text,
#     Telefono text,
#     Gb text,
#     Localidad text,
#     PinDni text,
#     Observaciones text
# )""")

# #Guardar Cambios a la Base de Datos:
# conn.commit()
# #Cerrar Conexión a la Base de Datos:
# conn.close()

#Función Submit:

def submit():

    #Validaciones de entries:
    fechaS=fecha.get()
    nombreS= (nombre.get().lower()).title()
    telefonoS= telefono.get()
    gbS=(gb.get().lower()).capitalize()
    localidadS= (localidad.get().lower()).capitalize()
    pinDniS=(pinDni.get())
    observacionesS=(observaciones.get().lower()).capitalize()
    
   

    if ((nombreS.replace(" ", "")).isalpha()==FALSE or (localidadS.replace(" ", "").replace("-", "")).isalpha()==FALSE):

        notificationFrame.grid(row=2,column=0, pady=10)

        error1= Label(notificationFrame, text="El nombre y/o localidad contienen un número y/o caracter invalido. Por favor, ingreselo nuevamente.", fg=("#fff"), bg=("#f00"), font=("", 12))
        error1.grid(row=6, column=0, pady= 20, columnspan=2)
        root.after(3500, lambda:error1.grid_forget())
        root.after(3500, lambda:notificationFrame.grid_forget())

    #ESTA ANDANDO MAL LA VALIDACIÓN TELEFONO

    elif((((((telefonoS.replace("+","0")).replace("-","0")).isdigit())==FALSE) or (((fechaS.replace("/","0")).replace("-","0")).isdigit()))==FALSE):

        notificationFrame.grid(row=2,column=0, pady=10)

        error2= Label(notificationFrame, text="El telefono y fecha deben disponer de sólo caracteres númericos y /, -, \. Por favor, ingreselos nuevamente.", fg=("#fff"), bg=("#f00"), font=("", 12))
        error2.grid(row=7, column=0, pady= 20, columnspan=2)
        root.after(3500, lambda:error2.grid_forget())
        root.after(3500, lambda:notificationFrame.grid_forget())

    #Conexión a base de datos, ingreso, y mensaje de confirmación:

    else:

        # Crear/Conectar a la base de datos:
        conn = sqlite3.connect("clientes_db.db")

        #Crear Cursor:
        c = conn.cursor()   

        #Insertar a la Tabla "empleados":
        c.execute("""INSERT INTO clientes VALUES (
            :fecha,
            :nombre,
            :telefono,
            :gb,
            :localidad,
            :pinDni,
            :observaciones)""",
            {
            "fecha":fechaS,
            "nombre":nombreS,
            "telefono":telefonoS,
            "gb":gbS,
            "localidad":localidadS,
            "pinDni":pinDniS,
            "observaciones":observacionesS
            })

        #Guardar Cambios a la Base de Datos:
        conn.commit()

        #Cerrar Conexión a la Base de Datos:
        conn.close()

        #limpiar casillas de formulario tras submit:
        fecha.delete(0, END)      
        nombre.delete(0, END)
        telefono.delete(0, END)
        gb.delete(0, END)
        localidad.delete(0, END)
        pinDni.delete(0, END)
        observaciones.delete(0, END)

        #Mensaje de confirmaciòn para el usuario:
        notificationFrame.grid(row=2,column=0, pady=10)

        confirmation= Label(notificationFrame, text=f"¡Cliente cargado con exito!", fg=("#fff"), bg=("#0f0"), font=("", 12))
        confirmation.grid(row=6, column=0, pady= 20, columnspan=2)
        root.after(4000, lambda:confirmation.grid_forget())
        root.after(3500, lambda:notificationFrame.grid_forget())

#Función para mostrar todo el contenido de la Tabla empleados en una nueva ventana:

def mostrarTodo():

    #Abre nueva ventana para modificar datos:
    mostrarTodoV=Tk()
    mostrarTodoV.title("Base de Datos · Clientes v1.0")
    mostrarTodoV.geometry("900x900")
    mostrarTodoV.configure(background="#9090ff")
    # mostrarTodoV.iconbitmap(r"E:\Python - Projects\Proyecto 415 - 2.0\Images\accessories-text.ico")

    ###############################################################################################################################################
    #Scrollbar:
    ###############################################################################################################################################
    
    #Crear Frame:
    mostrarTFrame= LabelFrame(mostrarTodoV, fg="#3030ff", padx=5, pady=5, borderwidth=5, bg="#ffffff", bd=5, font=("", 13))
    mostrarTFrame.pack(pady=10, padx=5, fill=BOTH, expand=1)

    #Crear Canvas en Frame:
    canvas= Canvas(mostrarTFrame, bg="#9090ff")
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    #Agregar ScrollBar al Canvas:
    scrollbar1= ttk.Scrollbar(mostrarTFrame, orient=VERTICAL, command=canvas.yview)
    scrollbar1.pack(side=RIGHT,fill=Y)

    #Configurar Canvas:
    canvas.configure(yscrollcommand=scrollbar1.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    #Crear mainFrame dentro del Canvas:
    mainFrameMostrar = LabelFrame(canvas, text= """  Estos son los datos de todos los empleados registrados:  """, fg="#3030ff", padx=10, pady=20, bg="#ffffff", borderwidth=5, bd=5, font=("", 13))

    #Agregar un nuevo Frame a una ventana dentro del Canvas:
    canvas.create_window((0,0), window=mainFrameMostrar, anchor="nw")

    ###############################################################################################################################################
    ###############################################################################################################################################

    #Agregar ScrollBarX al Canvas:
    scrollbar2= ttk.Scrollbar(mostrarTFrame, orient=HORIZONTAL, command=canvas.xview)
    scrollbar2.pack(side=BOTTOM,fill=X)

    #Configurar Canvas:
    canvas.configure(yscrollcommand=scrollbar1.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    ###############################################################################################################################################
    ###############################################################################################################################################

    # Crear/Conectar a la base de datos:
    conn = sqlite3.connect("clientes_db.db")

    #Crear Cursor:
    c = conn.cursor()   

    #Insertar a la Tabla "empleados":
    c.execute("SELECT *, oid FROM clientes")

    #Mostrar registro en la pantalla:
    registros = c.fetchall()

    printRegistro=""
    
    for registro in registros:
            printRegistro += "\n" + str(registro) + "\n"

    registros= Label(mainFrameMostrar, text=printRegistro, bg="#fff", fg="#3030ff", font=("Arial", 17))
    registros.grid(row=5,column=0, columnspan=2)

    #Guardar Cambios a la Base de Datos:
    conn.commit()

    #Cerrar Conexión a la Base de Datos:
    conn.close()
      
    #Boton Cerrar:
    btnCerrar= Button(mainFrameMostrar, text="Cerrar Ventana", width=50, bg="#8080ff", fg="#fff", borderwidth=2, font=("", 11), command= lambda:mostrarTodoV.destroy())
    btnCerrar.grid(row=6, column=0, padx=10, pady=20, ipadx=40, columnspan=3)

#Función para mostrar todos los datos de un solo empleado en la misma ventana:

def mostrar():

    root.geometry("890x990")
    thirdFrame.grid(row=4, column=0, pady=5, padx=10)

    # #Data Frame:
    # thirdFrame = LabelFrame(root, text= """  Los datos en el registro de ese empleado son:  """, fg="#3030ff", padx=5, pady=5, borderwidth=5, bg="#ffffff", bd=5, font=("", 13))
    # thirdFrame.grid(row=4, column=0, pady=5, padx=10)

    # Limpiar el calleo previo de la función:
    registro= Label(thirdFrame, text="", bg="#fff", fg="#3030ff", font=("Arial", 1))
    registro.grid(row=5,column=0)
    
    # Crear/Conectar a la base de datos:
    conn = sqlite3.connect("clientes_db.db")

    #Crear Cursor:
    c = conn.cursor()   

    #Validación de entry:
    nombreS= (selector.get().lower()).title()

    #Seleccionar de la Tabla "empleados":

    #En base al Id:
    if ((nombreS).isdigit()):
        c.execute("SELECT *, oid FROM clientes WHERE oid=?", (nombreS,))
        #Mostrar registro unico por Id en la pantalla:
        registro = c.fetchone()
        printRegistro=""
        categorias=("""      Fecha: """, """    Nombre: """, """  Telefono: """, """    Gb: ""","""      Localidad: """, """    Pin-Dni: """, """  Observaciones: """)

        for propiedad, i in zip(registro, categorias) :
            printRegistro += i + str(propiedad) + "\n"

        registros= Label(thirdFrame, text=printRegistro, bg="#fff", fg="#3030ff", font=("Arial", 17))
        registros.grid(row=5,column=0, columnspan=2)

    #En base al Nombre:
    elif((nombreS.replace(" ", "")).isalpha() or (" " in nombreS)):
        c.execute("SELECT *, oid FROM clientes WHERE Nombre=?", (nombreS,))
        #Mostrar registro multiple en base a nombre compartido en la pantalla:
        registro = c.fetchmany(50)

        printRegistro=""

        for propiedad in (registro) :
            printRegistro += str(propiedad) + "\n"

        registros= Label(thirdFrame, text=printRegistro, bg="#fff", fg="#3030ff", font=("Arial", 17))
        registros.grid(row=5,column=0, columnspan=2)
  
    #Guardar Cambios a la Base de Datos:
    conn.commit()

    #Cerrar Conexión a la Base de Datos:
    conn.close()

    #Función Resize y Boton Cerrar:
    def resize():
        thirdFrame.grid_forget()
        root.geometry("700x950")
    
    btnCerrar= Button(thirdFrame, text="Cerrar Datos", width=50, bg="#8080ff", fg="#fff", borderwidth=2, font=("", 11), command= resize)
    btnCerrar.grid(row=6, column=0, padx=10, pady=20, ipadx=20, columnspan=2)

    # #limpiar casillas de formulario tras submit:
    # selector.delete(0, END)

#Función para modificar los datos de un empleado, abriendo una nueva ventana, y su función auxiliar:

# def modificar2():

#     # Crear/Conectar a la base de datos:
#     conn = sqlite3.connect("empleados_db.db")

#     #Crear Cursor:
#     c = conn.cursor()   

#     #Insertar cambios a la Tabla de "empleados":
#     empleadoId= selector.get()

#     sql= "UPDATE empleados SET nombre= :nombre, cargo= :cargo, salario= :salario, antigüedad= :antiguedad WHERE oid = :oid"

#     c.execute(sql,{
#         "nombre": nombreEditor.get(),
#         "cargo": cargoEditor.get(),
#         "salario": salarioEditor.get(),
#         "antiguedad": antiguedadEditor.get(),
#         "oid": empleadoId
#         })
    
#     # sql= "UPDATE empleados SET nombre=?, cargo=?, salario=?, antigüedad=? WHERE oid =?"

#     # c.execute(sql,(
#     #     nombreEditor.get(),
#     #     cargoEditor.get(),
#     #     salarioEditor.get(),
#     #     antiguedadEditor.get(),
#     #     empleadoId
#     #     ))
    
#     #Guardar Cambios a la Base de Datos:
#     conn.commit()

#     #Cerrar Conexión a la Base de Datos:
#     conn.close()

#     #Cerrar Ventana de Modificación de Datos tras uso:
#     modificarV.destroy()

#     #Mensaje de confirmaciòn para el usuario:
#     notificationFrame.grid(row=2,column=0, pady=10)

#     confirmation= Label(notificationFrame, text="""        
#                           ¡Empleado modificado con exito!                                  
#                                                                              """, fg=("#fff"), bg=("#0f0"), font=("", 12))
#     confirmation.grid(row=6, column=0, pady= 20, ipadx=40, columnspan=2)
#     root.after(4000, lambda:confirmation.grid_forget())
#     root.after(3500, lambda:notificationFrame.grid_forget())

# def modificar():

#     #Abre nueva ventana para modificar datos:
#     global modificarV
#     modificarV=Tk()
#     modificarV.title("Base de Datos · Empleados v2.0")
#     modificarV.geometry("650x300")
#     modificarV.configure(background="#9090ff")
#     # modificarV.iconbitmap(r"E:\Python - Projects\Proyecto 415 - 2.0\Images\texteditor.ico")

#     #mainFrame:
#     mainFrameEditor = LabelFrame(modificarV, text= """  Modifique los datos del empleado:  """, fg="#3030ff", padx=5, pady=5, bg="#ffffff", borderwidth=5, bd=5, font=("", 13))
#     mainFrameEditor.pack(pady=(15,10), padx=10)

#     #Etiquetas del Formulario de Entrada:
#     Nombre= Label(mainFrameEditor, text="Nombre:", fg=("#3030ff"), bg=("#fff"), font=("", 11))
#     Nombre.grid(row=0, column=0, pady= (20, 0))

#     Cargo= Label(mainFrameEditor, text="Cargo:", fg=("#3030ff"), bg=("#fff"), font=("", 11))
#     Cargo.grid(row=1, column=0, pady=10)

#     Salario= Label(mainFrameEditor, text="Salario:", fg=("#3030ff"), bg=("#fff"), font=("", 11))
#     Salario.grid(row=2, column=0, pady=10)

#     Antiguedad= Label(mainFrameEditor, text="Antigüedad:", fg=("#3030ff"), bg=("#fff"), font=("", 11))
#     Antiguedad.grid(row=3, column=0, pady=10)

#     # Formulario de Entrada:
#     global nombreEditor
#     nombreEditor= Entry(mainFrameEditor, width=50, fg="#3030ff", borderwidth=2, font=("", 11))
#     nombreEditor.grid(row=0, column=1, padx=20, pady= (20, 0), ipadx=50)

#     global cargoEditor
#     cargoEditor= Entry(mainFrameEditor, width=50, fg="#3030ff", borderwidth=2, font=("", 11))
#     cargoEditor.grid(row=1, column=1, padx=20, pady=10, ipadx=50)

#     global salarioEditor
#     salarioEditor= Entry(mainFrameEditor, width=50, fg="#3030ff", borderwidth=2, font=("", 11))
#     salarioEditor.grid(row=2, column=1, padx=20, pady=10, ipadx=50)

#     global antiguedadEditor
#     antiguedadEditor= Entry(mainFrameEditor, width=50, fg="#3030ff", borderwidth=2, font=("", 11))
#     antiguedadEditor.grid(row=3, column=1, padx=20, pady=10, ipadx=50)

#     #Boton Modificar:
#     btnSelectorModificar= Button(mainFrameEditor, text="Modificar Datos", width=50, bg="#8080ff", fg="#fff", borderwidth=2, font=("", 11), command=modificar2)
#     btnSelectorModificar.grid(row=4, column=0, padx=10, pady=10, ipadx=40, columnspan=3)
        
#     # Crear/Conectar a la base de datos:
#     conn = sqlite3.connect("empleados_db.db")

#     #Crear Cursor:
#     c = conn.cursor()   

#     #Insertar desde la Tabla de "empleados":
#     IdNombre= selector.get()

#     c.execute("SELECT * FROM empleados WHERE oid=" + IdNombre)

#     registros = c.fetchall()
    
#     for registro in registros:
#         nombreEditor.insert(0, registro[0])
#         cargoEditor.insert(0, registro[1])
#         salarioEditor.insert(0, registro[2])
#         antiguedadEditor.insert(0, registro[3])
    
#     #Guardar Cambios a la Base de Datos:
#     conn.commit()

#     #Cerrar Conexión a la Base de Datos:
#     conn.close()

#     #limpiar casillas de formulario tras submit:
#     selector.delete(0, END)

#Función para borrar del registro por completo todos los datos de un empleado:

def borrar():

    #Pop-up de confirmación:
    borrar= messagebox.askquestion("¿Borrar este cliente?", f"Está seguro que desea eliminar al cliente de id:{selector.get()} del registro?")

    if (borrar=="yes"):
    
        # Crear/Conectar a la base de datos:
        conn = sqlite3.connect("clientes_db.db")

        #Crear Cursor:
        c = conn.cursor()   

        #Validación de entry:
        nombreS= (selector.get().lower()).title()

        #Seleccionar de la Tabla "empleados":

        #En base al Id:
        if ((nombreS).isdigit()):   
            #Borrar empleado de la Tabla "empleados":
            c.execute("DELETE from clientes WHERE + oid=" + selector.get())
            
        #En base al Nombre:
        elif((nombreS.replace(" ", "")).isalpha() or (" " in nombreS)):

            #Borrar empleado de la Tabla "empleados":
            c.execute("DELETE from clientes WHERE + oid=" + nombreS)

        #Guardar Cambios a la Base de Datos:
        conn.commit()

        #Cerrar Conexión a la Base de Datos:
        conn.close()

        #limpiar casilla de formulario de selección:
        selector.delete(0, END)

        #Mensaje de confirmaciòn para el usuario:
        notificationFrame.grid(row=2,column=0, pady=10)

        confirmation= Label(notificationFrame, text="""        
                            ¡Cliente eliminado con exito!                                  
                                                                                """, fg=("#fff"), bg=("#0f0"), font=("", 12))
        confirmation.grid(row=6, column=0, pady= 20, ipadx=40, columnspan=2)
        root.after(4000, lambda:confirmation.grid_forget())
        root.after(3500, lambda:notificationFrame.grid_forget())

#Función para pop-up de confirmación de cierre de aplicación:
def alCerrar():
    if messagebox.askokcancel("Salir", "¿Está seguro que desea salir?"):
        root.destroy()
root.protocol("WM_DELETE_WINDOW", alCerrar)

###############################################################################################################################################
#Tkinter GUI - Botones:
###############################################################################################################################################

#Boton de Submit:
btnSubmit= Button(mainFrame, text="Guardar Datos", width=50, bg="#8080ff", fg="#fff", borderwidth=2, font=("", 11), command=submit)
btnSubmit.grid(row=7, column=0, padx=10, pady=15, ipadx=40, columnspan=2)

#Boton Mostrar Todo:
btnSelectorMostrar= Button(mainFrame, text="Mostrar Registro Completo", width=50, bg="#8080ff", fg="#fff", borderwidth=2, font=("", 11), command=mostrarTodo)
btnSelectorMostrar.grid(row=8, column=0, padx=10, pady=10, ipadx=40, columnspan=2)

#Boton Mostrar:
btnSelectorMostrar= Button(secondFrame, text="Mostrar Datos", width=50, bg="#8080ff", fg="#fff", borderwidth=2, font=("", 11), command=mostrar)
btnSelectorMostrar.grid(row=2, column=0, padx=10, pady=10, ipadx=40, columnspan=3)

# #Boton Modificar:
# btnSelectorModificar= Button(secondFrame, text="Modificar Datos", width=50, bg="#8080ff", fg="#fff", borderwidth=2, font=("", 11), command=modificar)
# btnSelectorModificar.grid(row=3, column=0, padx=10, pady=10, ipadx=40, columnspan=3)

#Boton Borrar:
btnSelectorBorrar= Button(secondFrame, text="Borrar del Registro", width=50, bg="#8080ff", fg="#fff", borderwidth=2, font=("", 11), command=borrar)
btnSelectorBorrar.grid(row=4, column=0, padx=10, pady=10, ipadx=40, columnspan=3)

###############################################################################################################################################

#Ejecución de la Pantalla del Usuario:
root.mainloop()

