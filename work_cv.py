#Image reading with numpy and matplotlib
import numpy as np#for nd arrays
import matplotlib.pyplot as plt#for visualisations
from PIL import Image #Python Imaging Library
zeros_arr=np.zeros((3,3),dtype=int)
print(zeros_arr)
ones_arr=np.ones((5,5),dtype=int)
print(ones_arr)
print(ones_arr*255)
img = Image.open(r'C:\Users\Lenovo\Desktop\workshops\cv_for_genAI\horse1.jpg')
print(img)
print(plt.imshow(img))
print(plt.show())
img_to_arr = np.asarray(img)
print(img_to_arr)
print(type(img_to_arr))
print(img_to_arr.shape)
img2 = img.copy()
img2 == img
img2 = np.array(img2)
print(img2)
print(plt.imshow(img2))
print(plt.show())
print(plt.imshow(img2[:,:,0]))
print(plt.show())
print(plt.imshow(img2[:,:,0],cmap='gray'))
print(plt.show())
