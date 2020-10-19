import cv2
import numpy as np

# 高斯金字塔：向下采样方法(缩小)--将Gi与高斯内核卷积，将所有偶数行和列去除,向上采样方法(放大):
# 这里的向上和向下指的是图片变大还是变小
# 拉普拉斯金字塔:

img = cv2.imread('pig.jpg')  # (501, 500, 3)


def img_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 上采样
def up():
    up = cv2.pyrUp(img)
    img_show('up', up)
    print(up.shape)  # (1002, 1000, 3) -- 上采样相当于放大了俩倍


# 下采样
def down():
    down = cv2.pyrDown(img)
    img_show('down', down)
    print(down.shape)  # (251, 250, 3)


def up_down():
    up = cv2.pyrUp(img)
    up_down = cv2.pyrDown(up)
    img_show('up_down', up_down)
    print(up_down.shape)

if __name__ == '__main__':
    # img_show('img', img)
    # print(img.shape)
    # up()
    # down()
    up_down()
