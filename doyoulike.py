import tkinter as tk
from PIL import Image, ImageTk
import random

# Create the main window
myApp = tk.Tk()
myApp.geometry("1200x800")
myApp.configure(background='light blue')
myApp.title("Do You Like Me?")

# Main frame for layout
mainMenu = tk.Frame(myApp, background='light blue')
mainMenu.place(relx=0.5, rely=0.5, anchor='center')

# Move the "No" button randomly, ensuring it's within the visible area
def move_no_button():
    new_x = random.randint(100, 900)
    new_y = random.randint(100, 600)
    btn_no.place(x=new_x, y=new_y)

# Function to display the cat GIF
def display_gif():
    gif_path = "cat.gif"  # Path to your cat GIF
    img = Image.open(gif_path)

    # Handle frames for the GIF
    frames = []
    try:
        while True:
            frames.append(ImageTk.PhotoImage(img.copy()))
            img.seek(len(frames))  # Go to the next frame
    except EOFError:
        pass  # End of GIF

    def update_gif(index):
        label.config(image=frames[index])
        myApp.after(100, update_gif, (index + 1) % len(frames))

    label = tk.Label(mainMenu, bg='light blue')
    label.grid(column=7, row=4)
    update_gif(0)

# Function to display the pink heart GIF when "Yes" is clicked
def display_heart_gif():
    heart_gif_path = "pink_heart.gif"  # Path to your pink heart GIF
    heart_img = Image.open(heart_gif_path)

    # Handle frames for the heart GIF
    heart_frames = []
    try:
        while True:
            frame = heart_img.copy()
            resized_frame = frame.resize((heart_img.width * 2, heart_img.height * 2), Image.Resampling.LANCZOS)
            heart_frames.append(ImageTk.PhotoImage(resized_frame))
            heart_img.seek(len(heart_frames))  # Move to the next frame
    except EOFError:
        pass  # End of GIF

    heart_label = tk.Label(myApp, bg='light blue')
    heart_label.place(relx=0, rely=0, relwidth=1, relheight=1)  # Cover entire screen with GIF

    # Add "I know" label below the heart GIF
    tk.Label(myApp, text="I know", font=('Helvetica', 24, 'bold italic'), bg='light blue', fg='dark blue').place(relx=0.5, rely=0.9, anchor='center')

    # Function to update and loop the GIF
    def update_heart_gif(index):
        heart_label.config(image=heart_frames[index])
        index = (index + 1) % len(heart_frames)  # Loop the frames
        myApp.after(100, update_heart_gif, index)  # Adjust delay as needed (100ms)

    # Start the GIF animation
    update_heart_gif(0)

# Label asking the question (more visible)
text = tk.Label(mainMenu, text="Do you like me?", font=('Helvetica', 24, 'bold italic'),
                background='light blue', bd=20, fg='dark blue')  # Dark blue font for visibility
text.grid(column=7, row=5, pady=20)

# "Yes" Button triggers the pink heart GIF
btn_yes = tk.Button(mainMenu, text="Yes", font=('Helvetica 14 bold italic'),
                    background='pink', activebackground='red', bd=5, height=2,
                    width=10, fg='white', relief=tk.SOLID, command=display_heart_gif)
btn_yes.grid(column=10, row=5, padx=20)

# "No" Button moves randomly using 'place' to visibly move it
btn_no = tk.Button(myApp, text="No", font=('Helvetica 14 bold italic'),
                   background='pink', activebackground='red', bd=5, height=2,
                   width=10, fg='white', relief=tk.SOLID, command=move_no_button)
btn_no.place(x=500, y=400)  # Initial position for the "No" button

# Display the cat GIF
display_gif()

# Start the app
myApp.mainloop()
