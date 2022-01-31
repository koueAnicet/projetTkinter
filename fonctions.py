
import json
from tkinter import ttk,messagebox
from tkinter import*


def consultation():
    consul= Tk()
    consul.geometry("800x800")
    consul.configure(bg="#08ffef")

    frame =Frame(consul, width=800, height=770)
    frame.pack(pady=100)

    
    consul.mainloop()

def enregistrer():
    dicty={}

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
    EntryCivilite = Entry(frame, width=90, borderwidth=3)
    EntryCivilite .pack()

    labNom= Label(frame, text="Nom ", width=90, font=('Arial', 20, "bold", ))
    labNom.pack()
    EntryNom= Entry(frame, width=90, borderwidth=3)
    EntryNom.pack()

    labPrenom = Label(frame, text="Prenom", width=90, font=('Arial', 20, "bold"))
    labPrenom.pack()
    EntryPrenom= Entry(frame, width=90,  borderwidth=3)
    EntryPrenom.pack()

    labAge = Label(frame, text="Age", width=90, font=('Arial', 20, "bold"))
    labAge.pack()
    EntryAge = Entry(frame, width=90, borderwidth=3)
    EntryAge.pack()

    # btnRendezVous = Label(frame, text="Rendez-vous", width=90, font=('Arial', 20, "bold"))
    # btnRendezVous.pack()
    
     # recuperationdes donees d'enregistrements
    def data_rdv():
        dicty={
            "civilite": EntryCivilite.get(),
            "nom": EntryNom.get(),
            "prenom": EntryPrenom.get(),
            "age": EntryAge.get()

        }
        with open("list_enregistres.json", "a") as f:
            json.dump(dicty, f, indent=4)
        print(dicty)
    Button(frame, text="s'enregistré", width=10, height=3, fg="red", font=('Arial', 23, "bold"), cursor="watch", command=data_rdv).pack(pady=10, ipady=10)
    EntryCivilite.delete(0, END)
    EntryNom.delete(0, END)
    EntryPrenom.delete(0, END)
    EntryAge.delete(0, END)
     
    registre.mainloop()
      

def rendezVous():
    rdz= Tk()
    rdz.title("s'enregister")
    rdz.geometry("500x500")
    rdz.configure(borderwidth=2)
    #rdz.resizable(False, False)#empeche d'agrandir la fenetre

    labelEnregistrer = Label(rdz, text="Prise de rendez-vous!", background="#07dbf7", width=100, height=2, font=('Arial', 22, "bold"), fg='red')
    labelEnregistrer.pack()

    frame = Frame(rdz, width=350, height=350 , background="white", highlightbackground='white', highlightthickness=2)
    frame.pack(pady=60)

    labDate = Label(frame, text="Date du rendez-vous", width=30, font=('Arial', 20, "bold"))
    labDate.grid(row=0, columnspan=3)
    #la date 
    #-----------les jours--------------
    EntryYourEntry = ttk.Combobox(frame, width=10, state="readonly" )
    EntryYourEntry['values'] = (
        "1","2","3","4","5","6","7","8","9","10","11","12","13","14"
        ,"15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
    EntryYourEntry.grid(row=1, column=0, padx=2, pady=10)
    EntryYourEntry.current(0) #selection par defaut
    #--------------les mois-----------
    EntryWeekEntry = ttk.Combobox(frame, width=10, state="readonly" )
    EntryWeekEntry['values'] = (
        "janvier","février","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","décembre")
    EntryWeekEntry.grid(row=1,column=1, padx=2, pady=10)
    EntryWeekEntry.current(0) #selection par defaut

    #--------------annees-----------
    EntryAnneeEntry = ttk.Combobox(frame, width=10, state="readonly" )
    EntryAnneeEntry['values'] = ("2022","2023","2024")
    EntryAnneeEntry.grid(row=1,column=2, padx=2, pady=10)
    EntryAnneeEntry.current(0) #selection par defaut

    #medecin
    labMedecin = Label(frame, text="Médécin", width=30, font=('Arial', 20, "bold"))
    labMedecin .grid(row=2, column=0, columnspan=3)

    EntryMedecin = ttk.Combobox(frame, width=38, state="readonly")
    EntryMedecin['values'] = ("Selectionez","homme","femme")
    EntryMedecin.grid(row=3,column=0, columnspan=3, pady=10)
    EntryMedecin.current(0) #selection par defaut

    Button(frame, text="Valider", width=30, height=1.5, fg="red", font=('Arial', 23, "bold"), cursor="watch", ).grid(row=4, column=0, columnspan=3, pady=10, ipady=10)
    
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
    EntryUser= Entry(frame, width=90, borderwidth=3,)
    EntryUser.pack()

    labEmail = Label(frame, text="Email", width=90, font=('Arial', 20, "bold"))
    labEmail.pack()
    EntryEmail= Entry(frame, width=90, borderwidth=3)
    EntryEmail.pack()

    labPassword = Label(frame ,text="Mot de pass", width=90, font=('Arial', 20, "bold"))
    labPassword.pack()
    EntryPassword= Entry(frame, width=90, borderwidth=3)
    EntryPassword.pack()

    btn = Button(frame, text="Enregistrer", width=30, height=2, fg="red", font=('Arial', 18, "bold"), cursor="mouse").pack( pady=20)

    connexion.mainloop()  

