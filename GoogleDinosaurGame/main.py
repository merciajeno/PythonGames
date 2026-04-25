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
    canvas.move(ground1,-5,0)
    canvas.move(ground2,-5,0)
    x1 = canvas.coords(ground1)
    x2 = canvas.coords(ground2)
    if x1[2] < 0:
        canvas.coords(ground1, x2[2], x2[3], x2[2] + 400, x2[3])
    if x2[2] < 0:
        canvas.coords(ground2, x1[2], x1[3], x1[2] + 400, x1[3])
    print(x1)
    print(x2)
    canvas.after(30,move_dino)

#  Convert to Tkinter-compatible photo
tk_img = ImageTk.PhotoImage(resized_img)
ground_y = 150
ground1 = canvas.create_line(0,ground_y,400,ground_y,width=3)
ground2 = canvas.create_line(400,ground_y,800,ground_y,width=3)
# Add image to canvas (x, y coordinates)
dino = canvas.create_image(0, ground_y-50, anchor="nw", image=tk_img)
move_dino()
root.mainloop()
