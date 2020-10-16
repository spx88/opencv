import cv2 as cv
import numpy as np


# 视频读取操作
def video_demo():
    capture = cv.VideoCapture(0)
    while (True):
        ret, frame = capture.read()
        # 颠倒摄像头
        frame = cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break


# 图像读取操作
def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


print("---------hello python------")
# 读取图像，opencv读取的格式是BGR
# src = cv.imread("logo.jpg")

# 读取灰度图像,之后会经常用到灰度图和彩色图的转换
src = cv.imread("RIMG0094.jpg", cv.IMREAD_GRAYSCALE)

# 保存图像
cv.imwrite('gray1.jpg', src)

# cv.namedWindow("input images", cv.WINDOW_AUTOSIZE)

# 指定参数 第一个是窗口名字，第二个是图片
cv.imshow("input image", src)
get_image_info(src)
# video_demo()

# 等待时间，毫秒级
cv.waitKey(0)

cv.destroyAllWindows()
