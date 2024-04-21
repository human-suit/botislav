import imutils
import pyautogui as pg
import time
import cv2 as cv
import numpy as np
import mss
import keyboard
import random

green = np.uint8([[[203, 192, 255]]]) # Here insert the BGR values which you want to convert to HSV
hsvGreen = cv.cvtColor(green, cv.COLOR_BGR2HSV)
print(hsvGreen)

lowerLimit = hsvGreen[0][0][0] - 10, 100, 100
upperLimit = hsvGreen[0][0][0] + 10, 255, 255

print(upperLimit)
print(lowerLimit)



def get_monitor(x,y,w,h,sct):
    monitor = {"top": x, "left": y, 'width': w, 'height': h}
    img = np.array(sct.grab(monitor))
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    return hsv

with (mss.mss() as sct):
    # time.sleep(2)
    # img2 = get_monitor(102, 54, 80, 30, sct)
    time.sleep(1.5)
    # print("2")
    # try:
    #     x, y = pg.locateCenterOnScreen("C://Users/FilipStoyn/PycharmProjects/demo2/5.png")
    #     pg.rightClick(x, y, duration=1)
    #     print("1")
    # except:
    #     pass
    # # list = [376, 345, 451, 184, 617, 114]
    # # rand = [0, 2, 4]
    # # psw = random.choice(rand)
    # print(psw)
    # while True:
    x, y = pg.position()
    #     if 757> x >512 and 462> y >180:
    #         print("xa")
    #     if keyboard.is_pressed('q'):  # if key 'q' is pressed
    #         print('You Pressed A Key!')
    #         break
    print(x,y)
            # # img2 = cv.imread("start.png")255,192,203
    # object_detected = cv.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

    # img2 = cv.imread("4.png")
    up_range = np.array([((98, 255, 255))])  # 9, 255, 255
    low_range = np.array([(90, 50, 70)])
    # mask2 = cv.inRange(img2, low_range, up_range)
    # edges = cv.Canny(img2, 30, 200)
    # cont = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    # cont = imutils.grab_contours(cont)
    # cont = sorted(cont, key=cv.contourArea, reverse=True)
    # pos = None
    # for c in cont:
    #     aprox = cv.approxPolyDP(c, 10, True)
    #     if len(aprox) == 4:
    #         pos = aprox
    #         break
    # mask = np.zeros(gray.shape, np.uint8)
    # bit = cv.bitwise_and(img2, img2, mask=mask)
    # cv.imwrite("C:/Users/FilipStoyn/PycharmProjects/demo2/3.png",mask2)

    # cv.imshow("EE",img)
    # cv.waitKey(0)

# cv.destroyAllWindow()