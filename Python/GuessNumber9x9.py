import numpy as np

def getPossibleMap(mList):
    H = len(mList);
    W = pow(2, len(mList))
    mat = np.zeros((H, W), dtype=np.int8)
    for i in range(H):
        for j in range(W):
            step = W // (pow(2, i) * 2)
            mat[i, j] = mList[i][(j // step) % 2]

    return mat
    # print(mat)
    #
    # line = 0
    # sameLine = 0
    # while line + sameLine < W:
    #     l = mat[:, line:line+1]
    #     setL = set(l.flatten())
    #     if len(l) is not len(setL):
    #         sameLine = sameLine + 1
    #         mat[:, line: -1] = mat[:, line + 1:]
    #     else:
    #         line = line + 1
    #
    # print('sameLine : ', sameLine)
    # print(mat)
    # nMat = np.copy(mat[:, 0: W - sameLine])
    # return nMat

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


def possibility2number(mainMat):
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

                if len(iteams) >= 7:
                    fullNumber = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).tolist()
                    for it in iteams:
                        if it in fullNumber:
                            fullNumber.remove(it)
                    #print(i, j, fullNumber)
                    possibles.append(fullNumber)
                    coordinates.append([i, j])
    return coordinates, possibles

def main():
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

    mainMat = easyFindNumbers(mainMat)
    printMat(mainMat)

    coordinates, possibles = possibility2number(mainMat)
    if coordinates is []:
        return

    print(coordinates, possibles)
    pMap = getPossibleMap(possibles)
    tH, tW = pMap.shape
    print('H : ', tH, ', W : ', tW)

    tMat = np.copy(mainMat)
    for i in range(tW):
        pline = pMap[:, i: i + 1].flatten()
        #print('aaa', pline)
        for j in range(len(coordinates)):
            tMat[coordinates[j][0], coordinates[j][1]] = pline[j]

        ttmap = easyFindNumbers(tMat)
        if isValue(ttmap):
            printMat(ttmap)


if __name__ == '__main__':
    main()