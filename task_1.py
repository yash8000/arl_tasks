# if img is not None and img.shape[0] > 0 and img.shape[1] > 0:
#     # Display the image
#     cv.imshow("picasso", img)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
# else:
#     print("Invalid image dimensions. Unable to display the image.")


import cv2 as cv
import numpy as np
import random

img=cv.imread("C:\\Users\\YASH AGARWAL\\Downloads\\artwork_picasso.png")
# img=cv.imread('Photos/cats.jpg')
# img=cv.resize(img,(7,7))
print(img.shape)
# output = np.zeros_like(image1)
output_and = np.zeros((img.shape[0], img.shape[1] ), dtype=np.uint8)
output_or = np.zeros((img.shape[0], img.shape[1] ), dtype=np.uint8)
output_xor = np.zeros((img.shape[0], img.shape[1] ), dtype=np.uint8)
print(output_or)
j=0
i=0
for k in range(img.shape[0]*img.shape[0]-2):
        
        pixel1=img[i,j]
        if j<img.shape[1]-2:
            pixel2=img[i,j+2]
        # print(pixel1)
        # print(pixel2)
        j=j+1
        if i==img.shape[0] and j==img.shape[1]-2:
              break
        if j==img.shape[0]:
              i=i+1
              j=0
        
            
            
        result_and=cv.bitwise_and(pixel1,pixel2)
        # print(result_and)
        result_or=cv.bitwise_or(pixel1,pixel2)
        # print(result_or)
        result_xor=cv.bitwise_xor(pixel1,pixel2)
        # print(result_xor)
        
        output_and[i,j]=result_and[1]
        output_or[i,j]=result_or[1]
        output_xor[i,j]=result_xor[1]
        # print(output_and)
        # print(output_or)
        # print(output_xor)

cv.imshow("and",output_and)        
cv.imshow("or",output_or)        
cv.imshow("xor",output_xor)        
cv.imshow("picasso",img)

template=cv.resize(output_and,(100,100))
cv.imshow("final template",template)

t=cv.imread("C:\\Users\\YASH AGARWAL\\Downloads\\collage.png")
t_gray=cv.cvtColor(t,cv.COLOR_BGR2GRAY)
#now not need to print the map
cv.imshow("map",t)
cv.imshow("map_gray",t_gray)







result = cv.matchTemplate(t_gray,template, cv.TM_CCOEFF_NORMED)

# Define a threshold to determine a match
threshold = 0.1

# Locate the positions of matches above the threshold
positions = np.where(result >= threshold)
# print("poistions")
# print(positions)
# Get the coordinates of the top-left corners of the matched regions
matched_coordinates = []
for (x, y) in zip(positions[1], positions[0]):
    matched_coordinates.append((x, y))

# # Display the result
# for (x, y) in matched_coordinates:
#     # Draw a rectangle around the matched region
#     w, h = cropped_gray.shape[::-1]
#     cv.rectangle(t, (x, y), (x + w, y + h), (255, 255, 0), 2)

# Display the result
# cv.imshow('Result', t_gray)




# print("printing random")
# print(matched_coordinates)
# print(t.shape)

# password==[(100+100)*pi]=628

maze=cv.imread("C:\\Users\\YASH AGARWAL\\Downloads\\maze.png")
cv.imshow("maze",maze)
print("the sahpe of the maze")
print(maze.shape)




cv.waitKey(0)
cv.destroyAllWindows()
# cv.waitKey(0)