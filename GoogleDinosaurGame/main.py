import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Google Dino Runner")

# 1. Improved UI Styling
BG_COLOR = "#202124"  # Dark theme like Google Chrome's offline page
GROUND_COLOR = "#5f6368"
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 300

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BG_COLOR, highlightthickness=0)
canvas.pack(pady=20)

# Load and resize image
try:
    img = Image.open("dino.png")
    resized_img = img.resize((50, 50), Image.Resampling.LANCZOS)
    tk_img = ImageTk.PhotoImage(resized_img)
except:
    # Fallback if you don't have the image file handy
    tk_img = None

# Game Constants
ground_y = 220

# 2. Add a Score Label
score = 0
score_label = canvas.create_text(530, 30, text=f"HI  {score:05d}", fill="white", font=("Courier", 16, "bold"))

# 3. Create elements with cleaner colors
ground1 = canvas.create_line(0, ground_y, CANVAS_WIDTH, ground_y, fill=GROUND_COLOR, width=2)
ground2 = canvas.create_line(CANVAS_WIDTH, ground_y, CANVAS_WIDTH * 2, ground_y, fill=GROUND_COLOR, width=2)

# Obstacle (The Tree)
tree = canvas.create_rectangle(500, ground_y - 40, 525, ground_y, fill="#81b214", outline="")

# Dino
if tk_img:
    dino = canvas.create_image(50, ground_y - 50, anchor="nw", image=tk_img)
else:
    dino = canvas.create_rectangle(50, ground_y - 50, 100, ground_y, fill="gray")


def move_dino():
    global score

    # Speed of the game
    speed = -7
    canvas.move(tree, speed, 0)
    canvas.move(ground1, speed, 0)
    canvas.move(ground2, speed, 0)

    # Collision Detection
    dino_box = canvas.bbox(dino)
    tree_box = canvas.coords(tree)

    # Simple Logic for Score
    score += 1
    canvas.itemconfig(score_label, text=f"HI  {score:05d}")

    # Check for Collision
    if (dino_box[2] > tree_box[0] and dino_box[0] < tree_box[2] and
            dino_box[3] > tree_box[1]):
        canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, text="G A M E  O V E R",
                           fill="red", font=("Courier", 24, "bold"))
        return

    # Reset Ground for infinite loop
    x1 = canvas.coords(ground1)
    x2 = canvas.coords(ground2)
    if x1[2] < 0:
        canvas.coords(ground1, x2[2], ground_y, x2[2] + CANVAS_WIDTH, ground_y)
    if x2[2] < 0:
        canvas.coords(ground2, x1[2], ground_y, x1[2] + CANVAS_WIDTH, ground_y)

    # Reset Tree
    if tree_box[2] < 0:
        canvas.coords(tree, CANVAS_WIDTH + 50, ground_y - 40, CANVAS_WIDTH + 75, ground_y)

    canvas.after(20, move_dino)


move_dino()
root.mainloop()