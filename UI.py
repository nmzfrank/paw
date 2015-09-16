from sys import exit
import Tkinter

def hello():
	print ('hello')


mainframe = Tkinter.Tk()
menu = Tkinter.Menu(mainframe)
filemenu = Tkinter.Menu(menu,tearoff=0)
filemenu.add_command(label = "new", command=hello)
filemenu.add_command(label = "save", command=hello)
menu.add_cascade(label="file", menu=filemenu)

mainframe.config(menu=menu)
mainframe.mainloop()
