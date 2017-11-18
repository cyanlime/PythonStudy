def chorus_formation(array):
    dequenes = []
    dequene=0
    item = 0
    while item<len[array]-1:
        item+=1
        if array[item]>array[item-1]:
            continue
        else:
            dequene+=1
            dequenes.append(array[item])
            continue

if __name__ == "__main__":
    chorus_formation([186,186,150,200,160,130,197,200])
    chorus_formation([186,186,201,150,200,160,130,197,200])