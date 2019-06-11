import numpy as np

divNum = np.array([1, 2, 3, 5], dtype=int)
numList = []


def main():
    ################### At here input your number################
    inputNum = 100
    ################### At here input your number################

    while True:
        if inputNum % 2 == 0:
            inputNum = inputNum / 2
            numList.append(2)
        elif inputNum % 3 == 0:
            inputNum = inputNum / 3
            numList.append(3)
        elif inputNum % 5 == 0:
            inputNum = inputNum / 5
            numList.append(5)
        else:
            if (divNum == inputNum).any():
                if inputNum != 1:
                    numList.append(inputNum)
                print(numList)
            else:
                print('None')
            break;


if __name__ == '__main__':
    main()
