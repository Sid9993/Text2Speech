

from tkinter import *
from gtts import gTTS
from playsound import playsound
from datetime import datetime
from PIL import Image, ImageTk
import threading



################### INITIALIZED WINDOW ####################

root = Tk()
root.geometry('350x300')
root.resizable(0,0)
root.config(bg = 'black')
root.title('SIDHARTH - TEXT2SPEECH')


# HEADING
Label(root, text = 'TEXT2SPEECH' , font='arial 20 bold' , bg ='#3555E2').pack()
Label(root, text ='SIDHARTH' , font ='arial 15 bold', bg = '#3555E2').pack(side = BOTTOM)




# LABEL
Label(root, text ='Enter Text', font ='arial 15 bold', bg ='#3555E2').place(x=20,y=60)


# TEXT VARIABLE
Msg = StringVar()


# ENTRY
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)


################### FUNCTION DEFINITION ##############################

# Function to play the GIF
def play_gif():
    gif_path = "Voice_Visualisation.gif"  # Replace with the path to your GIF file
    
    # Open the GIF using PIL
    gif_image = Image.open(gif_path)

    # Create a label to display the GIF frames
    gif_label = Label(root)
    gif_label.place(x=87,y=200)

    # Function to update the GIF frames
    def update_label():
        try:
            gif_image.seek(gif_image.tell() + 1)
            frame = gif_image.copy()
            photo = ImageTk.PhotoImage(frame)
            gif_label.config(image=photo)
            gif_label.image = photo  # Keep a reference to prevent garbage collection
            root.after(gif_image.info['duration'], update_label)
        except EOFError:
            pass

    # Start the animation
    update_label()

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice"+date_string+".mp3"
    speech.save(filename)
    playsound(filename)

def start_functions():
    thread1 = threading.Thread(target=Text_to_speech)
    thread2 = threading.Thread(target=play_gif)

    thread1.start()
    thread2.start()
    
def Exit():
    root.destroy()

def Reset():
    Msg.set("")

# BUTTONS
Button(root, text = "PLAY" , font = 'arial 15 bold', command = start_functions,bg= 'green', width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed1').place(x=100,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset).place(x=175 , y =140)


# FOR RUNNING THE PROGRAM CONTINUOSLY
root.mainloop()
