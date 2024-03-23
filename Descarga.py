from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
from pytube import YouTube

def Dowloader():
    try:
        url = YouTube(str(link.get()))
        video = url.streams.get_highest_resolution()
        video.download()
        messagebox.showinfo("Exito", "Descarga completada!")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('Tu propio downloader de YouTube con Python')
root.configure(bg='#AACDE2')

Label(root, text='Descarga tus videos', font='arial 20 bold', bg='#AACDE2').place(x=90, y=30)

link = StringVar()
Label(root, text='Pega el link aquí:', font='arial 12', bg='#AACDE2').place(x=190, y=90)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=120)

Button(root, text='DESCARGAR', font='arial 13 bold italic', bg='#B57199', padx=2, command=Dowloader).place(x=180, y=180)

root.mainloop()
