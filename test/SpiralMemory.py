import numpy as np

orgGird = np.array([[4, 3], [1, 2]], dtype=int)

#shape是用来生成多大的矩阵。
def madeGird(shape, maxNum):
    global orgGird
    for i in range(2, shape):
        oldSize, _ = orgGird.shape
        newSize = oldSize + 1
        newGird = np.zeros((newSize, newSize))
        try:
            #当是奇数矩阵的时候向右上角挪动
            if newSize % 2 == 1:
                newGird[0:-1, 1:] = orgGird
                for j in range(newSize):
                    newGird[j, 0] = oldSize*oldSize + 1 + j
                    if newGird[j, 0] == maxNum:
                        return
                for j in range(1, newSize):
                    newGird[newSize - 1, j] = newGird[newSize -1, 0] + j
                    if newGird[newSize - 1, j] == maxNum:
                        return
            else:
                #当是偶数的时候想左下角移动
                newGird[1:, 0:-1] = orgGird
                for j in reversed(range(newSize)):
                    newGird[j, -1] = oldSize*oldSize + 1 + oldSize -j
                    if newGird[j, -1] == maxNum:
                        return
                for j in reversed(range(newSize -1)):
                    newGird[0, j] = 1 + newGird[0, j + 1]
                    if newGird[0, j] == maxNum:
                        return
        finally:
            orgGird = newGird


def main():
    inputNum = 101

    sqrt = inputNum ** 0.5
    sqrt_int = int(sqrt)
    if (sqrt > float(sqrt_int)):
        sqrt_int += 1

    madeGird(sqrt_int, inputNum)
    print(orgGird)
    one_pos = np.argwhere(orgGird == 1)
    one_x = one_pos[0][0]
    one_y = one_pos[0][1]

if __name__ == '__main__':
    main()