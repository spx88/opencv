import cv2
import numpy as np

img = cv2.imread('pig.jpg', cv2.IMREAD_GRAYSCALE)


def img_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 图像梯度处理- Sobel算子,参数：1图片 2.图像的深度 3水平方向 4竖直方向5 Sobel算子的大小
# 特点：计算简单，速度快。但是由于只采用了2个方向的模板，只能检测水平和垂直方向的边缘，
# 因此这种算法对于纹理较为复杂的图像，其边缘检测效果就不是很理想
# 在这里dx，dy谁为一就算谁
def Sobelx():
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobelx = cv2.convertScaleAbs(sobelx)
    img_show('Sobelx', sobelx)

    return sobelx


def Sobely():
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobely = cv2.convertScaleAbs(sobely)
    img_show('Sobely', sobely)

    return sobely


# 对soble算法求得的x,y进行求和
def soblexy():
    soblexy = cv2.addWeighted(Sobelx(), 0.5, Sobely(), 0.5, 0)
    img_show('soblexy', soblexy)


# Laplacian 算子
# Laplacian 算子是n维欧几里德空间中的一个二阶微分算子，定义为梯度grad的散度div。
# 可使用运算模板来运算这定理定律。不建议单独使用。
def laplacian():
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)
    img_show('Laplacian', laplacian)

    return laplacian


if __name__ == '__main__':
    # soblexy()
    # laplacian()
    res = np.hstack((laplacian(), img))
    img_show('res', res)
