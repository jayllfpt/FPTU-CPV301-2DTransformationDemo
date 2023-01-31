import cv2
import numpy as np
import math

height = 768
width = 1024
Ax, Ay, Bx, By = -1, -1, -1, -1
color1 = (0, 255, 255)
color2 = (0, 100, 255)


def function1():
    img = np.zeros((height, width, 3), np.uint8)
    img[:, :] = (255, 255, 255)

    return img


# cv2.imshow('Binary', function1())
# cv2.waitKey(0)


def function2():
    # drawing = False
    img = function1()

    def draw_rectangle(event, x, y, flags, param):
        global Ax, Ay, Bx, By, drawing
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            Ax = x
            Ay = y
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            Bx = x
            By = y
            print("Rectangle: (", Ax, ",", Ay, ") and (", Bx, ",", By, ").")
            print("Press ESC to confirm the rectangle")
            cv2.rectangle(img, (Ax, Ay), (Bx, By), color1, -1)

    # Create a window and bind the function to window
    cv2.namedWindow("Rectangle Window")

    # Connect the mouse button to our callback function
    cv2.setMouseCallback("Rectangle Window", draw_rectangle)

    # display the window
    while True:
        cv2.imshow("Rectangle Window", img)
        if cv2.waitKey(10) == 27:
            break

    return Ax, Ay, Bx, By
    cv2.destroyAllWindows()


# Ax, Ay, Bx, By = function2()


# translation
def function3(Ax, Ay, Bx, By):
    print("     Translation")
    print("     Enter translation vector: ")
    x = int(input("x = "))
    y = int(input("y = "))
    img_trans = function1()
    ax = Ax + x
    ay = Ay + y
    bx = Bx + x
    by = By + y
    print("     Old Rectangle: (", Ax, ",", Ay, ") and (", Bx, ",", By, ").")
    cv2.rectangle(img_trans, (Ax, Ay), (Bx, By), color1, -1)
    print("     New Rectangle: (", ax, ",", ay, ") and (", bx, ",", by, ").")
    cv2.rectangle(img_trans, (ax, ay), (bx, by), color2, 3)

    print("Press any key to continue.")
    cv2.imshow('Translation', img_trans)
    cv2.waitKey(0)
    return img_trans


def function4(Ax, Ay, Bx, By):
    def rotatePoint(Ax, Ay, Ox, Oy, a):
        a *= math.pi/180
        cosA = math.cos(a)
        sinA = math.sin(a)
        ax = int((Ax - Ox) * cosA - (Ay - Oy) * sinA + Ox)
        ay = int((Ax - Ox) * sinA + (Ay - Oy) * cosA + Oy)
        return ax, ay
    print("     Rotation")
    a = float(input("       Enter rotation angle: "))

    Ox = (Bx + Ax) / 2
    Oy = (By + Ay) / 2

    ax, ay = rotatePoint(Ax, Ay, Ox, Oy, a)
    bx, by = rotatePoint(Ax, By, Ox, Oy, a)
    cx, cy = rotatePoint(Bx, Ay, Ox, Oy, a)
    dx, dy = rotatePoint(Bx, By, Ox, Oy, a)

    img_rot = function1()
    print("     Old Rectangle: (", Ax, ",", Ay, ") and (", Bx, ",", By, ").")
    cv2.rectangle(img_rot, (Ax, Ay), (Bx, By), color1, -1)

    print("     New Rectangle: (", ax, ",", ay, ") and (", bx, ",", by, ") and (", cx, ",", cy, ") (", dx, ",", dy, ").")
    cv2.line(img_rot, (ax, ay), (bx, by), color2, 2)
    cv2.line(img_rot, (dx, dy), (bx, by), color2, 2)
    cv2.line(img_rot, (cx, cy), (dx, dy), color2, 2)
    cv2.line(img_rot, (ax, ay), (cx, cy), color2, 2)

    print("Press any key to continue.")
    cv2.imshow('Rotation', img_rot)
    cv2.waitKey(0)
    return img_rot


def function5(Ax, Ay, Bx, By):
    print("     Scaling")
    f = float(input("       Enter scaling factor: "))
    ax = int(Ax * f)
    ay = int(Ay * f)
    bx = int(Bx * f)
    by = int(By * f)
    img_scale = function1()
    print("     Old Rectangle: (", Ax, ",", Ay, ") and (", Bx, ",", By, ").")
    cv2.rectangle(img_scale, (Ax, Ay), (Bx, By), color1, -1)

    print("     New Rectangle: (", ax, ",", ay, ") and (", bx, ",", by, ").")
    cv2.rectangle(img_scale, (ax, ay), (bx, by), color2, 3)

    print("Press any key to continue.")
    cv2.imshow('Scaling', img_scale)
    cv2.waitKey(0)
    return img_scale

# function3(Ax, Ay, Bx, By)
# function4(Ax, Ay, Bx, By)
# function5(Ax, Ay, Bx, By)