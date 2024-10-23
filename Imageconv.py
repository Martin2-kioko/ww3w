import cv2
import numpy as np


# Reading the image
image = cv2.imread("C:\\Users\\ADMIN\\Desktop\\image.jpg")

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image. Check the file path and try again.")
else:
    # Converting to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Inverting the grayscale image
    inverted = 255 - gray_image

    # Applying Gaussian Blur
    blur = cv2.GaussianBlur(inverted, (21, 21), 0)

    # Inverting the blurred image
    invertedblur = 255 - blur

    # Creating the sketch effect
    sketch = cv2.divide(gray_image, invertedblur, scale=260.0)

    # Saving the sketch image to the Desktop
    cv2.imwrite("C:\\Users\\ADMIN\\Desktop\\sketch12_image.png", sketch)

    # Displaying the sketch image
    cv2.imshow("Image", sketch)
    cv2.waitKey(0)  # Keeps the window open until a key is pressed
    cv2.destroyAllWindows()  # Closes the window
