from tkinter import Tk, Canvas

root = Tk()
# Initialize canvas
canvas = Canvas(root, width=400, height=200, bg="white")
canvas.pack()

# Draw a red line
canvas.create_line(0, 0, 400, c200, fill="red")

# Draw a blue rectangle
canvas.create_rectangle(50, 50, 150, 150, fill="blue")

root.mainloop()
