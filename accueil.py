import fonctions
from tkinter import*


accueil =Tk()
accueil.configure(bg="#00ffc8")
accueil.geometry("1900x1900")
accueil.title("Accueil")
#accueil.resizable(False, False)#empeche d'agrandir la fenetre

Button(accueil, text="Se connecter", width=20, fg="red", font=("Condensed Italic", 20, "bold"),cursor="hand",command=fonctions.connexion).grid(row=0, column=0,padx=0,pady=20, ipady=10)
Button(accueil, text="S'inscrire", width=20, fg="red", font=("Condensed Italic", 20, "bold"), cursor="hand",command=fonctions.s_inscrire).grid(row=0, column=1, padx=0 , pady=20, ipady=10)

frame =Frame(accueil, width=1500,height=900, bg="#61d2ff", ).grid(row=1, column=0, columnspan=2, padx=200, pady=30)


accueil.mainloop()