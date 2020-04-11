import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd
from qbreport_to_csv import create_df, transform, export_to_csv

def open_file():
    """Open the XLSX file to transform."""
    file = askopenfilename(
            filetypes=[("Excel Files", "*.xlsx")]
            )
    if not file:
        return
    df = create_df(file)
    df = transform(df)
    df.to_csv('test.csv', index=False)

window = tk.Tk()
window.geometry("400x400")
window.title("QB to CSV")

btn_open = tk.Button(window, text="Open", command=open_file)
btn_open.pack()

window.mainloop()

