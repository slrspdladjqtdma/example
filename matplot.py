import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv 

image = cv.imread('C:/Users/BigData/.vscode/example/yellow.png')
plt.figure()
plt.imshow(image)
plt.title("Original")
# plt.show()

rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
plt.figure()
plt.imshow(rgb)
plt.title("RGB")

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(gray, cmap='gray')
plt.title("GRAY")
plt.show()

blur = cv.blur(image, (50, 50))
blur = cv.cvtColor(blur, cv.COLOR_BGR2RGB)
plt.subplot(121)
plt.imshow(rgb)
plt.title("RGB")
plt.subplot(122)
plt.imshow(blur)
plt.title("BLur")
plt.show()

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(gray, cmap='gray')
plt.title('Gray')

edges = cv.Canny(gray, 100, 200)
plt.subplot(121)
plt.imshow(gray, cmap='gray')
plt.title("Gray")
plt.subplot(122)
plt.imshow(edges, cmap='gray')
plt.title("Edge Detection")

plt.show()