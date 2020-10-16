import cv2 as cv

import numpy as np


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width: %s, height: %s channels: %s" % (width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("pixels_demo", image)


def create_image():
    # img = np.zeros([400, 400, 3], np.uint8)
    # # 蓝色通道
    # # img[:, :, 0] = np.ones([400, 400]) * 255
    # # 红色通道
    # img[:, :, 2] = np.ones([400, 400]) * 255

    # img = np.zeros([400, 400, 1], np.uint8)
    # img[:, :, 0] = np.ones([400, 400]) * 127
    #
    # cv.imshow("new image ", img)

    m1 = np.ones([3, 3], np.float32)

    m1.fill(122.388)

    print(m1)


if __name__ == '__main__':
    print("---------hello python------")
    src = cv.imread("logo.jpg")  # RGB
    # cv.namedWindow("input images", cv.WINDOW_AUTOSIZE)
    cv.imshow("input image", src)
    t1 = cv.getTickCount()
    create_image()
    # access_pixels(src)

    t2 = cv.getTickCount()
    time = (t2 - t1) / cv.getTickFrequency();
    print("time:%s ms" % (time * 1000))
    # video_demo()

    cv.waitKey(0)

    cv.destroyAllWindows()
