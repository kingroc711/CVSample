import numpy as np
import copy

#这个函数的作用是多个数组，每个数组中取一个数字，最多能有多少种组合方式。
def getAllPossibleMap(mList):
    H = len(mList)
    W = 1
    for l in mList:
        W = W * len(l)

    print('getAllPossibleMap : ', H, W)
    mat = np.zeros((H, W), dtype=np.int8)
    for i in range(H):
        for j in range(W):
            step = W // (pow(len(mList[i]), i) * len(mList[i]))
            mat[i, j] = mList[i][(j // step) % len(mList[i])]

    return mat

def printMat(mat):
    print('----------------------', end=' ')
    H = 9; W = 9
    for i in range(H):
        if i % 3 == 0 and i != 0:
            print('\n---------------------')
        else:
            print()

        for j in range(W):
            if j % 3 == 0 and j != 0:
                print('|', end=' '); print(mat[i, j], end=' ')
            else:
                print(mat[i, j], end=' ')
    print('\n----------------------')

def isValue(mat):
    H, W = mat.shape
    for i in range(H):
        for j in range(W):
            iteams = np.append(mat[i, :], mat[:, j])
            iteams = np.append(iteams, mat[(i // 3) * 3: ((i // 3) * 3) + 3, (j // 3) * 3: ((j // 3) * 3) + 3].flatten())
            iteams = list(set(iteams))
            if 0 in iteams:
                return False
            if len(iteams) != 9:
                return False

    return True

def easyFindNumbers(mat):
    H, W = mat.shape
    lastMat = np.zeros(mat.shape, mat.dtype)

    while not (lastMat == mat).all():
        lastMat = mat.copy()
        for i in range(H):
            for j in range(W):
                if mat[i, j] == 0:
                    iteams = np.append(mat[i, :], mat[:, j])
                    iteams = np.append(iteams, mat[(i // 3) * 3 : ((i // 3) * 3) + 3, (j // 3) * 3 : ((j // 3) * 3) + 3].flatten())
                    iteams = list(set(iteams))

                    if 0 in iteams:
                        iteams.remove(0)
                    if len(iteams) == 8 and sum(iteams) != 45:
                        #print(i, j)
                        #print(iteams, len(iteams), sum(iteams))
                        mat[i, j] = 45 - sum(iteams)
    return lastMat


def possibilityNumber(mainMat, n):
    possibles = []
    coordinates = []
    (H, W) = mainMat.shape
    
    for i in range(H):
        for j in range(W):
            if mainMat[i, j] == 0:
                iteams = np.append(mainMat[i, :], mainMat[:, j])
                iteams = np.append(iteams, mainMat[(i // 3) * 3: ((i // 3) * 3) + 3, (j // 3) * 3: ((j // 3) * 3) + 3].flatten())
                iteams = list(set(iteams))

                if 0 in iteams:
                    iteams.remove(0)

                if len(iteams) == 9 - n:
                    fullNumber = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).tolist()
                    for it in iteams:
                        if it in fullNumber:
                            fullNumber.remove(it)
                    #print(i, j, fullNumber)
                    possibles.append(fullNumber)
                    coordinates.append([i, j])
    return coordinates, possibles

strList = []
strList2 = []
index = 0
def calAllWay(possibles):
    wayList = []
    tmpwayList= []

    for line in possibles:
        if len(wayList) == 0:
            for item in line:
                wayList.append(item)
        else:
            for wline in wayList:
                for item in line:
                    tmpwayList.append(np.append(wline, item))

            wayList = copy.deepcopy(tmpwayList)
            tmpwayList.clear()

    print('waylist : ', wayList)
    return wayList

def main():
    #初始化数独矩阵
    H = 9; W = 9
    mainMat = np.zeros((H,W), dtype=np.int8)
    mainMat[0, 1] = 7; mainMat[0, 5] = 5; mainMat[0, 7] = 9
    mainMat[1, 0] = 4; mainMat[1, 5] = 6; mainMat[1, 8] = 7
    mainMat[2, 3] = 8; mainMat[2, 5] = 2
    mainMat[3, 0] = 2; mainMat[3, 1] = 8; mainMat[3, 2] = 6; mainMat[3, 6] = 4
    mainMat[5, 2] = 9; mainMat[5, 6] = 1; mainMat[5, 7] = 7; mainMat[5, 8] = 8
    mainMat[6, 3] = 4; mainMat[6, 5] = 1
    mainMat[7, 0] = 3; mainMat[7, 3] = 6
    mainMat[7, 8] = 5
    mainMat[8, 1] = 4; mainMat[8, 3] = 3; mainMat[8, 7] = 2

    printMat(mainMat)

    #将容易计算出来的位置进行计算
    mainMat = easyFindNumbers(mainMat)
    printMat(mainMat)

    #计算一个格子里可能存在的数字。
    coordinates2, possibles2 = possibilityNumber(mainMat, 2)
    print('coordinates2 : ', coordinates2, '\npossibles2 : ', possibles2)

    coordinates3, possibles3 = possibilityNumber(mainMat, 3)
    print('coordinates3 : ', coordinates3, '\npossibles3 : ', possibles3)

    #由于电脑性限制，有3个可能性的我只添加了3个。
    for i in range(3):
        coordinates2.append(coordinates3[i])
        possibles2.append(possibles3[i])

    print('coordinates : ', coordinates2, '\npossibles : ', possibles2)
    #计算所有的路径了
    allWay = calAllWay(possibles2.copy())

    #测试所有的路径
    for index in range(len(allWay)):
        tMat = np.copy(mainMat)
        line = allWay[index]
        #print(line)
        for index2 in range(len(coordinates2)):
            tMat[coordinates2[index2][0], coordinates2[index2][1]] = line[index2]

        #检测路径是否正确
        ttmap = easyFindNumbers(tMat)
        if isValue(ttmap):
            printMat(ttmap)

if __name__ == '__main__':
    main()