import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def load_data():
    excel_file = "Bug_Report_Tamim.xlsx"
    file_path = resource_path(excel_file)
    
    try:
        df = pd.read_excel(file_path)
        
        tree.delete(*tree.get_children())
        
        for index, row in df.iterrows():
            tree.insert("", "end", values=list(row))
    except FileNotFoundError:
        messagebox.showerror("Error", f"Could not find '{excel_file}'.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
# --- Sorting Function for Severity ---
def sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    
    if col == "Severity":
        severity_rank = {"High": 1, "Medium": 2, "Low": 3}
        l.sort(key=lambda t: severity_rank.get(t[0].strip(), 4), reverse=reverse)
    else:
        l.sort(reverse=reverse)
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)
    tv.heading(col, command=lambda: sort_column(tv, col, not reverse))

def on_double_click(event):
    selected_item = tree.selection()
    if not selected_item:
        return
        
    item = selected_item[0]
    values = tree.item(item, "values")
    
    #pop-up window
    detail_win = tk.Toplevel(root)
    detail_win.title(f"Bug Details - {values[0]}")
    detail_win.geometry("600x450")
    detail_win.configure(bg="#ffffff")
    
    text_widget = tk.Text(detail_win, wrap="word", font=("Arial", 11), bg="#f9f9f9", padx=15, pady=15)
    text_widget.pack(fill="both", expand=True, padx=10, pady=10)
    
    details = f"Bug ID: {values[0]}\n"
    details += f"Severity: {values[5]}\n"
    details += "-"*60 + "\n\n"
    details += f"Title:\n{values[1]}\n\n"
    details += f"Steps to Reproduce:\n{values[2]}\n\n"
    details += f"Expected Result:\n{values[3]}\n\n"
    details += f"Actual Result:\n{values[4]}\n\n"
    details += f"Screenshot Link:\n{values[6]}\n"
    
    text_widget.insert("1.0", details)
    text_widget.config(state="disabled") 

# --- main ui ---
root = tk.Tk()
root.title("Bug Reporter - Md. Tahmid Shah Tamim")
root.geometry("1100x550")
root.configure(bg="#f4f4f9")

header = tk.Label(root, text="Intern SQA Engineer Task - Supporters Frame", font=("Helvetica", 18, "bold"), bg="#f4f4f9", fg="#2c3e50")
header.pack(pady=15)

instruction = tk.Label(root, text="(Double-click on any row to view full details | Click headers to sort)", font=("Arial", 10, "italic"), bg="#f4f4f9", fg="#7f8c8d")
instruction.pack(pady=0)

frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=20, pady=10)

columns = ("Bug ID", "Bug Title", "Steps to Reproduce", "Expected Result", "Actual Result", "Severity", "Screenshot")
tree = ttk.Treeview(frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col, command=lambda c=col: sort_column(tree, c, False))
    if col == "Bug ID" or col == "Severity":
        tree.column(col, width=80, anchor="center")
    elif col == "Screenshot":
        tree.column(col, width=120, anchor="center")
    else:
        tree.column(col, width=200, anchor="w")

tree.bind("<Double-1>", on_double_click)


y_scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
x_scroll = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.pack(side="right", fill="y")
x_scroll.pack(side="bottom", fill="x")
tree.pack(side="left", fill="both", expand=True)

btn_frame = tk.Frame(root, bg="#f4f4f9")
btn_frame.pack(pady=10)

load_btn = tk.Button(btn_frame, text="Refresh Data", font=("Arial", 11, "bold"), bg="#27ae60", fg="white", command=load_data, padx=15, pady=5, cursor="hand2")
load_btn.pack()

load_data()
root.mainloop()