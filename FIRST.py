# Import Libraries or Setup enviroment
import cv2 as cv
import sys

# read image file
img=cv.imread("you_img_file",cv.IMREAD_GRAYSCALE) # in second argument , I'm changing color of image. By default , It is IMAGE_COLOR BGR (8-BIT format). You can use other formats. 

# by using sys module if output is none it stop the program
if img is None:
    sys.exit("Image is not Avaliable.")

# Display window of your image
cv.imshow("Display Window",img)

# This use for img wait untill any key is not press.
k=cv.waitKey(0)

# if key pressed is smallcase letter of 's' then it saves your image in cwd.
if k==ord("s"):

  # this use for saving file in your current working directory.
    cv.imwrite("hE.png",img)
