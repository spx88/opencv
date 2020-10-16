import cv2
import matplotlib.pyplot as plt
import time


# 照片的读取
# img = cv2.imread("RIMG0094.jpg")
#
# cv2.imshow("OutPut", img)
# cv2.waitKey(0)

# 视频文件的读取
# cap = cv2.VideoCapture("1353400305196a24be865310.mp4")
# 摄像头读取
# cap = cv2.VideoCapture(0)
# cap.set(3, 460)

def video_demo(src):
    cap = cv2.VideoCapture(src)
    # 检查是否打开正确,isOpened会返回俩个值，第一个是布尔类型，第二个是当前的这一帧图像
    if cap.isOpened():
        open, frame = cap.read()
    else:
        open = False
    while open:
        ret, frame = cap.read()
        if frame is None:
            break
        if ret == True:
            # 转换为灰度图
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('result', gray)
            # 27指定的是退出键也就是esc
            if cv2.waitKey(100) & 0xFF == 27:
                break
    cap.release()
    cv2.destroyAllWindows()


# 截获图像的一部分
def img_split(src):
    img = cv2.imread(src)
    cat = img[0:200, 0:200]
    cv2.imshow('cat', cat)
    cv2.waitKey(0)


# 分别查看图像BGR
def img_RGB(src):
    img = cv2.imread(src)
    b, g, r = cv2.split(img)
    print("b:", b)
    print("b.shape", b.shape)
    print("g:", g)
    print("r:", r)
    # 只保留R
    cur_img = img.copy()
    cur_img[:, :, 0] = 0
    cur_img[:, :, 1] = 0
    cv2.imshow("R", cur_img)
    cv2.waitKey(0)


# 几种填充方式的展示
def padding(src):
    top_size, bottom_size, left_size, right_size = (50, 50, 50, 50)
    img = cv2.imread(src)
    replicate = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT)
    reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP)
    constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_CONSTANT)

    plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL'),
    # BORDER_REPLICATE 复制法，也就是复制最边缘像素
    print("开始复制法填充")
    plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE'),
    # BORDER_REFLECT 反射法，也就是以最边缘像素为轴，对称
    plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
    plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
    # plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')


def number(src):
    img = cv2.imread(src)
    print(img)
    img2 = img + 10
    print(img2)


def add(src_dog, src_cat):
    img_dog = cv2.imread(src_dog)
    img_cat = cv2.imread(src_cat)
    # 如果图片大小不一致，可以通过resize改变图片像素
    print(img_dog.shape)
    print(img_cat.shape)
    # 图像融合 第一个x 第二个x 偏置
    res = cv2.addWeighted(img_cat, 0.4, img_dog, 0.6, 0)
    # imshow函数负责对图像进行处理，但不能显示   
    plt.imshow(res)
    # 这里imshow不显示要加一个plt.show
    plt.show()


if __name__ == '__main__':
    # video_demo("1353400305196a24be865310.mp4")
    # img_split("RIMG0094.jpg")
    # while True:
    #     success, img = cap.read()
    #     cv2.imshow("video", img)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    # img_RGB("RIMG0094.jpg")
    # padding("RIMG0094.jpg")
    # number("RIMG0094.jpg")
    add("dog001.jpg", "cat006.jpg")
