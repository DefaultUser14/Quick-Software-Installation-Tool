import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import installer
import os
import threading
import icon
import loader

def run():

    def close():
        try:
            os.remove(iconico)
        except Exception:
            pass
        window.destroy()

    def update_start_button(*args):
        start_button.state(["disabled"])
        for i in checkbox_list:
            if "selected" in i.state():
                start_button.state(["!disabled"])
                break

    def start_install(*args):
        start_button.state(["disabled"])
        update_log("STARTING\n")

        package_list = []
        n = 0
        for i in checkbox_list:
            if "selected" in i.state():
                package_list.append(software_list[n])                        
            n += 1      
            i.state(["disabled"])   

        thread = threading.Thread(target=installer.install_software, args = (package_list, update_log), daemon=True)
        thread.start()

    def update_log(new_log, tag=None):
        window.after(0, append_log, new_log, tag)

    def append_log(new_log, tag):
        window_log_output.config(state="normal")
        window_log_output.insert(tk.END, new_log, tag)
        window_log_output.see(tk.END)
        window_log_output.config(state="disabled")

    iconico = icon.GET_ICON()
    software_list = loader.scan_packages()
    
# Main Window
    window = tk.Tk()
    window.after(10, lambda: (window.state("normal"), window.lift(), window.focus_force()))
    window.title('Quick Install Tool')
    window.iconbitmap(iconico)
    window.minsize(width=320,height=100)
    window.resizable(False,False)
    window.columnconfigure(0, weight = 1)
    window.rowconfigure(0, weight = 1)

    window_main = ttk.Frame(master=window)
    window_main.columnconfigure(1, weight = 1)

# Left Side
    window_leftside = ttk.Frame(master=window_main)
    window_leftside.columnconfigure(0, weight = 1)
    window_leftside.rowconfigure(0, weight = 1)
    window_leftside.rowconfigure(1, weight=1)

    window_programs = ttk.Frame(master=window_leftside)
    window_programs.columnconfigure(0, weight = 1)
    window_programs.rowconfigure(0, weight = 1)

    row_n = 0
    checkbox_list = []
    for i in software_list:
        i = i.split('.', 1)[0]
        checkbox = ttk.Checkbutton(master=window_programs, text=i, command=update_start_button)
        checkbox.state(["!alternate"])
        if row_n == 0:
            checkbox.grid(column=0, row=row_n,sticky="w", pady=(15,3),padx=(5,0))
        else: 
            checkbox.grid(column=0, row=row_n,sticky="w", pady=3, padx=(5,0))
        checkbox_list.append(checkbox)
        row_n +=1


    window_buttons = ttk.LabelFrame(master=window_leftside)
    window_buttons.columnconfigure(0, weight = 1)
    window_buttons.rowconfigure(0, weight = 1)

    start_button = ttk.Button(master=window_buttons, text="Start", command=start_install)
    start_button.grid(column=0,row=0, sticky="we", padx=5,pady=2)
    start_button.state(["disabled"])

    exit_button = ttk.Button(master=window_buttons, text="Exit", command=close)
    exit_button.grid(column=0,row=1, sticky="we", padx=5,pady=2)

# Right Side
    window_logs = ttk.LabelFrame(master=window_main, text="Logs")
    window_logs.columnconfigure(0, weight = 1)
    window_logs.rowconfigure(0, weight = 1)


    window_log_output = scrolledtext.ScrolledText(master=window_logs,wrap="word", state="disabled", height=0, width= 20)
    window_log_output.tag_config('error', foreground="red")
    window_log_output.tag_config('success', foreground="green")

# Loop
    window_main.grid(row=0,column= 0, sticky="nswe")
    window_leftside.grid(row=0,column=0, sticky="nswe")
    window_programs.grid(row=0,column=0,sticky="nwe")
    window_buttons.grid(row=1,column=0, sticky="swe", padx=5, pady=5)
    window_logs.grid(row=0,column=1, sticky="nswe",padx=5,pady=5 )
    window_log_output.grid(row=0,column=0,sticky="nswe",pady=(0,5))

    window.protocol("WM_DELETE_WINDOW", close)

    window.mainloop()
