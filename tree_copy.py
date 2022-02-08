from pydoc import text
from tkinter import*
import json
from tkinter.ttk import Treeview

#The Next page which shows the results of the formula  
 
def tree():
    window = Tk()
    window.title("Les rendez-vous")
    tree = Treeview(window, height=30) 
    tree['columns']=("Date_rdz","Civilite","Nom", "Prenom","Age","Medecin")
    
    tree.heading("Nom", text="Date rdz", )
    tree.heading("Civilite", text="Civilité", )
    tree.heading("Nom", text="Nom", )
    tree.heading("Prenom", text="Prenom", )
    tree.heading("Age", text="Age", )
    tree.heading("Medecin", text="Medecin", )
    
    
    tree.column("Date_rdv",  )
    tree.column("Civilite",  )
    tree.column("Nom",  )
    tree.column("Prenom", )
    tree.column("Age",  )
    tree.column("Medecin",  )
    
    
    
    with open("", "r", encoding='utf-8') as f:
        liste = json.load(f)
        for i in liste: 
            for elt in i.values():
                tree.insert( parent='',index='end', values=(elt))
                
    
    tree.pack(pady=20, ipady=100)
    
    btn = Button(window, text="Retour" , font="Roboto 15")
    btn.pack(ipadx=25, pady=10, ipady=10)
 
    window.mainloop()
    