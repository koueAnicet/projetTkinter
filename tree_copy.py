from tkinter import*
import json
from tkinter.ttk import Treeview

#The Next page which shows the results of the formula  
 
def tree():
    from tkinter.ttk import Treeview
    window = Tk()
    window.title("Les rendez-vous")
    tree = Treeview(window, height=30) 
    tree['columns']=("Date_rdz","Civilite","Nom", "Prenom","Age","Medecin")
    
    tree.heading("Date_rdz", text="Date rdz", )
    tree.heading("Civilite", text="Civilité", )
    tree.heading("Nom", text="Nom", )
    tree.heading("Prenom", text="Prenom", )
    tree.heading("Age", text="Age", )
    tree.heading("Medecin", text="Medecin", )
    
    
    tree.column("Date_rdz",  )
    tree.column("Civilite",  )
    tree.column("Nom",  )
    tree.column("Prenom", )
    tree.column("Age",  )
    tree.column("Medecin",  )
    
    
    
    with open("/Users/imac-05/Desktop/projetTkinter/dataAdmin.json", "r", encoding='utf-8') as f:
        liste = json.load(f)
        for i in liste: 
            for elt in i.values():
                tree.insert( parent='',index='end', values=(elt))
                
    
    tree.pack(pady=20, ipady=100)
    
    btn = Button(window, text="Retour" , font="Roboto 15",)
    btn.pack(ipadx=25, pady=10, ipady=10)
 
    window.mainloop()
    