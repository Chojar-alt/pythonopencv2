import cv2
from tkinter import *
from tkinter import filedialog
from PIL import Image

file_path = ""
file_path2 = ""
image = ""


def get_file_path():
 global file_path
 file_path = filedialog.askopenfilename(title="Wybierz plik", filetypes=(("jpg", "*.jpg"), ("png", "*.png")))
 l1 = Label(window, text=file_path).pack()


def get_file_path2():
 global file_path2
 file_path2 = filedialog.askopenfilename(title="Wybierz plik", filetypes=(("jpg", "*.jpg") ,("png", "*.png") ))
 l2 = Label(window, text=file_path2).pack()

def swapface():
 global file_path
 global file_path2
 global image
 image = cv2.imread(file_path)
 image2 = cv2.imread(file_path2)
 imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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
 im_pil.save(a)



window = Tk()
window.title("Po wybraniu zamknij okno...")
window.geometry("450x200")
label1 = Label(window, text = "Wybierz 1:").place(x = 5, y = 0)
label2 = Label(window, text = "Wybierz 2:").place(x = 5, y = 25)
label3 = Label(window, text = "Sprawdź ").place(x = 5, y = 55)
b1 = Button(window, text = "Pierwsze zdjecie", command = get_file_path).pack()
b2 = Button(window, text = "Drugie zdjecie", command = get_file_path2).pack()
b3 = Button(window, text = "Pokaz efekt", command = showface).pack()
b4 = Button(window, text = "Zapisz jako", command = saveas).pack()

window.mainloop()

cv2.waitKey(0)
cv2.destroyAllWindows()