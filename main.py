from tkinter import*

import fonctions

fenetre = Tk()
fenetre.title("gestion")
fenetre.geometry("1900x1900")# taille de de la fenetre
fenetre.configure(bg="light blue")
#fenetre.resizable(False, False)#empeche d'agrandir la fenetre

btn = Button(fenetre, text="s'engerister", command=fonctions.enregistrer)
btn.grid(row=0, column=1, padx=0, pady=20, ipady=5)
btn1 = Button(fenetre, text="Diagnostique")
btn1.grid(row=0, column=2, padx=0, pady=20, ipady=5)
btn2 = Button(fenetre, text="zrtrzt")
btn2.grid(row=0, column=3, padx=0, pady=20, ipady=5)
btn3 = Button(fenetre, text="rrtr")
btn3.grid(row=0, column=4, padx=0, pady=20, ipady=5)
btn4 = Button(fenetre, text="Se connecté", command=fonctions.connexion)
btn4.grid(row=0, column=5, padx=0, pady=20, ipady=5)

#frame 
frame = Frame(fenetre, background="white", width=1900, height=1000 , relief="solid", highlightcolor="red", highlightthickness=2, )
frame.grid(row=1, columnspan=6, pady=60,)



fenetre.mainloop()