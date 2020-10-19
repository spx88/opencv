import cv2
import numpy as np

"""图像轮廓"""
# cv2.findContours(img, model, method)
# mode:轮廓检测模式
# RETR_EXTERNAL:只检测最外面的轮廓
# RETR_LIST:检测所有轮廓，并将其保存到一条链表当中
# RETR_CCOMP:检测所有轮廓，并将他们组织为俩层：顶层是各部分的外部边界，第二层是空洞的边界
# RETR_TREE:检测所有轮廓，并重构嵌套轮廓的整个层次
# method：轮廓逼近方法
# CHAIN_APPROX_NONE:以Freeman链码的方式输出轮廓，所有其它方法输出多边形
# CHAIN_APPROX_SIMPLE:压缩水平的、垂直的和斜的部分，函数只保留终点部分

img = cv2.imread('cat006.jpg')


def img_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 图像的灰度处理以及二值处理
def binary_deal():
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # img_show('thresh', thresh)
    # contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # print(np.array(contours).shape)
    return thresh


# 画出轮廓
def outline():
    # 这里新版本的opencv的findContours方法只会返回俩个值
    contours, hierarchy = cv2.findContours(binary_deal(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print(np.array(contours).shape)
    # 注意需要使用copy，否则原图会发生改变
    draw_img = img.copy()
    res = cv2.drawContours(draw_img, contours, -1, (0, 0, 255), 2)
    # img_show('res', res)
    cnt = contours[0]
    # 面积
    print(cv2.contourArea(cnt))
    # 周长，True表示闭合的
    print(cv2.arcLength(cnt, True))


def outline1():
    # 这里新版本的opencv的findContours方法只会返回俩个值
    contours, hierarchy = cv2.findContours(binary_deal(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print(np.array(contours).shape)
    # 注意需要使用copy，否则原图会发生改变
    draw_img = img.copy()

    res = cv2.drawContours(draw_img, contours, 0, (0, 0, 255), 5)
    img_show('res', res)


def outline_approx():
    contours, hierarchy = cv2.findContours(binary_deal(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnt = contours[0]

    draw_img = img.copy()
    res = cv2.drawContours(draw_img, [cnt], -1, (0, 0, 255), 2)
    img_show('res', res)

    epsilon = 0.2 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)

    draw_img = img.copy()
    res = cv2.drawContours(draw_img, [approx], -1, (0, 0, 255), 2)
    img_show('res', res)


def template():
    # 读取目标图片
    target = cv2.imread("target.jpg")
    # 读取模板图片
    template = cv2.imread("template.jpg")
    # 获得模板图片的高宽尺寸
    theight, twidth = template.shape[:2]
    # 执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)
    # 归一化处理
    cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)
    # 寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # 匹配值转换为字符串
    # 对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
    # 对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
    strmin_val = str(min_val)
    # 绘制矩形边框，将匹配区域标注出来
    # min_loc：矩形定点
    # (min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高
    # (0,0,225)：矩形的边框颜色；2：矩形边框宽度
    cv2.rectangle(target, min_loc, (min_loc[0] + twidth, min_loc[1] + theight), (0, 0, 225), 2)
    # 显示结果,并将匹配值显示在标题栏上
    cv2.imshow("MatchResult----MatchingValue=" + strmin_val, target)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # binary_deal()
    # outline()
    # outline1()
    # outline_approx()
    template()
