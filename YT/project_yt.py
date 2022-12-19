import tkinter
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import Image,ImageTk
from pytube import YouTube


frm=Tk()
frm.geometry('700x950') # main window
frm.resizable(width=False,height=False)
frm.configure(bg='black')

#logo placed in center of main frame
img=Image.open('../YT/pngwing.com.png')
img=img.resize((250,200))
imgtk=ImageTk.PhotoImage(img,master=frm)

l=Label(frm,image=imgtk,bg='black')
l.place(relx=.34,rely=.0)

def main_frame():
    frm1=Frame(frm,bg='black') #frame inside window
    frm1.place(relx=.03,rely=.2,width=660,height=730)
    
    #link part here
    lbl_enter=Label(frm1,font=('arial',17,'italic'),bg='black',fg='red',text='Link: ')
    lbl_enter.place(relx=.05,rely=.1)
    
    e_enter=Entry(frm1,bd=6)
    e_enter.place(relx=.22,rely=.1,width=420)
    e_enter.focus()#end of link part here
    
    
    #start of format part here
    lbl_format=Label(frm1,font=('arial',17,'italic'),bg='black',fg='red',text='Format')
    lbl_format.place(relx=.05,rely=.2)
    
    e_format=Combobox(frm1,font=('arial',17,'italic'),values=("  ---------select format----------","144p","240p","360p","720p","1080p"))
    e_format.place(relx=.22,rely=.2,width=420)
    e_format.current(0)#end of format part here
    
    
    
    #start of path part here
    lbl_path=Label(frm1,font=('arial',17,'italic'),bg='black',fg='red',text='Path')
    lbl_path.place(relx=.05,rely=.3)
    
    e_path=Combobox(frm1,font=('arial',17,'italic'),values=("/home/vaibh/Videos/","/home/vaibh/Music/","/home/vaibh/Downloads/"))
    e_path.place(relx=.22,rely=.3,width=420)
    e_path.current(0)#end of path part here
    
    
    #logic for link taking
    def link():   
        try:
             
            link = e_enter.get()
            con = YouTube(link)
            # print(con.title)
        except:
            messagebox.showerror("WARNING","INVALID LINK OR BROKEN URL")
        
        #resolution logic
        res = e_format.get()
        format = con.streams.filter(res=e_format.get())
        video = list(enumerate(format))        
        format[0].download(e_path.get())   
        messagebox.showinfo("DONE","Video downloaded")
        
    def clear():
        e_enter.delete(0,'end')
        e_format.delete(0,'end')
        e_path.delete(0,'end')
        e_enter.focus()
        e_format.current(0)
        e_path.current(0)
        

    #clear
    btn_clear=Button(frm1,font=('arial',17,'italic'),bg='black',fg='white',text='clear',command=clear)
    btn_clear.place(relx=.2,rely=.5,width=200)         
    #enter button
    btn_enter=Button(frm1,font=('arial',17,'italic'),bg='black',fg='white',text='Download',command=link)
    btn_enter.place(relx=.5,rely=.5,width=200)
    
main_frame()
frm.mainloop()

