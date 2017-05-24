from tkinter import *
about_view = Tk()

def display_about_view():
    about_view.title("Taller GIT - Sobre Nosotros") 
    about_view.minsize(500,500) 
    about_view.maxsize(500,500)
     
    about_lbl = Label(about_view, text = "Sobre este proyecto", font = ("calibri","18"), fg = "#000b98", width= 28, height = 1)
    about_lbl.place(x = 20, y = 20)
     
    about_view.mainloop()

# Eliminar esta linea para que la ventana se abra cuando se presione el botón en el menú principal.
display_about_view()
