# Import Required Library
from tkinter import *
import calendar

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")
""" 
# Add Calendar
cal = calendar(root, selectmode = 'day',
			year = 2020, month = 5,
			day = 22)

cal.pack(pady = 20)

def grad_date():
	date.config(text = "Selected Date is: " + cal.get_date())

# Add Button and Label
Button(root, text = "Get Date", command = grad_date).pack(pady = 20)

date = Label(root, text = "")
date.pack(pady = 20)
"""

# def screen():
# 	width = root.winfo_screenwidth()
# 	height = root.winfo_screenheight()
# 	return width,height 

# n1,n2 =screen()
#print(n1,n2 )
#afficher bouton de menu
# from tkinter import*

# Bouton_de_menu=Menubutton(root)
# #Pour ajouter un élément :
# Var1=IntVar()
# Menu1=Menu(Bouton_de_menu, tearoff=0)
# Menu1.add_checkbutton(label="Pizza",variable=Var1)
# Menu1.add_checkbutton(label="kjhk",variable=Var1)
# Bouton_de_menu['menu']=Menu1
# Bouton_de_menu.pack()
""" liste element"""
# liste=Listbox(root)
# #Pour ajouter un élément :
# liste.insert(1,"Emmental")
# liste.pack()

# if b:
# elif:
# elif:
# Execute Tkinter
root.mainloop()
