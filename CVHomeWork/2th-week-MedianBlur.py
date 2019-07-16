import cv2
import numpy as np


def medianBlur(img, kernel, padding_way='ZERO', Multithreading=False):
    # 检测传入的kernel是否为一个合法数组.
    if kernel % 2 == 0 or kernel is 1:
        print('kernel size need 3, 5, 7, 9....')
        return None

    # 通过kernel的大小来计算paddingSize的大小
    paddingSize = kernel // 2

    # 获取图片的通道数
    layerSize = len(img.shape)

    # 获取传入的图片的大小
    height, width = img.shape[:2]

    # 假设输入,如下矩阵,5x5
    # [[2 6 3 4 7]
    #  [6 1 7 1 5]
    #  [4 6 7 3 3]
    #  [3 1 8 8 6]
    #  [2 4 8 0 7]]

    # 这里是对多通道的处理
    if layerSize == 3:  # 多通道的处理方式,就是反复的调用单通道.
        matMutbase = np.zeros_like(img)
        for l in range(matMutbase.shape[2]):
            matMutbase[:, :, l] = medianBlur(img[:, :, l], kernel, padding_way)
        return matMutbase
    elif layerSize == 2:  # 单通道是中值滤波的实际工作的位置.
        # 实现方式和np.lib.pad相同
        # matBase = np.lib.pad(img,paddingSize, mode='constant', constant_values=0)
        matBase = np.zeros((height + paddingSize * 2, width + paddingSize * 2), dtype=img.dtype)

        # 创建一个添加了padding的矩阵,初始值为0
        # 如果kernel的大小为3,所以从5x5变成了7x7
        # [[0 0 0 0 0 0 0]
        #  [0 0 0 0 0 0 0]
        #  [0 0 0 0 0 0 0]
        #  [0 0 0 0 0 0 0]
        #  [0 0 0 0 0 0 0]
        #  [0 0 0 0 0 0 0]
        #  [0 0 0 0 0 0 0]]

        matBase[paddingSize:-paddingSize, paddingSize:-paddingSize] = img
        # 将原值写入新创建的矩阵当中
        # [[0 0 0 0 0 0 0]
        # [0 2 6 3 4 7 0]
        # [0 6 1 7 1 5 0]
        # [0 4 6 7 3 3 0]
        # [0 3 1 8 8 6 0]
        # [0 2 4 8 0 7 0]
        # [0 0 0 0 0 0 0]]
        # print(matBase)
        if padding_way is 'ZERO':
            pass
        elif padding_way is 'REPLICA':
            for r in range(paddingSize):
                matBase[r, paddingSize:-paddingSize] = img[0, :]
                matBase[-(1 + r), paddingSize:-paddingSize] = img[-1, :]
                matBase[paddingSize:-paddingSize, r] = img[:, 0]
                matBase[paddingSize:-paddingSize, -(1 + r)] = img[:, -1]
                # 通过REPLICA后的矩阵,讲四个边补齐
                # [[0 2 6 3 4 7 0]
                # [2 2 6 3 4 7 7]
                # [6 6 1 7 1 5 5]
                # [4 4 6 7 3 3 3]
                # [3 3 1 8 8 6 6]
                # [2 2 4 8 0 7 7]
                # [0 2 4 8 0 7 0]]
                # 实现方式和np.lib.pad相同
                # matBase = (img, padding, mode='edge')
            # print(matBase)
        else:
            print('padding_way error need ZERO or REPLICA')
            return None

        # 创建用于输出的矩阵
        matOut = np.zeros((height, width), dtype=img.dtype)
        # 这里是遍历矩阵的每个点
        for x in range(height):
            for y in range(width):
                # 获取kernel X kernel 的内容,并转化成队并列
                line = matBase[x:x + kernel, y:y + kernel].flatten()
                # 队列排序处理.
                line = np.sort(line)
                # 取中间值赋值
                matOut[x, y] = line[(kernel * kernel) // 2]
        return matOut
    else:
        print('image layers error')
        return None


def main():
    # 读取原始图片
    img = cv2.imread("res/jyan.jpeg")
    # print(img)

    # 使用自己手写的medianBlur进行中值滤波啊
    myself = medianBlur(img, 5, padding_way='REPLICA')
    if myself is None:
        return

    # 调用OpenCV的接口进行中值滤波
    opencv = cv2.medianBlur(img, 5)

    # 这里进行图片合并
    img = np.hstack((img, myself))
    img = np.hstack((img, opencv))

    # 显示对比效果
    cv2.imshow('ORG + myself + OpenCV', img)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
