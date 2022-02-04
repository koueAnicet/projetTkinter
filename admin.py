from tkinter import*
from tkinter import messagebox
import fonctions

admin = Tk()
admin.configure()
admin.title('Page admins')
admin.geometry("1900x1900")
#admin.resizable("")

frame1 = Frame(admin, width=300, height=1000, borderwidth=2, highlightcolor= "red", bg="lightgrey")
frame1.grid(row= 0,column=0 )

btn1=Button(frame1, text="liste Rendez-vous", width=20).pack(pady=20, ipady=10)
btn2=Button(frame1, text="liste Users", width=20).pack(ipady=10)
btn3=Button(frame1, text="Consultion", width=20, command=fonctions.consultation).pack(pady=20, ipady=10)

if btn1:
    
   print("hfgjfjfjf")
    # consul= Tk()
    # consul.geometry("800x800")
    # consul.configure(bg="#08ffef")

    # frame =Frame(consul, width=800, height=770)
    # frame.pack(pady=100)

    
    # consul.mainloop()
elif btn2:
    messagebox.showinfo("info", "hello")
elif btn3:
    messagebox.showinfo("info", "uouoh")

frame2 =Frame(admin, width=1500, height=1000, borderwidth=2, bg="grey")
frame2.grid(row=0 ,column=2, padx=50, pady=20)

admin.mainloop()



