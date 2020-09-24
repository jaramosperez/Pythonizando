from tkinter import *

# Creamos la raíz
root = Tk()
root.title("Hola Mundo")
root.resizable(1, 1)
root.iconbitmap('@hola.xbm')



frame = Frame(root, width=480, height=320)
frame.pack(fill='both', expand="1")
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")

root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=25)
root.config(relief="ridge")

# Comenzamos el bucle de aplicación, es como un while True
root.mainloop() # Siempre al final
