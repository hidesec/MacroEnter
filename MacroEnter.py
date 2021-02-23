from keyboard import press
import time
from tkinter import *

root = Tk()
root.title("Auto Enter Catalist!")
root.geometry("250x250")

app = Frame(root)
app.grid()
label1 = Label(app, text= "Script Running!!", fg='green', font=('helvetica', 12, 'bold'))
label2 = Label(app, text= "Script Stop!!", fg='green', font=('helvetica', 12, 'bold'))

running = False  # Global flag
def scanning():
    if running:  # Only do this if the Stop button has not been clicked
        print("hello")
        time.sleep(4)
        press('enter')

    # After 1 second, call scanning again (create a recursive loop)
    root.after(1000, scanning)

def start():
    """Enable scanning by setting the global flag to True."""
    label1.grid()
    global running
    running = True

def stop():
    """Stop scanning by setting the global flag to False."""
    label2.grid()
    global running
    running = False


start = Button(app, text="Start Scan", command=start)
stop = Button(app, text="Stop", command=stop, bg="red")

start.grid(padx=100,pady=10)
stop.grid()
label3 = Label(app, text= "created by: Raihan H. Q.(@hidesec)", fg='black', font=('helvetica', 8, 'bold'))
label3.grid(pady=160)

root.after(1000, scanning)  # After 1 second, call scanning
root.mainloop()