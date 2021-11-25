import cv2
import numpy as np
#import dlib
from math import hypot
from tkinter import *
from tkinter import filedialog

file_path = ""
file_path2 = ""
image = ""
file = ""

def get_file_path():
 global file_path
 file_path = filedialog.askopenfilename(title="Wybierz plik", filetypes=(("jpg", "*.jpg"), ("png", "*.png")))
 #print("sciezka : {}".format(file_path))
 l1 = Label(window, text=file_path).pack()


def get_file_path2():
 global file_path2
 file_path2 = filedialog.askopenfilename(title="Wybierz plik", filetypes=(("jpg", "*.jpg") ,("png", "*.png") ))
 l2 = Label(window, text=file_path2).pack()

def swapface():
 global file_path
 global file_path2

 #print("sciezka : {}".format(file_path))
 image = cv2.imread(file_path)
 image2 = cv2.imread(file_path2)
 #print (image)
 imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 face_Cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
 faces = face_Cascade.detectMultiScale(imgGray, 1.1, 4)
 for (x, y, w, h) in faces:
  image[x:x + w, y:y + h] = cv2.resize(image2, (w, h))
  cv2.imshow('img', image)
  window.destroy()



window = Tk()
window.title("Po wybraniu zamknij okno...")
window.geometry("450x300")
label1 = Label(window, text = "Wybierz 1:").place(x = 5, y = 0)
label2 = Label(window, text = "Wybierz 2:").place(x = 5, y = 25)
label3 = Label(window, text = "Sprawdź ").place(x = 5, y = 55) # testy
b1 = Button(window, text = "Pierwsze zdjecie", command = get_file_path).pack()
b2 = Button(window, text = "Drugie zdjecie", command = get_file_path2).pack()
b3 = Button(window, text = "Pokaz efekt", command = swapface).pack()
window.mainloop()

cv2.waitKey(0)
cv2.destroyAllWindows()