import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Load the image
img = tk.PhotoImage(file="dino.png")

# Add image to canvas (x, y coordinates)
canvas.create_image(20, 20, anchor="nw", image=img)

root.mainloop()
