def SAMplespace(Numdice):
    list = []
    for x in range(6):
        for y in range(6):
            pair = [x+1, y+1]
            list.append(pair)
    size = len(list)
    print('size:' + str(size))
    print(list)

SAMplespace(1)


def sumOFdieis(sum):
    list = []
    for x in range(6):
        for y in range(6):
            pair = [x + 1, y + 1]
            if (x+y+2) == 2 or (x+y+2) == 3 or (x+y+2)== 12 or (x+y+2)==7 or (x+y+2)== 11:
                list.append(pair)
    size = len(list)
    print('size that sum:' + str(size))
    print(list)

sumOFdieis(5)

def sumofdieodd():
    list = []
    for x in range(6):
        for y in range(6):
            pair = [x + 1, y + 1]
            if (x+y+2) % 3 == 0:
                list.append(pair)
    size = len(list)
    print('size odd:' + str(size))
    print(list)
#sumofdieodd()

def oneoddoneeven():
    list = []
    for x in range(6):
        for y in range(6):
            pair = [x + 1, y + 1]
            if (((x+1) % 2 == 0 or (y+1) % 2 == 0)) or (x+y+2) == sum:
                list.append(pair)
    size = len(list)
    print('size 1even1odd:' + str(size))
    print(list)
oneoddoneeven()