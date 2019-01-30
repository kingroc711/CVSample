file = './data/neutral.txt'

#这些是已知的分类
names = ['drawings', 'hentai', 'neutral', 'porn', 'sexy']
itemList = []

with open(file) as f:
    item = {}

    for line in f.readlines():
        line = line.strip('\n')
        #每个以'.jpg'结尾的行，作为一个item的开始
        if line.endswith('.jpg'):
            if item != {}:
                t = item.copy()
                itemList.append(t)
                item.clear()
            item['pic'] = line
        else:
            splits = line.split(' ')
            if len(splits) > 1:
                key = splits[0].strip()
                value = splits[3].strip(')')
                item[key] = value
    #将最后一item放入队列
    if item != {}:
        itemList.append(item)

maxList = []
itemNumber = len(itemList)
for i in itemList:
    pic = i.get('pic')
    maxKey = max(i, key=i.get)
    # if(maxKey == 'porn'):
    #     print(pic + " : " + str(maxKey))
    maxList.append(maxKey)

for n in names:
    print('%8s : %d' % (n, maxList.count(n)))
    #print(n + ' : ' + str(maxList.count(n)))