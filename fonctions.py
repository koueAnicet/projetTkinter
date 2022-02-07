import json
from tkinter import ttk,messagebox
from tkinter import*
import pageUser
import os

def consultation():
    consul= Tk()
    consul.geometry("800x800")
    consul.configure(bg="#08ffef")

    frame =Frame(consul, width=800, height=770)
    frame.pack(pady=100)

    
    consul.mainloop()

def enregistrer():
    
    
    registre= Tk()
    registre.title("s'enregister")
    registre.geometry("500x600")
    registre.configure(borderwidth=2)
    registre.resizable(False, False)#empeche d'agrandir la fenetre

    labelEnregistrer = Label(registre, text="Enregistrez-vous!", background="#07dbf7", width=100, height=2, font=('Arial', 22, "bold"), fg='red')
    labelEnregistrer.pack()

    frame = Frame(registre, width=350, height=400, background="white", highlightbackground='white', highlightthickness=2)
    frame.pack(pady=60)
    
    labCivilite = Label(frame ,text="Civilité", width=90, font=('Arial', 20, "bold"))
    labCivilite .pack()
    EntryCivilite = Entry(frame, width=90, borderwidth=3)
    EntryCivilite .pack(ipady=3)
#EntrymoisEntry = ttk.Combobox(frame, width=10, state="readonly" )
    # EntryWeekEntry['values'] = (
    #     "janvier","février","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","décembre")
    # EntryWeekEntry.grid(row=1,column=1, padx=2, pady=10)
    # EntryWeekEntry.current(0) #selection par defaut
    labNom= Label(frame, text="Nom ", width=90, font=('Arial', 20, "bold", ))
    labNom.pack()
    EntryNom= Entry(frame, width=90, borderwidth=3)
    EntryNom.pack(ipady=3)

    labPrenom = Label(frame, text="Prenom", width=90, font=('Arial', 20, "bold"))
    labPrenom.pack()
    EntryPrenom= Entry(frame, width=90,  borderwidth=3)
    EntryPrenom.pack(ipady=3)

    labAge = Label(frame, text="Age", width=90, font=('Arial', 20, "bold"))
    labAge.pack()
    EntryAge = Entry(frame, width=90, borderwidth=3)
    EntryAge.pack(ipady=3)

    labEmail = Label(frame, text="Email", width=90, font=('Arial', 20, "bold"))
    labEmail.pack()
    EntryEmail = Entry(frame, width=90, borderwidth=3)
    EntryEmail.pack(ipady=3)

    # btnRendezVous = Label(frame, text="Rendez-vous", width=90, font=('Arial', 20, "bold"))
    # btnRendezVous.pack()
    
     # recuperationdes donees d'enregistrements
    def data_rdv():
        list_enregist=[]
        
        dicty={
            "civilite": EntryCivilite.get(),
            "nom": EntryNom.get(),
            "prenom": EntryPrenom.get(),
            "age": EntryAge.get(),
            "email": EntryEmail.get()
            }
        list_enregist.append(dicty)
        print(list_enregist)
        try:
            with open("list_inscris.json", "r") as f:
                json.load(f)

        except json.decoder.JSONDecodeError:
           
            with open("list_inscris.json", "w") as f:
                json.dump(list_enregist, f, indent=4)
       

        else:
            with open("list_inscris.json", "r") as f:
                json.load(f)
            list_enregist.append(dicty)    

        with open("list_inscris.json", "w") as f:
            json.dump(list_enregist, f, indent=4) 

        EntryCivilite.delete(0, END)
        EntryNom.delete(0, END)
        EntryPrenom.delete(0, END)
        EntryAge.delete(0, END)
       
        
    Button(frame, text="s'enregistré", width=25, height=10, fg="red", font=('Arial', 23, "bold"), cursor="hand", command=data_rdv,).pack(pady=8, ipady=35,)
    
     
    registre.mainloop()
    
      

def rendezVous():
    rdz= Tk()
    rdz.title("s'enregister")
    rdz.geometry("500x500")
    rdz.configure(borderwidth=2)
    #rdz.resizable(False, False)#empeche d'agrandir la fenetre

    labelEnregistrer = Label(rdz, text="Prise de rendez-vous!", background="#07dbf7", width=100, height=2, font=('Arial', 22, "bold"), fg='red')
    labelEnregistrer.pack()

    frame = Frame(rdz, width=350, height=450 , background="white", highlightbackground='white', highlightthickness=2)
    frame.pack(pady=60)
    labCivilite = Label(frame, text="Civilité", width=11, font=('Condensed Italic', 15, "bold")).grid(row=0, column=0, pady=10)
    entryCivilite = Entry(frame, width=11, borderwidth=3)
    entryCivilite.grid(row=1, column=0)

    labNom = Label(frame, text="Nom", width=11, font=('Condensed Italic', 15, "bold")).grid(row=0, column=1, pady=10)
    entryNom = Entry(frame, width=11, borderwidth=3)
    entryNom.grid(row=1, column=1)

    labPrenom = Label(frame, text="Prenom", width=11, font=('Condensed Italic', 15, "bold")).grid(row=0, column=2, pady=10)
    entryPrenom= Entry(frame, width=11,borderwidth=3)
    entryPrenom.grid(row=1, column=2)

    

    labDate = Label(frame, text="Date du rendez-vous", width=30, font=('Condensed Italic', 20, "bold"))
    labDate.grid(row=2, columnspan=3, pady=10)
    
    #

    #-----------les jours--------------
    EntryJoursEntry = ttk.Combobox(frame, width=10, state="readonly" )
    EntryJoursEntry['values'] = (
        "1","2","3","4","5","6","7","8","9","10","11","12","13","14"
        ,"15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
    EntryJoursEntry.grid(row=3, column=0, padx=2, pady=10)
    EntryJoursEntry.set("jour") #selection par defaut
    #--------------les mois-----------
    EntrymoisEntry = ttk.Combobox(frame, width=10, state="readonly" )
    EntrymoisEntry['values'] = (
        "janvier","février","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","décembre")
    EntrymoisEntry.grid(row=3,column=1, padx=2, pady=10)
    EntrymoisEntry.set("mois") #selection par defaut
    
    #--------------annees-----------
    EntryAnneeEntry = ttk.Combobox(frame, width=10, state="readonly" )
    EntryAnneeEntry['values'] = ("2022","2023","2024")
    EntryAnneeEntry.grid(row=3,column=2, padx=2, pady=10)
    EntryAnneeEntry.set("annnée")#current(0) selection par defaut

    #medecin
    labMedecin = Label(frame, text="Médécin", width=30, font=('Condensed Italic', 20, "bold"))
    labMedecin .grid(row=4, column=0, columnspan=3)

    #choix du medecin
    EntryMedecin = ttk.Combobox(frame, width=43, state="readonly")
    EntryMedecin['values'] = ("Selectionez","homme","femme")
    EntryMedecin.grid(row=4,column=0, columnspan=3, pady=10)
    EntryMedecin.current(0) #selection par defaut
    def donneesRdv():

        dataRdv={
            "jours": EntryJoursEntry.get(),
            "mois": EntrymoisEntry.get(),
            "annees": EntryAnneeEntry.get(),
            "medecins": EntryMedecin.get(),
        }
        print(dataRdv)
    Button(frame, text="prendre-rdv", width=25, height=1, fg="red", font=('Condensed Italic', 23, "bold"), cursor="hand", command=donneesRdv).grid(row=5, column=0, columnspan=3, pady=10, ipady=10)
    
    rdz.mainloop()

def s_inscrire():

    connexion = Tk()
    connexion.title("connexion")
    connexion.geometry("500x680")# taille de de la fenetre
    connexion.configure( borderwidth=2)
    connexion.resizable(False, False)#empeche d'agrandir la fenetre

    labelConnexion = Label(connexion, text="Inscrivez-vous ici !", background="#1cd6d3", width=100, height=2, font=('Arial', 22, "bold"), fg='red')
    labelConnexion.pack()

    frame = Frame(connexion, width=350, height= 500 , background="white", highlightbackground='white', highlightthickness=2)
    frame.pack(pady=60)

    labNom= Label(frame, text="Nom", width=90, font=('Arial', 20, "bold"))
    labNom.pack()
    EntryNom= Entry(frame, width=90, borderwidth=3,)
    EntryNom.pack(ipady=3)

    labPrenom= Label(frame, text="Prenom", width=90, font=('Arial', 20, "bold"))
    labPrenom.pack()
    EntryPrenom= Entry(frame, width=90, borderwidth=3,)
    EntryPrenom.pack(ipady=3)

    labEmail = Label(frame, text="Email", width=90, font=('Arial', 20, "bold"))
    labEmail.pack()
    EntryEmail= Entry(frame, width=90, borderwidth=3)
    EntryEmail.pack(ipady=3)

    labPassword = Label(frame ,text="Mot de pass", width=90, font=('Arial', 20, "bold"))
    labPassword.pack()
    EntryPassword= Entry(frame, width=90,  borderwidth=3)
    EntryPassword.pack(ipady=3)

    labConfirmPassword = Label(frame ,text=" Confirmer mot de pass", width=90, font=('Arial', 20, "bold"))
    labConfirmPassword.pack()
    EntryConfirPassword= Entry(frame, width=90,  borderwidth=3)
    EntryConfirPassword.pack(ipady=3)

    def recupDonneCon():
        listData= []
    
        donnees ={
            "Nom":  EntryNom.get(),
            "Prenom":  EntryPrenom.get(),
            "Email":  EntryEmail.get(),
            "Password":  EntryConfirPassword.get()
        } 

        
        listData.append(donnees)
        try: 
            with open("dataConnexion.json", "r") as ouvFicheJson:
                json.load(ouvFicheJson)
        except json.JSONDecodeError:
            if EntryPassword.get() != EntryConfirPassword.get():
                messagebox.showerror("Erreur","Mot de passe non identique!")

            elif EntryPassword.get()== EntryConfirPassword.get():
                with open("dataConnexion.json","w") as ouvFicheJson:
                    json.dump(listData, ouvFicheJson, indent=4)
                
                messagebox.showinfo("validation reussie!","Inscription reuissie!")

        else:
            with open("dataConnexion.json", "r") as ouvFicheJson:
                donnee =  json.load(ouvFicheJson)

            donnee.append(donnees)
            
            if  EntryPassword.get() != EntryConfirPassword.get():
                messagebox.showerror("Erreur","Mot de passe non identique!")

            elif EntryNom.get()=="" and EntryPrenom.get()=="" and EntryEmail.get()=="" and EntryConfirPassword.get()=="":
                messagebox.showinfo("ChampVide!","remplissez tous les champs!")
            else:
            
                with open("dataConnexion.json","w") as ouvFicheJson:
                    json.dump(donnee, ouvFicheJson, indent=4)   
            
                messagebox.showinfo("validation reussie!","Inscription reuissie!")

        EntryNom.delete(0, END)
        EntryPrenom.delete(0, END)
        EntryEmail.delete(0, END)
        EntryPassword.delete(0, END)
        EntryConfirPassword.delete(0, END)
        
    btn = Button(frame, text="Insris", width=30, height=2, fg="red", font=('Arial', 18, "bold"), cursor="mouse", command=recupDonneCon)
    btn.pack( pady=20)
    
    
    connexion.mainloop()  
    
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

    

    labEmail = Label(frame, text="Email", width=90,  font=('Arial', 20, "bold"))
    labEmail.pack()
    EntryEmail= Entry(frame, width=90, borderwidth=3)
    EntryEmail.pack(ipady=3)

    labPassword = Label(frame ,text="Mot de pass", width=90, font=('Arial', 20, "bold"))
    labPassword.pack()
    EntryPassword= Entry(frame, width=90,  borderwidth=3)
    EntryPassword.pack(ipady=3)

    def connecte():
        with open("dataConnexion.json","r") as f:
            recupCompar = json.load(f)
        print(recupCompar)
        for i in recupCompar:
            
            # for y in i.values():
            if EntryEmail.get() in i.values() and EntryPassword.get() in i.values() :
                messagebox.showinfo("reuissie", "vous êtes connectez!")
                print("ok")
            elif EntryEmail.get()=="" or EntryPassword.get()=="":
                messagebox.showerror("Error", "Veuillez remplir tous les champs!")
            else:
                messagebox.showerror("Error", "vous n'êtes pas inscris!")
            break
        EntryEmail.delete(0, END)
        EntryPassword.delete(0, END)
        

    
                  
    btn = Button(frame, text="connecté", width=30, height=2, fg="red", font=('Arial', 18, "bold"), cursor="hand", command=connecte)
    btn.pack( pady=20) 
    
    connexion.mainloop()

def listRdv():
    pass
def listUser():
    pass