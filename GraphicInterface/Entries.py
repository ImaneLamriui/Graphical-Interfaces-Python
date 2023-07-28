#https://www.tutorialspoint.com/python/tk_entry.htm
#widgets entry 
#estilos: https://www.pythontutorial.net/tkinter/tkinter-frame/


from tkinter import *
raiz = Tk()
raiz.iconbitmap("cattt.ico")
raiz.title("Widget")
raiz.config(bg="purple")
raiz.resizable(1,1)

miFrame = Frame(raiz, width=800, height=1200)
miFrame['borderwidth'] = 5
miFrame['relief'] = 'sunken'

#miFrame.pack(fill="y", expand="True")
# int : IntVar()
minombre = StringVar()

miFrame.place(x=80, y=100)
miFrame.config(relief="groove", pady=20)
cuadroNombre = Entry(miFrame, textvariable = minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="blue",justify="left",font=("", 14))

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=10)
cuadroApellido.config(fg="blue",justify="left", font=("", 14))

cuadroPassword = Entry(miFrame)
cuadroPassword.grid(row=2, column=1, padx=10, pady=10)
cuadroPassword.config(fg="blue",justify="left",font=("", 14))
cuadroPassword.config(show="*")

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)
cuadroDireccion.config(fg="blue",justify="left",font=("", 14))

textComentario = Text(miFrame, width=20, height=5)
textComentario.grid(row=4, column=1, padx=10, pady=10)

scrollVertical = Scrollbar(miFrame, command = textComentario.yview)
scrollVertical.grid(row=4, column=2, sticky="nsew")
textComentario.config(yscrollcommand = scrollVertical.set, font=("", 14))

#*********labels******************
nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)
nombreLabel.config(font=("", 12))

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)
apellidoLabel.config(font=("", 12))

passwordLabel = Label(miFrame, text="Contraseña:")
passwordLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)
passwordLabel.config(font=("", 12))

direccionLabel = Label(miFrame, text="Dirección:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)
direccionLabel.config(font=("", 12))

comentariosLabel = Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)
comentariosLabel.config(font=("", 12))

def codigoBoton():
    minombre.set("Imane")
    
botonSubmit = Button(raiz, text="Enviar", command=codigoBoton)
botonSubmit.pack()
botonSubmit.place(x=650, y=600)
botonSubmit['borderwidth'] = 5
botonSubmit['relief'] = 'raised'
botonSubmit.config(pady=5, padx=10, font=("", 12) )
raiz.mainloop()