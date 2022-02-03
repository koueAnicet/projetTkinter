from tkinter import*

import fonctions

def seconMenuPrinci():
    fenetre = Tk()
    fenetre.title("Demande de consultion")
    fenetre.geometry("1900x1900")# taille de de la fenetre
    fenetre.configure(bg="#0be6e6")
    #fenetre.resizable(False, False)#empeche d'agrandir la fenetre

    btn = Button(fenetre, text="S'engerister", font=('Arial', 13, "bold"), fg='black', command=fonctions.enregistrer)
    btn

    btn.grid(row=0, column=0, padx=10, pady=25, ipady=5)

    btn1 = Button(fenetre, text="Consultation", font=('Arial', 13, "bold"), fg='black', command=fonctions.consultation)
    btn1
    btn1.grid(row=0, column=1, padx=0, pady=25, ipady=5)
    btn2 = Button(fenetre, text="Rendez-Vous", font=('Arial', 13, "bold"), fg='black', command=fonctions.rendezVous)
    btn2.grid(row=0, column=2, padx=0, pady=25, ipady=5)

    btn3 = Button(fenetre, text="Resultat/Diagnostique", font=('Arial', 13, "bold"), fg='black')
    btn3
    btn3.grid(row=0, column=3, padx=0, pady=25, ipady=5)

    btn4 = Button(fenetre, text="Se connecté", font=('Arial', 13, "bold"), fg='black', command=fonctions.connexion)
    btn4
    btn4.grid(row=0, column=4, padx=0, pady=25, ipady=5)


    btn5 = Button(fenetre, text="S'inscrire'", font=('Arial', 13, "bold"), fg='black', command=fonctions.s_inscrire)
    btn5
    btn5.grid(row=0, column=5, padx=0, pady=25, ipady=5)

    #frame 
    frame = Frame(fenetre, background="white", width=1900, height=1000 , relief="solid", highlightcolor="red", highlightthickness=2, )
    frame.grid(row=1,column=0, columnspan=6, pady=45)

    #recherche



    fenetre.mainloop()