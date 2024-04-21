import imutils
import pyautogui as pg
import time
import cv2 as cv
import numpy as np
import mss
import random
import keyboard

# def get_color(x, y):
#     m = mss()
#     monitor = {
#         "left": x,
#         "top": y,
#         "width": 1,
#         "height":1
#     }
#     img = m.grab(monitor)
#     img_arr = np.array(img)
#     print(img_arr)
start_time = time.time()
current_time = time.time() - start_time
minutes = int(current_time // 60)
def get_monitor(x,y,w,h,sct):
    monitor = {"top": x, "left": y, 'width': w, 'height': h}
    img = np.array(sct.grab(monitor))
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    return hsv


def refresh(sct):
    x, y = pg.size()
    img3 = get_monitor(0, 0, x, y, sct)

    up_range = np.array([89, 255, 255])  # 9, 255, 255
    low_range = np.array([36, 50, 70])  # 0, 50, 70
    mask = cv.inRange(img3, low_range, up_range)
    arrayMask = getmask(mask)
    dMo1 = arrayMask[0]
    dMo10 = arrayMask[1]
    dArea = arrayMask[2]
    if dArea > 100:
        x = int(dMo10 / dArea)
        y = int(dMo1 / dArea)
        pg.moveTo(x, y)
        getStart()
# def coloram():
# color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
#               'white': [[180, 18, 255], [0, 0, 231]],
#               'red1': [[180, 255, 255], [159, 50, 70]],
#               'red2': [[9, 255, 255], [0, 50, 70]],
#               'green': [[89, 255, 255], [36, 50, 70]],
#               'blue': [[128, 255, 255], [90, 50, 70]],
#               'yellow': [[35, 255, 255], [25, 50, 70]],
#               'purple': [[158, 255, 255], [129, 50, 70]],
#               'orange': [[24, 255, 255], [10, 50, 70]],
#               'gray': [[180, 18, 230], [0, 0, 40]]}

def getmask (mask):
    moments = cv.moments(mask, 1)
    dMo1 = moments['m01']
    dMo10 = moments['m10']
    dArea = moments['m00']
    return dMo1,dMo10,dArea
def proverka(sct):
    image = get_monitor(102, 54, 80, 30, sct)
    up_range = np.array([((98, 255, 255))])  # 9, 255, 255
    low_range = np.array([(90, 50, 70)])  # 0, 50, 70
    maska = cv.inRange(image, low_range, up_range)
    arrayMa = getmask(maska)
    dArea5 = arrayMa[2]
    time.sleep(0.2)
    if dArea5 < 80:
        time.sleep(0.5)
        keyboard.press("1")
        keyboard.release("1")
        time.sleep(2.5)
        image = get_monitor(102, 54, 80, 30, sct)
        up_range = np.array([((98, 255, 255))])  # 9, 255, 255
        low_range = np.array([(90, 50, 70)])  # 0, 50, 70
        maska = cv.inRange(image, low_range, up_range)
        arrayMa = getmask(maska)
        dArea5 = arrayMa[2]
        if dArea5 < 80:
            # try:
            #     x, y = pg.locateCenterOnScreen("C://Users/FilipStoyn/PycharmProjects/demo2/5.png")
            #     pg.rightClick(x, y, duration=1)
            #     print("1")
            # except:
            #     pass
            pg.keyDown("tab")
            pg.moveTo(1132, 429)
            time.sleep(1.3)
            pg.click(button='right')
            pg.keyUp("tab")
            pg.keyDown("tab")
            time.sleep(0.7)
            keyboard.press("1")
            keyboard.release("1")
    if dArea5 > 70:
        print("nice")


def proverka2(sct):
    image = get_monitor(102, 54, 80, 30, sct)
    up_range = np.array([((24, 255, 255))])  # 9, 255, 255
    low_range = np.array([(10, 50, 70)])  # 0, 50, 70
    maska = cv.inRange(image, low_range, up_range)
    arrayMa = getmask(maska)
    dArea5 = arrayMa[2]
    if dArea5 < 80:
        keyboard.press("2")
        keyboard.release("2")
        time.sleep(2)
def getStart():
    time.sleep(1)
    with (mss.mss() as sct):
        proverka(sct)
        proverka2(sct)
        x, y = pg.size()
        last_time = time.time()
        hsv = get_monitor(0, 0, x, y,sct)

        color_yeal = (0, 255, 255)

        current_time = time.time() - start_time
        minutes2 = int(current_time // 60)
        up_range = np.array([128, 255, 255])  # 128, 255, 255
        low_range = np.array([90, 50, 70])  # [90, 50, 70]
        mask = cv.inRange(hsv, low_range, up_range)
        arrayMask = getmask(mask)
        dMo1 = arrayMask[0]
        dMo10 = arrayMask[1]
        dAreablue = arrayMask[2]
        hsv2 = get_monitor(0, 0, x, y, sct)
        up_ranges = np.array([158, 255, 255])
        low_ranges = np.array([129, 50, 70])
        mask = cv.inRange(hsv2, low_ranges, up_ranges)
        arrayMask3 = getmask(mask)
        dMo3 = arrayMask3[0]
        dMo30 = arrayMask3[1]
        dAreaperpel = arrayMask3[2]
        Drea1 = None
        if dAreablue > dAreaperpel:
            Drea1 = dAreablue
            x3 = int(dMo10 / Drea1)
            y3 = int(dMo1 / Drea1)
            spleh = 0.6
        if dAreaperpel > dAreablue:
            Drea1 = dAreaperpel
            x3 = int(dMo30 / Drea1)
            y3 = int(dMo3 / Drea1)
            list = [10, 20]
            rand = [0, 1]
            psw = random.choice(rand)
            minx = list[psw]
            x3 = x3 - minx
            spleh = 0.5
        else:
            Drea1 = dAreablue
            x3 = int(dMo10 / Drea1)
            y3 = int(dMo1 / Drea1)
            list = [10, 20]
            rand = [0, 1]
            psw = random.choice(rand)
            minx = list[psw]
            x3 = x3 - minx
            spleh = 0.6
        pro=x3
        pro2=y3
        if 825> pro >420 and 462> pro2 >160:
            list = [393, 184]
            rand = [0]
            psw = random.choice(rand)
            x3=list[psw]
            y3=list[psw+1]
            spleh=0.5
            print("lol")
        print(x3)
        print(y3)
        pg.moveTo(x3, y3, duration=0.2)
        pg.mouseDown(button='left')
        time.sleep(spleh)
        pg.mouseUp(button='left')
        time.sleep(1)
        start3 = time.time()
        current_time = time.time() - start3
        seconds = int(current_time % 60)
        k=0
        while "Screen capturing":
            current_time = time.time() - start3
            seconds2 = int(current_time % 60)
            img = get_monitor(768 - (768 - y3) - 55, 1360 - (1360 - x3) - 55, 160, 160,sct)
            # cv.imwrite("C:/Users/FilipStoyn/PycharmProjects/demo2/3.png", img)
            up_range = np.array([9, 255, 255])  # 9, 255, 255
            low_range = np.array([0, 50, 70])  # 0, 50, 70
            mask = cv.inRange(img, low_range, up_range)
            arrayMask = getmask(mask)
            dMo1 = arrayMask[0]
            dMo10 = arrayMask[1]
            dArea = arrayMask[2]
            if dArea > 10:
                ran = random.randint(35,37)
                if seconds + ran == seconds2:
                    pg.click()
                    refresh(sct)
                if (k == 0):
                    k +=1
                    x = int(dMo10 / dArea)
                    y = int(dMo1 / dArea)
                    x2 = x
                    y2 = y
                else:
                    k += 1
                    x2 = int(dMo10 / dArea)
                    y2 = int(dMo1 / dArea)

                if (x2 > x + 4 or y2 > y + 4):
                    start = time.time()
                    current_time = time.time() - start
                    seconds = int(current_time % 60)
                    pg.leftClick()
                    time.sleep(0.3)
                    while True:
                        img2 = get_monitor(344, 538, 120, 40, sct)
                        up_range = np.array([((40, 255, 255))])  # 9, 255, 255
                        low_range = np.array([(20, 100, 100)])  # 0, 50, 70
                        mask2 = cv.inRange(img2, low_range, up_range)
                        arrayMask = getmask(mask2)
                        dArea2 = arrayMask[2]
                        if dArea2 > 10:
                            pg.mouseDown(button='left')

                        else:
                            pg.mouseUp(button='left')

                        current_time = time.time() - start
                        seconds2 = int(current_time % 60)
                        # elapsed_time = start2
                        # print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

                        if seconds+16 == seconds2:
                            refresh(sct)

                        cv.imwrite("C:/Users/FilipStoyn/PycharmProjects/demo2/3.png", mask2)
                        cv.imwrite("C:/Users/FilipStoyn/PycharmProjects/demo2/4.png", img2)
                        cv.waitKey(0)


                cv.circle(img, (x, y), 5, (0, 0, 255), -1)
                cv.circle(img, (x2, y2), 2, color_yeal, 2)

            else:
                refresh(sct)




        # Круглишок метка
        # cv.circle(hsv,(x,y),10,(0,0,255),-1)
        # cv.circle(hsv,(x,y),5,color_yeal,2)

        # cv.imshow("name", img)

        # контуры ищет
        # cv.circle(mask, (x,y),10,(0,0,255), -1)
        # cv.circle(mask, (x,y), 5, color_yeal,2)
        # mask = cv.inRange(hsv, low_range, up_range)
        # cont = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        # cont = imutils.grab_contours(cont)
        # cont = sorted(cont, key=cv.contourArea, reverse=True)
        #
        # pos = None
        # for c in cont:
        #     approx = cv.approxPolyDP(c, 10,True)
        #     if len(approx) == 3:
        #         pos = approx
        #         break
        #
        # print(pos)

while True:
    getStart()



bit.release()
cv.destroyAllWindow()
