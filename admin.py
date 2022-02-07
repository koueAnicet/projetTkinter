from distutils import command
from struct import pack
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



frame2 =Frame(admin, width=1500, height=1000, borderwidth=2, bg="grey")
frame2.grid(row=0 ,column=2, padx=50, pady=20)
if btn1:
    frame3= Frame(frame2, width=300, height=1000, borderwidth=2, highlightcolor= "red", bg="lightyellow" ).grid(row=0 ,column=1, padx=10, pady=20)
elif btn2:
    frame4= Frame(frame2, width=300, height=1000, borderwidth=2, highlightcolor= "red", bg="brown" ).grid(row=0 ,column=2, padx=10, pady=20)

elif btn3:
    frame4= Frame(frame2, width=300, height=1000, borderwidth=2, highlightcolor= "red", bg="lightgreen" ).grid(row=0 ,column=3, padx=10, pady=20)
admin.mainloop()



