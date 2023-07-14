from utils import Player,WINDOW_WIDTH
import cv2
import numpy as np
from MapGeneration import generateMap,generateRandomStart
from utils import Player


player = Player()
    #Initializing a Player object with a random start position on a randomly generated Maze

def getMap(self):
    return self.__Map


def strategy():
    # img=getMap()
    img=generateMap()
    # cv2.imshow("map",img)
    
    # k=generateRandomStart()
    snapshot=player.getSnapShot()
    # cv2.imshow("snapppp",snapshot)
    cv2.waitKey(0)
    
    map=np.array(img)
    print(map)

    snap=np.array(snapshot)

    
    


    # print("see here manannajsnsjcsdj")
    # print(img.shape)
    # print(img.shape[0])
    # print(snap.shape)
    # print(map.shape)

    for i in range(map.shape[0]):
        for j in range(snap.shape[0]):
            if(i!=j):
                continue
            if(j==snap.shape[0]):
                print("the location you want is")
                print(i+21)
                print(j-21)



    print("the array")
    print(snap)

    print("image size",img.shape)
    print("array size",snap.shape)
     



    # Read the original image and the cropped part
    gray_image = generateMap()
    cv2.imshow("map",gray_image)
    
    gray_cropped_image = player.getSnapShot()
    cv2.imshow("snapshot",gray_cropped_image)

    # Convert the images to grayscale
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # gray_cropped_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

    # Find the cropped part within the original image
    result = cv2.matchTemplate(gray_image, gray_cropped_image, cv2.TM_CCORR_NORMED)
    threshold=0.8
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # Determine the location of the cropped part
    height, width = gray_cropped_image.shape
    top_left = max_loc
    bottom_right = (top_left[0] + width, top_left[1] + height)

    # Draw a rectangle around the found location
    cv2.rectangle(gray_image, top_left, bottom_right, (0, 255, 0), 2)
    print("the estimate location is")
    print("top left corner",top_left)
    print("bottom right corner",bottom_right)
    print("the estimated point",(top_left[0]+bottom_right[0])/2,(top_left[1]+bottom_right[1])/2)
    # Display the image with the location of the cropped part
    cv2.imshow("Result", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    # image = np.zeros((snapshot.shape[0], snapshot.shape[1], 3), dtype=np.uint8)
    # print(image)
    # # cv2.imshow("snap",snap)
    # # cv2.waitKey(0)
    # color_map = {
    #         0: (0, 0, 0),
    #         1: (255, 255, 255),  # White for empty spaces
    #                # Black for obstacles
    #     }

    #     # Fill the image with the corresponding colors from the snapshot
    # for i in range(snapshot.shape[0]):
    #     for j in range(snapshot.shape[1]):
    #         value = snapshot[i, j]
    #         color = color_map[value]
    #         image[i, j] = color

    #     # Display the image
    # print(image)    
    # cv2.imshow("Snapshot", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


if __name__ == "__main__":
     strategy()    