import cv2
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Video Player")

canvas = tk.Canvas(root, width=600, height=1040)
canvas.pack()

cap = cv2.VideoCapture('logo_3.mp4')

width, height = 600, 340


def update_canvas():
    ret, frame = cap.read()
    if ret:
        resized = cv2.resize(frame, (width, height))
        img = Image.fromarray(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB))
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, image=photo, anchor='nw')
        canvas.photo = photo
        root.after(10, update_canvas)
    else:
        cap.release()
        root.destroy()


update_canvas()

root.mainloop()
