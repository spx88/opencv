import cv2
import matplotlib.pyplot as plt


def ret_img(src):
    # 转换为灰度图
    img_gray = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
    # 不同的阈值设定方法
    # THRESH_BINARY，超过阈值部分取最大值，否则取0
    ret, thresh1 = cv2.threshold(img_gray, 100, 100, cv2.THRESH_BINARY)
    # THRESH_BINARY_INV，THRESH_BINARY的反转
    ret, thresh2 = cv2.threshold(img_gray, 100, 100, cv2.THRESH_BINARY_INV)
    # THRESH_TRUNC，大于阈值部分设为阈值，否则不变
    ret, thresh3 = cv2.threshold(img_gray, 100, 100, cv2.THRESH_TRUNC)
    # THRESH_TOZERO，大于阈值部分不改变，否则设为0
    ret, thresh4 = cv2.threshold(img_gray, 100, 100, cv2.THRESH_TOZERO)

    titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO']
    images = [img_gray, thresh1, thresh2, thresh3, thresh4]

    # subplot用来绘制子图
    for i in range(5):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    img = cv2.imread('cat006.jpg')
    print(img.shape)
    ret_img('cat006.jpg')
