import tkinter as tk

root = tk.Tk()
root.geometry("400x600")
root.title("Calculator")
buttonsize = 50

lbl_display = tk.Label(root, text="0", font="Arial 20", bg="Grey")
lbl_display.place(x=0, y=20, width=400, height=170)

h_diff = 1
w_diff = 0

for i in range(10):
    btn_numbtn = tk.Button(root, text=i, font="Arial 20")
    
    
    btn_numbtn.place(x=buttonsize*(w_diff), y=600-(buttonsize*h_diff), width=buttonsize, height=buttonsize)

    if w_diff==3:
        h_diff += 1
        w_diff = 0
    else:
        w_diff += 1

root.mainloop()