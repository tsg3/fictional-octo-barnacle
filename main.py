from tkinter import *
import license
import about
#Label(etiqueta)
 
root = Tk() #lol
 
root.title("Taller GIT") 
root.minsize(500,500) 
root.maxsize(500,500)
 
#Label con texto
#etiquetatexto = Label(WidgetContenedor, text=Contenido, font = (Tipo,Tamanno), bg=ColorDeFondo, fg=ColorDeLetra, width, height)
welcome_lbl = Label(root, text = "Bienvenidos al taller de GIT", font = ("calibri","18"), fg = "#000b98", width= 28, height = 1)
welcome_lbl.place(x = 20, y = 20)
 
root.mainloop()
