import tkinter as tk
from PIL import Image,ImageTk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Load the image
img = Image.open("dino.png")
new_width = 50
new_height = 50
resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

#  Convert to Tkinter-compatible photo
tk_img = ImageTk.PhotoImage(resized_img)
# Add image to canvas (x, y coordinates)
canvas.create_image(0, 100, anchor="nw", image=tk_img)

root.mainloop()
