
from tkinter import ttk,messagebox
from tkinter import*
from xmlrpc.client import DateTime


def enregistrer():
    registre= Tk()
    registre.title("s'enregister")
    registre.geometry("500x500")
    registre.configure(borderwidth=2)
    registre.resizable(False, False)#empeche d'agrandir la fenetre

    labelEnregistrer = Label(registre, text="Enregistrez-vous!", background="#07dbf7", width=100, height=2, font=('Arial', 22, "bold"), fg='red')
    labelEnregistrer.pack()

    frame = Frame(registre, width=350, height=350 , background="white", highlightbackground='white', highlightthickness=2)
    frame.pack(pady=60)
    
    labCivilite = Label(frame ,text="Civilité", width=90, font=('Arial', 20, "bold"))
    labCivilite .pack()
    EntryCivilite = Entry(frame, width=90)
    EntryCivilite .pack()

    labNom= Label(frame, text="Nom ", width=90, font=('Arial', 20, "bold"))
    labNom.pack()
    EntryNom= Entry(frame, width=90)
    EntryNom.pack()

    labPrenom = Label(frame, text="Prenom", width=90, font=('Arial', 20, "bold"))
    labPrenom.pack()
    EntryPrenom= Entry(frame, width=90)
    EntryPrenom.pack()

    labAge = Label(frame, text="Age", width=90, font=('Arial', 20, "bold"))
    labAge.pack()
    EntryAge = Entry(frame, width=90)
    EntryAge.pack()

    # btnRendezVous = Label(frame, text="Rendez-vous", width=90, font=('Arial', 20, "bold"))
    # btnRendezVous.pack()

    Button(frame, text="Rendez-vous", width=10, height=3, fg="red", font=('Arial', 23, "bold"), command=rendezVous ).pack(pady=10, ipady=10)
    
    registre.mainloop()  

def rendezVous():
    rdz= Tk()
    rdz.title("s'enregister")
    rdz.geometry("500x500")
    rdz.configure(borderwidth=2)
    rdz.resizable(False, False)#empeche d'agrandir la fenetre

    labelEnregistrer = Label(rdz, text="Prise de rendez-vous!", background="#07dbf7", width=100, height=2, font=('Arial', 22, "bold"), fg='red')
    labelEnregistrer.pack()

    frame = Frame(rdz, width=350, height=350 , background="white", highlightbackground='white', highlightthickness=2)
    frame.pack(pady=60)

    labDate = Label(frame, text="Date du rendez-vous", width=20, font=('Arial', 20, "bold"))
    labDate.grid(row=0)
    #la date 
    EntryYourEntry = ttk.Combobox(frame, width=5, state="readonly" )
    EntryYourEntry['values'] = (
        "1","2","3","4","5","6","7","8","9","10","11","12","13","14"
        ,"15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
    EntryYourEntry.grid(row=1, column=0, padx=10)
    EntryYourEntry.current(0) #selection par defaut
    #----------------------------_
    EntryWeekEntry = ttk.Combobox(frame, width=5, state="readonly" )
    EntryWeekEntry['values'] = (
        "1","2","3","4","5","6","7","8","9","10","11","12")
    EntryWeekEntry.grid(row=1,column=1, padx=10)
    EntryWeekEntry.current(0) #selection par defaut

    #efeffgrgrgggt
    labMedecin = Label(frame, text="Medecin", width=90, font=('Arial', 20, "bold"))
    labMedecin .pack()

    EntryMedecin = ttk.Combobox(frame, width=90, state="readonly")
    EntryMedecin['values'] = ("Selectionez","homme","femme")
    EntryMedecin.pack()
    EntryMedecin.current(0) #selection par defaut

    rdz.mainloop()

def connexion():
    connexion = Tk()
    connexion.title("connexion")
    connexion.geometry("500x500")# taille de de la fenetre
    connexion.configure( borderwidth=2)
    connexion.resizable(False, False)#empeche d'agrandir la fenetre

    labelConnexion = Label(connexion, text="Connectez-vous ici !", background="#1cd6d3", width=100, height=2, font=('Arial', 22, "bold"), fg='red')
    labelConnexion.pack()

    frame = Frame(connexion, width=350, height=350 , background="white", highlightbackground='white', highlightthickness=2)
    frame.pack(pady=60)

    labUser= Label(frame, text="Nom utilisation", width=90, font=('Arial', 20, "bold"))
    labUser.pack()
    EntryUser= Entry(frame, width=90)
    EntryUser.pack()

    labEmail = Label(frame, text="Email", width=90, font=('Arial', 20, "bold"))
    labEmail.pack()
    EntryEmail= Entry(frame, width=90)
    EntryEmail.pack()

    labPassword = Label(frame ,text="Mot de pass", width=90, font=('Arial', 20, "bold"))
    labPassword.pack()
    EntryPassword= Entry(frame, width=90)
    EntryPassword.pack()

    btn = Button(frame, text="Enregistrer", width=30, height=2, fg="red", font=('Arial', 18, "bold")).pack( pady=20)

    if btn :
        pass
    connexion.mainloop()  
