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

def move_dino():
    global x_speed, y_speed
    canvas.move(dino,x_speed,0)
    x_speed = x_speed+10
    canvas.after(500, move_dino)
#  Convert to Tkinter-compatible photo
tk_img = ImageTk.PhotoImage(resized_img)
# Add image to canvas (x, y coordinates)
dino = canvas.create_image(0, 100, anchor="nw", image=tk_img)
x_speed = 0
move_dino()
root.mainloop()
