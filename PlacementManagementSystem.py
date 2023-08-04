import tkinter
from tkinter import *
# from tkinter import messagebox
import webbrowser
# import PIL
import customtkinter as ck
import tkinter as tk

from PIL import ImageTk
from PIL import Image

# import LoginDatabase
import PO,student
def web():
    webbrowser.open("http://www.cittumkur.org/placements/")
if __name__ == '__main__':
    root = ck.CTk()
    # ck.set_default_color_theme("green")

    root.title("PlacementManagement")
    root.iconbitmap("Files\\icon.ico")
    # p1=PhotoImage(file='H:\\Placement_Management\\Trails\\icon.png')
    # root.iconphoto(False,p1)
    root.geometry("1024x680")
    root.maxsize(1024, 680)
    ck.set_appearance_mode("light")
    ck.set_default_color_theme("dark-blue")
    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)

        label.config(image=photo)

        label.image = photo  # avoid garbage collection


    image = Image.open('Files/college1.png')
    image2=Image.open('Files/Chethan-balaji.jpg')
    im2=image2.resize((120,120))
    im=ImageTk.PhotoImage(im2)
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    # label1=tkinter.Label(root,text="Placement Management System")
    # label1.place(relx=0.5,rely=0.1,anchor=CENTER)
    label = tkinter.Label(root, image=photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand=YES)

    lab=ck.CTkLabel(root,text="",image=im)
    lab.place(relx=0.85,rely=.1)

    lab1 = ck.CTkLabel(root, text='''Training & Placement Officer
    Mr. Chetan Balaji
    placement@cittumkur.org
    +91-9886090916''', bg_color="black",text_color="white",fg_color=("black","white"))
    lab1.place(relx=0.82, rely=.25)
    lab = ck.CTkLabel(root, bg_color="black", text="To Know More About Our CIT College and Placements ..", text_color="white",fg_color=("black","white"))
    lab.place(relx=0.25, rely=.8)
    btn=ck.CTkButton(root,corner_radius=0, bg_color="black",text="Click Here",command=web)
    btn.place(relx=0.55, rely=.8)


    ck.CTkLabel(root, text="Placement Management System",
                width=120, height=25, bg_color="black", text_color="white",fg_color=("black","white")
                , corner_radius=0,font=("Times New Roman",50)).place(relx=0.5,rely=0.05,anchor=CENTER)

    check_var = tk.StringVar()


    button = ck.CTkButton(root, bg_color="black", text="Student Login",corner_radius=0,border_width=2, command=student.suc)
    button.place(relx=.5, rely=.35, anchor=CENTER)
    button1 = ck.CTkButton(root, bg_color="black", text="Placement Login",corner_radius=0,border_width=2, command=PO.suc)
    button1.place(relx=.5, rely=.45, anchor=CENTER)
   
    ck.CTkButton(root,text="VERSION 1.0", bg_color="black",state=DISABLED,corner_radius=0,border_width=5).place(relx=0.5,rely=.98,anchor=CENTER)

    root.mainloop()

