import tkinter

ventana = tkinter.Tk()

v = tkinter.IntVar()

#elemento = StringVar()
listbox = tkinter.Listbox(ventana)
for item in ["Argentina", "Brasil", "Ecuador", "Uruguay"]:
    listbox.insert(-1, item)

listbox.pack()
label = tkinter.Label(text="Clasificados a Qatar 2022")
label.pack()

ventana.mainloop()
