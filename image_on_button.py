#image test

import tkinter as tk

root=tk.Tk()
b = tk.Button(root,justify = "left")
photo=tk.PhotoImage(file="tree.png")
b.config(image=photo,width="300",height="162")
b.pack(side="left")
root.mainloop()
