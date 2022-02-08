import pageUser
import fonctions
from tkinter import*
from PIL import ImageTk,Image
accueil =Tk()
def screen():
    
	width = accueil.winfo_screenwidth()
	height = accueil.winfo_screenheight()
    
	return width, height 


accueil.configure(bg="#0be6e6")
accueil.geometry()
accueil.title("Accueil")

#accueil.resizable(False, False)#empeche d'agrandir la fenetre

btn1=Button(accueil, text="Se connecter", width=20, fg="red", font=("Condensed Italic", 20, "bold"),cursor="hand1",command=fonctions.connexion)
btn1.grid(row=0, column=0, padx= 100,pady=20, ipady=10)

btn2=Button(accueil, text="S'inscrire", width=20, fg="red", font=("Condensed Italic", 20, "bold"), cursor="hand1",command=fonctions.s_inscrire)
btn2.grid(row=0, column=1 , pady=20, ipady=10)

btn3=Button(accueil, text="principal", width=20, fg="red", font=("Condensed Italic", 20, "bold"), cursor="hand1",command=pageUser.seconMenuPrinci)
btn3.grid(row=0, column=2 ,padx=120, pady=20, ipady=10)

#frame =Frame(accueil, width=1200,height=900, bg="#00ffc8", ).grid(row=1, columnspan=2,ipady=0, pady=30)

img = ImageTk.PhotoImage(Image.open("hospi.jpeg"))
img_label=Label(accueil, image= img, width=1000, height=900).grid(row=1, column=0,columnspan=3, )

accueil.mainloop()