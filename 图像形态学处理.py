import cv2
import numpy as np

"""形态学-腐蚀操作，一般是二值的图像可以进行处理"""

img = cv2.imread('text.jpg')


def img_show():
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 腐蚀处理
def edge_deal():
    kernel = np.ones((5, 5), np.uint8)
    # iterations是选择迭代次数
    erosion = cv2.erode(img, kernel, iterations=2)

    cv2.imshow('erosion', erosion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 腐蚀处理
def edge_deal1():
    kernel = np.ones((30, 30), np.uint8)
    erosion_1 = cv2.erode(img, kernel, iterations=1)
    erosion_2 = cv2.erode(img, kernel, iterations=2)
    erosion_3 = cv2.erode(img, kernel, iterations=3)
    res = np.hstack((erosion_1, erosion_2, erosion_3))
    cv2.imshow('res', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 膨胀操作,与腐蚀操作互为逆运算
def inflation_demo1():
    kernel = np.ones((3, 3), np.uint8)
    erosion = cv2.dilate(img, kernel, iterations=1)

    cv2.imshow('erosion', erosion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def inflation_demo2():
    kernel = np.ones((30, 30), np.uint8)
    dilate_1 = cv2.dilate(img, kernel, iterations=1)
    dilate_2 = cv2.dilate(img, kernel, iterations=2)
    dilate_3 = cv2.dilate(img, kernel, iterations=3)
    res = np.hstack((dilate_1, dilate_2, dilate_3))
    cv2.imshow('res', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 开运算：先腐蚀，再膨胀
def open_operation():
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    cv2.imshow('opening', opening)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 闭运算：先膨胀，后腐蚀
def close_operation():
    kernel = np.ones((5, 5), np.uint8)

    closing = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imshow('closing', closing)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 梯度 =膨胀-腐蚀
def gradient():
    # ones()返回一个全1的n维数组，同样也有三个参数：shape（用来指定返回数组的大小）、
    # dtype（数组元素的类型）、order（是否以内存中的C或Fortran连续（行或列）顺序存储多维数据）
    kernel = np.ones((7, 7), np.uint8)
    dilate = cv2.dilate(img, kernel, iterations=5)
    erosion = cv2.erode(img, kernel, iterations=5)

    # 在水平方向上平铺
    res = np.hstack((dilate, erosion))
    cv2.imshow('res', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 通过调用MORPH_GRADIENT直接进行膨胀操作，由此可见morphologyEx是一个强大的函数，通过传递不同的参数来实现各种操作
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow('gradient', gradient)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 礼帽子与黑帽
# 礼帽：原始输入 - 开运算结果
# 黑帽：闭运算- 原始输入
def top_hat():
    kernel = np.ones((5, 5), np.uint8)
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    cv2.imshow('tophat', tophat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def black_hot():
    kernel = np.ones((5, 5), np.uint8)
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
    cv2.imshow('blackhat', blackhat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # img_show()
    # edge_deal()
    # edge_deal1()
    # inflation_demo1()
    # inflation_demo2()
    # open_operation()
    # close_operation()
    # gradient()
    # string_print(123)
    # top_hat()
    black_hot()