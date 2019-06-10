import numpy as np

orgGird = np.array([[4, 3], [1, 2]], dtype=int)

#shape是用来生成多大的矩阵。
def madeGird(shape):
    global orgGird
    for i in range(2, shape):
        oldSize, _ = orgGird.shape
        newSize = oldSize + 1
        newGird = np.zeros((newSize, newSize))
        print(newSize)
        if newSize % 2 == 1:
            newGird[0:-1, 1:] = orgGird
            for j in range(newSize):
                newGird[j, 0] = oldSize*oldSize + 1 + j
            for j in range(1, newSize):
                newGird[newSize - 1, j] = newGird[newSize -1, 0] + j
            orgGird = newGird
            print(orgGird)
        else:
            newGird[1:, 0:-1] = orgGird
            for j in reversed(range(newSize)):
                newGird[j, -1] = oldSize*oldSize + 1 + oldSize -j
            for j in reversed(range(newSize -1)):
                newGird[0, j] = 1
            print(newGird)




def main():
    shape = 4

    madeGird(shape)


if __name__ == '__main__':
    main()