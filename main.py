import cv2
import numpy as np
#import dlib
from math import hypot
from tkinter import *
from tkinter import filedialog
from PIL import Image

file_path = ""
file_path2 = ""
image = ""
image2 = ""
dst = ""


def get_file_path():
 global file_path
 file_path = filedialog.askopenfilename(title="Wybierz plik", filetypes=(("jpg", "*.jpg"), ("png", "*.png")))
 #print("sciezka : {}".format(file_path))
 l1 = Label(window, text=file_path).pack()


def get_file_path2():
 global file_path2
 file_path2 = filedialog.askopenfilename(title="Wybierz plik", filetypes=(("jpg", "*.jpg") ,("png", "*.png") ))
 l2 = Label(window, text=file_path).pack()

def deleatebackgorund():
 global file_path2
 global image2
 image2 = cv2.imread(file_path2)
 mask = np.zeros(image2.shape[:2], np.uint8)
 bgdModel = np.zeros((1, 65), np.float64)
 fgdModel = np.zeros((1, 65), np.float64)

 rect = (1, 30, 665, 344)
 cv2.grabCut(image2, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

 mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
 img = image2 * mask2[:, :, np.newaxis]
 # cv2.imshow('img',img)
 cv2.imwrite('img.png', img)
 file_name = "img.png"
 src = cv2.imread(file_name, 1)
 tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
 _, alpha = cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
 b, g, r = cv2.split(src)
 rgba = [b, g, r, alpha]
 dst = cv2.merge(rgba, 4)


def swapface():
 global file_path
 global file_path2
 global image
 #global image2
 global dst
 #print("sciezka : {}".format(file_path))
 image = cv2.imread(file_path)
# image2 = deleatebackgorund()
# image2 = cv2.imread(file_path2)
 imgGray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
 face_Cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
 faces = face_Cascade.detectMultiScale(imgGray, 1.1, 4)
 for (x, y, w, h) in faces:
  image[x:x + w, y:y + h] = cv2.resize(image2, (w, h))
  return image


def showface():
 global image
 swapface()
 window.destroy()
 cv2.imshow('img', image)

def saveas():
 global image
 swapface()
 image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 im_pil = Image.fromarray(image)
 a = filedialog.asksaveasfile(defaultextension=".jpg")
 print("sciezka : {}".format(a))
 im_pil.save(a)



window = Tk()
window.title("Po wybraniu zamknij okno...")
window.geometry("450x300")
label1 = Label(window, text = "Wybierz 1:").place(x = 5, y = 0)
label2 = Label(window, text = "Wybierz 2:").place(x = 5, y = 25)
label3 = Label(window, text = "Sprawdź ").place(x = 5, y = 55) # testy
b1 = Button(window, text = "Pierwsze zdjecie", command = get_file_path).pack()
b2 = Button(window, text = "Drugie zdjecie", command = get_file_path2).pack()
b3 = Button(window, text = "Pokaz efekt i zapisz", command = showface).pack()
b4 = Button(window, text = "save  as", command = saveas).pack()

window.mainloop()

cv2.waitKey(0)
cv2.destroyAllWindows()