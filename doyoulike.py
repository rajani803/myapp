import tkinter as tk
from PIL import Image, ImageTk
import random


myApp = tk.Tk()
myApp.geometry("1200x800")
myApp.configure(background='light blue')
myApp.title("Do You Like Me?")


mainMenu = tk.Frame(myApp, background='light blue')
mainMenu.place(relx=0.5, rely=0.5, anchor='center')

def move_no_button():
    new_x = random.randint(100, 900)
    new_y = random.randint(100, 600)
    btn_no.place(x=new_x, y=new_y)


def display_gif():
    gif_path = "cat.gif"  
    img = Image.open(gif_path)

    
    frames = []
    try:
        while True:
            frames.append(ImageTk.PhotoImage(img.copy()))
            img.seek(len(frames)) 
    except EOFError:
        pass  

    def update_gif(index):
        label.config(image=frames[index])
        myApp.after(100, update_gif, (index + 1) % len(frames))

    label = tk.Label(mainMenu, bg='light blue')
    label.grid(column=7, row=4)
    update_gif(0)


def display_heart_gif():
    heart_gif_path = "pink_heart.gif" 
    heart_img = Image.open(heart_gif_path)

    heart_frames = []
    try:
        while True:
            frame = heart_img.copy()
            resized_frame = frame.resize((heart_img.width * 2, heart_img.height * 2), Image.Resampling.LANCZOS)
            heart_frames.append(ImageTk.PhotoImage(resized_frame))
            heart_img.seek(len(heart_frames))  
    except EOFError:
        pass  

    heart_label = tk.Label(myApp, bg='light blue')
    heart_label.place(relx=0, rely=0, relwidth=1, relheight=1)  


    tk.Label(myApp, text="I know", font=('Helvetica', 24, 'bold italic'), bg='light blue', fg='dark blue').place(relx=0.5, rely=0.9, anchor='center')


    def update_heart_gif(index):
        heart_label.config(image=heart_frames[index])
        index = (index + 1) % len(heart_frames)  
        myApp.after(100, update_heart_gif, index)  

   
    update_heart_gif(0)


text = tk.Label(mainMenu, text="Do you like me?", font=('Helvetica', 24, 'bold italic'),
                background='light blue', bd=20, fg='dark blue')  
text.grid(column=7, row=5, pady=20)


btn_yes = tk.Button(mainMenu, text="Yes", font=('Helvetica 14 bold italic'),
                    background='pink', activebackground='red', bd=5, height=2,
                    width=10, fg='white', relief=tk.SOLID, command=display_heart_gif)
btn_yes.grid(column=10, row=5, padx=20)


btn_no = tk.Button(myApp, text="No", font=('Helvetica 14 bold italic'),
                   background='pink', activebackground='red', bd=5, height=2,
                   width=10, fg='white', relief=tk.SOLID, command=move_no_button)
btn_no.place(x=500, y=400)  


display_gif()


myApp.mainloop()
