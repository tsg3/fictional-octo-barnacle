from tkinter import *
license_view = Tk()

def display_license_view():
    license_view.title("Taller GIT - Licencia") 
    license_view.minsize(500,500) 
    license_view.maxsize(500,500)
     
    license_lbl = Label(license_view, text = "Licencia", font = ("calibri","18"), fg = "#000b98", width= 28, height = 1)
    license_lbl.place(x = 20, y = 20)
     
    license_view.mainloop()

# Eliminar esta linea para que la ventana se abra cuando se presione el botón en el menú principal.
display_license_view()
