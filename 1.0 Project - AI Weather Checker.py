from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import time


def start():
    if __name__=='__main__':
        Analysis = 100
        download = 0
        speed = 20
        while (download<Analysis):
            time.sleep(1)
            bar['value']+=(speed/Analysis)*100
            download+=speed
            percent.set(str(int((download/Analysis)*100))+"%")
            text.set(str(download)+"/"+str(Analysis)+" Weather Inspection")
            window.update_idletasks()
        if (download == Analysis):
            print("opening tab")
            new_window = Tk()

            label = Label(new_window,
                          text= "idk go look outside",
                          font=(('Arial'),20),
                          )
            label.pack()

            new_window.mainloop()


window = Tk()
window.title("AI Weather Report")

percent = StringVar()
text = StringVar()

label = Label(window, text= "This is an AI Weather Checker.\n    Where are you located?", font=(('Comic Sans'),13))
label.pack()

entry = Entry(window)
entry.pack(side= "top",pady=10, padx=30)


bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=20, padx= 20)

percent_label = Label(window, textvariable=percent).pack()
task_label = Label(window, textvariable=text).pack()


button = Button(window, text="Check Weather", command=start)
button.pack()

window.mainloop()
