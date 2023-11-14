import tkinter as tk
from PDFMover import PDFMover

# Specify source path, from which .pdf files will be taken, 
# and target path where files will land 
pdf_mover = PDFMover('<source_path>', '<target_path>')


m = tk.Tk()
m.title('PDF Mover')
m.geometry('200x80')
m.columnconfigure(0, weight=1)
m.rowconfigure(0, weight=1)

container = tk.Frame(m, bg='tan')
container.grid(row=0, column=0)


button = tk.Button(m, text='Move files', width=25, command=pdf_mover.move_files(), cursor="hand2")
button.grid(pady=20, padx=10)

m.mainloop()