file = './res/neutral.txt'

names = ['drawings', 'hentai', 'neutral', 'porn', 'sexy']
itemList = []

with open(file) as f:
    item = {}

    for line in f.readlines():
        line = line.strip('\n')
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
    print('%8s : %s' % (n, maxList.count(n)))
    #print(n + ' : ' + str(maxList.count(n)))