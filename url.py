from tkinter import*
import pyshorteners

root=Tk()
root.title("URL SHORTENER LINK")
root.geometry("800x300")

Label(root,text="Generate Short  Url" , font=("Georgia 25 bold") , fg="Purple").pack(pady=10)

frame1 = Frame(root)
Label(frame1,text="Paste Url here : " , font=("Georgia 15 bold")).pack(side=LEFT)
url=Entry(frame1, width="40", font=("Georgia 15 bold"))
url.pack()
frame1.pack(pady=10)

root.mainloop()