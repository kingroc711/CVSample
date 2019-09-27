import numpy as np

H = 9; W = 9

def printMat(mat):
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
    print()

mainMat = np.zeros((H,W), dtype=np.int8)
if False:
    mainMat[0, 1] = 7; mainMat[0, 5] = 5; mainMat[0, 7] = 9
    mainMat[1, 0] = 4; mainMat[1, 5] = 6; mainMat[1, 8] = 7
    mainMat[2, 3] = 8; mainMat[2, 5] = 2
    mainMat[3, 0] = 2; mainMat[3, 1] = 8; mainMat[3, 2] = 6; mainMat[3, 6] = 4
    mainMat[5, 2] = 9; mainMat[5, 6] = 1; mainMat[5, 7] = 7; mainMat[5, 8] = 8
    mainMat[6, 3] = 4; mainMat[6, 5] = 1
    mainMat[7, 0] = 3; mainMat[7, 3] = 6; mainMat[7, 8] = 5
    mainMat[8, 1] = 4; mainMat[8, 3] = 3; mainMat[8, 7] = 2
else:
    mainMat[0, 0] = 5; mainMat[0, 1] = 3; mainMat[0, 4] = 7
    mainMat[1, 0] = 6; mainMat[1, 3] = 1; mainMat[1, 4] = 9; mainMat[1, 5] = 5
    mainMat[2, 1] = 9; mainMat[2, 2] = 8; mainMat[2, 7] = 6
    mainMat[3, 0] = 8; mainMat[3, 4] = 6; mainMat[3, 8] = 3
    mainMat[4, 0] = 4; mainMat[4, 3] = 8; mainMat[4, 5] = 3; mainMat[4, 8] = 1
    mainMat[5, 0] = 7; mainMat[5, 4] = 2; mainMat[5, 8] = 6
    mainMat[6, 1] = 6; mainMat[6, 6] = 2; mainMat[6, 7] = 8
    mainMat[7, 3] = 4; mainMat[7, 4] = 1; mainMat[7, 5] = 9; mainMat[7, 8] = 5
    mainMat[8, 4] = 8; mainMat[8, 7] = 7; mainMat[8, 8] = 9

printMat(mainMat)


lastMat = np.zeros(mainMat.shape, mainMat.dtype)

while((lastMat == mainMat).all() == False):
    lastMat = mainMat.copy()
    for i in range(H):
        for j in range(W):
            if mainMat[i, j] == 0:
                iteams = np.append(mainMat[i, :], mainMat[:, j])
                iteams = np.append(iteams, mainMat[(i // 3) * 3 : ((i // 3) * 3) + 3, (j // 3) * 3 : ((j // 3) * 3) + 3].flatten())
                iteams = list(set(iteams))

                if 0 in iteams:
                    iteams.remove(0)
                if len(iteams) == 8 and sum(iteams) != 45:
                    print(i, j)
                    print(iteams, len(iteams), sum(iteams))
                    mainMat[i, j] = 45 - sum(iteams)
                    printMat(mainMat)


