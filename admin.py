from distutils import command
from struct import pack
from tkinter import*
from tkinter import messagebox
import fonctions,json

def listeUser():
    with open("dataConnexion.json", "r") as f:
       listU= json.load(f)
        
    
    for i in listU:
        messagebox.showinfo("info","")  

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

admin = Tk()
admin.configure()
admin.title('Page admins')
admin.geometry("1900x1900")
#admin.resizable("")


#frame1 = Frame(admin, width=300, height=1000, borderwidth=2, highlightcolor= "red", bg="lightgrey")
#frame1.grid(row= 0,column=0 )

btn1=Button(admin, text="liste Rendez-vous", width=20, command=tree).pack(pady=20, ipady=10)
btn2=Button(admin, text="liste Users", width=20,command=listeUser).pack(ipady=10)

#btn3=Button(admin, text="Consultion", width=20, command=fonctions.consultation).pack(pady=20, ipady=10)


 
"""frame2 =Frame(admin, width=1500, height=1000, borderwidth=2, bg="grey")
frame2.grid(row=0 ,column=2, padx=50, pady=20)
if btn1:
    frame3= Frame(frame2, width=300, height=1000, borderwidth=2, highlightcolor= "red", bg="lightyellow" ).grid(row=0 ,column=1, padx=10, pady=20)
elif btn2:
    frame4= Frame(frame2, width=300, height=1000, borderwidth=2, highlightcolor= "red", bg="brown" ).grid(row=0 ,column=2, padx=10, pady=20)

elif btn3:
    frame4= Frame(frame2, width=300, height=1000, borderwidth=2, highlightcolor= "red", bg="lightgreen" ).grid(row=0 ,column=3, padx=10, pady=20)"""
admin.mainloop()



