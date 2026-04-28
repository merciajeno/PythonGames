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
    canvas.move(tree, -5, 0)
    canvas.move(ground1,-5,0)
    canvas.move(ground2,-5,0)
    x1 = canvas.coords(ground1)
    x2 = canvas.coords(ground2)

    dino_box= canvas.bbox(dino)
    coords = canvas.coords(tree)
    dx1, dy1, dx2, dy2 = dino_box #dinosaur coordinates
    tx1, ty1, tx2, ty2 = coords #tree coordinates

    if tx1<dx2 and dy1 < ty2 and dy2 > ty1 and dx1<tx2:
        print("Collision!")
        return
    
    if coords[2]<0:
        canvas.coords(tree, 400, ground_y - 40, 420, ground_y)
    if x1[2] < 0:
        canvas.coords(ground1, x2[2], x2[3], x2[2] + 400, x2[3])
    if x2[2] < 0:
        canvas.coords(ground2, x1[2], x1[3], x1[2] + 400, x1[3])
    # print(x1)
    # print(x2)
    canvas.after(30,move_dino)

#  Convert to Tkinter-compatible photo
tk_img = ImageTk.PhotoImage(resized_img)
ground_y = 150
ground1 = canvas.create_line(0,ground_y,400,ground_y,width=3)
ground2 = canvas.create_line(400,ground_y,800,ground_y,width=3)
tree = canvas.create_rectangle(
    330, ground_y - 40,   # top-left
    350, ground_y,        # bottom-right
    fill="green"
)
# Add image to canvas (x, y coordinates)
dino = canvas.create_image(0, ground_y-50, anchor="nw", image=tk_img)
move_dino()
root.mainloop()
