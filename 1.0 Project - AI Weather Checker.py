from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import time

def start():
    # Main function to initiate the weather checking process
    if __name__=='__main__':
        Analysis = 100  # Total analysis to complete
        download = 0    # Counter for the downloaded data
        speed = 20      # Speed of download per iteration
        
        # Loop until the download is complete
        while (download < Analysis):
            time.sleep(1)  # Simulate time delay for data fetching
            # Update the progress bar value based on speed
            bar['value'] += (speed / Analysis) * 100
            download += speed  # Increase the downloaded data
            
            # Update the percentage and task status displayed to the user
            percent.set(str(int((download / Analysis) * 100)) + "%")
            text.set(str(download) + "/" + str(Analysis) + " Weather Inspection")
            window.update_idletasks()  # Update the UI
            
        # Once download is complete, open a new window with a message
        if (download == Analysis):
            print("opening tab")  # Print a message in the console
            new_window = Tk()  # Create a new Tkinter window

            # Create a label in the new window with a message
            label = Label(new_window,
                          text="idk go look outside",
                          font=(('Arial'), 20),
                          )
            label.pack()  # Pack the label into the window

            new_window.mainloop()  # Start the new window's main loop

# Main application window setup
window = Tk()
window.title("AI Weather Report")  # Set the window title

# String variables to hold percent and task text
percent = StringVar()
text = StringVar()

# Label to instruct the user
label = Label(window, text="This is an AI Weather Checker.\n    Where are you located?", font=(('Comic Sans'), 13))
label.pack()  # Pack the label into the window

entry = Entry(window)  # Entry widget for user input
entry.pack(side="top", pady=10, padx=30)  # Pack the entry with padding

# Progress bar to indicate download progress
bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=20, padx=20)  # Pack the progress bar with padding

# Labels to display percentage and task status
percent_label = Label(window, textvariable=percent).pack()
task_label = Label(window, textvariable=text).pack()

# Button to start the weather checking process
button = Button(window, text="Check Weather", command=start)
button.pack()  # Pack the button into the window

# Start the main event loop of the application
window.mainloop()
