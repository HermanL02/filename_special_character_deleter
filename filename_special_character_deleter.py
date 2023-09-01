import os
import re
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def clean_filename(filename):
    # 使用正则表达式替换非字母、数字和中文的字符为''
    cleaned = re.sub('[^\u4e00-\u9fffA-Za-z0-9]', '', filename)
    return cleaned

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_path_var.set(folder_path)

def process_folder():
    folder_path = folder_path_var.get()
    if not folder_path:
        return

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            new_filename = clean_filename(filename)
            if new_filename != filename:
                new_full_path = os.path.join(folder_path, new_filename)
                os.rename(full_path, new_full_path)
                result_listbox.insert(tk.END, f"Renamed {filename} to {new_filename}")

# GUI setup
root = tk.Tk()
root.title("Clean File Names")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

folder_path_var = tk.StringVar()

folder_label = ttk.Label(frame, text="Folder:")
folder_label.grid(row=0, column=0, sticky=tk.W)

folder_entry = ttk.Entry(frame, textvariable=folder_path_var, width=40)
folder_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

browse_button = ttk.Button(frame, text="Browse", command=browse_folder)
browse_button.grid(row=0, column=2)

process_button = ttk.Button(frame, text="Process", command=process_folder)
process_button.grid(row=1, columnspan=3)

result_listbox = tk.Listbox(frame, height=15, width=50)
result_listbox.grid(row=2, columnspan=3, sticky=(tk.W, tk.E))

frame.columnconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)

root.mainloop()
