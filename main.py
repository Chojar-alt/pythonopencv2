import cv2
import numpy as np
import dlib
from math import hypot
from tkinter import *
from tkinter import filedialog

image = None
image2 = None
global file_path
global file_path2

class App(object):


  def __init__(self):
   self.image = cv2.imread(self.file_path)
   self.image2 = cv2.imread(self.file_path2)
  def file_path(self):
   self.file_path = filedialog.askopenfilename(title="Wybierz plik", filetypes=(("jpg", "*.jpg"), ("png", "*.png")))
   l1 = Label(window, text=self.file_path).pack()
  def file_path2(self):
   self.file_path2 = filedialog.askopenfilename(title="Wybierz plik", filetypes=(("jpg", "*.jpg") ,("png", "*.png") ))
   l2 = Label(window, text=self.file_path2).pack()

  def faceswap(self):
   imgGray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
   face_Cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
   faces = face_Cascade.detectMultiScale(imgGray, 1.1, 4)
   for (x, y, w, h) in faces:
    self.image[x:x + w, y:y + h] = cv2.resize(self.image2, (w, h))

   cv2.imshow(self.image)

class AppRun(App):

  window = Tk()
  window.title("Po wybraniu zamknij okno...")
  window.geometry("400x130")
  label1 = Label(window, text = "Wybierz 1:").place(x = 5, y = 0)
  label2 = Label(window, text = "Wybierz 2:").place(x = 5, y = 25)
  label3 = Label(window, text = "(test)Zapisz jako:").place(x = 5, y = 55) # testy
  b1 = Button(window, text = "Pierwsze zdjecie", command = App.file_path(self=file_path)).pack()
  b2 = Button(window, text = "Drugie zdjecie", command = App.file_path2(file_path2)).pack()
  b3 = Button(window, text = "Pokaz efekt", command = App.faceswap(self=None)).pack()

  window.mainloop()
  cv2.waitKey(0)
  cv2.destroyAllWindows()