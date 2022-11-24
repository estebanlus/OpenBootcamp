import tkinter

ventana = tkinter.Tk()

v = tkinter.IntVar()

values = {"Brasil" : "1",
        "Argentina" : "2",
        "Ecuador" : "3",
        "Uruguay" : "4"}

for (text, value) in values.items():
    tkinter.Radiobutton(ventana, text = text, variable = v,
        value = value).pack(side = 'top', ipady = 5)

def reiniciar(valor):
    global v
    v.set(None)

bReinicio = tkinter.Button(ventana, text="Reiniciar!", bg= "grey", fg="black")
bReinicio.pack(ipadx=30, ipady=30, side='right')

bReinicio.bind('<Button-1>',reiniciar)

print(ventana)

ventana.mainloop()
