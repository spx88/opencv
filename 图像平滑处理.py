import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('dog001.jpg')


# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 均值滤波
def mean_filter():
    # 简单的平均卷积操作，（3,3）就是卷积核大小
    blur = cv2.blur(img, (3, 3))
    cv2.imshow('blur', blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return blur


# 方框滤波，基本和均值一样，可以选择归一化
def box_filter_true():
    # 可以选择是否归一化，选择了True，就是归一化，就是和均值滤波一样了
    box = cv2.boxFilter(img, -1, (3, 3), normalize=True)
    cv2.imshow('box', box)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return box


# 方框滤波，基本和均值一样，没有选择归一化，容易越界，当像素大于255时全部取255
def box_filter_false():
    box = cv2.boxFilter(img, -1, (3, 3), normalize=False)
    cv2.imshow('box', box)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # return


# 高斯滤波
def gaussian_filter():
    gaussian = cv2.GaussianBlur(img, (5, 5), 1)

    cv2.imshow('gaussian', gaussian)
    cv2.waitKey()
    cv2.destroyAllWindows()
    return gaussian


# 中值滤波,相当于中指代替,用来降噪处理
def median_filter():
    median = cv2.medianBlur(img, 5)

    cv2.imshow('median', median)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def show_img(img1, img2, img3):
    res = np.hstack((img1, img2, img3))
    print(res)
    cv2.imshow('all images', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # box_filter_false()
    # gaussian_filter()
    # median_filter()
    show_img(mean_filter(), box_filter_true(), gaussian_filter())
