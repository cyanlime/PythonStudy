def locate(array, x):
    locate_freq = {}
    freq_item = 0

    for item in range(len(array)):
        if array[item]==x:
            freq_item = item
            if array[item] not in locate_freq.keys():
                locate_freq[array[item]]=1
            else:
                locate_freq[array[item]]+=1
        else:
            locate_freq[array[item]]=0

    #max_value = locate_freq.items()[0][1]
    # for key, value in locate_freq.items():
    #     if value>max_value:
    #         key, max_value = key, value

    for item in range(len(locate_freq.items())-1):
        for item2 in range(item+1, len(locate_freq.items())):
            if locate_freq.items()[item][1]<locate_freq.items()[item2][1]:
                temp = locate_freq.items()[item2]
                locate_freq.items()[item2] = locate_freq.items()[item]
                locate_freq.items()[item] = temp
    print locate_freq.keys()




if __name__ == "__main__":
    #locate([1,2,3,4,5,6], 3)
    # array = [1,3,2,1,2,3,4,5,6,7,3,2]
    # max = array[0]
    # for item in array:
    #     if item>max:
    #         max=item
    # print max
    
    freq = {1: 0, 2: 2, 3: 1, 4: 0, 5: 3, 6: 0}

    print sorted(freq.items(), key=lambda d:d[1], reverse=True)
    #print sorted(freq.items(), lambda x,y: cmp(x[1], y[1]), reverse=True)


    array = []
    max_value = freq.items()[0][1]
    while len(freq.items())>len(array):
        for key, value in freq.items():
            if value>max_value:
                key, max_value = key, value
        array.append(key)
        #freq.pop(key)
        max_value = freq.items()[0][1]
    print array

    # for item in range(len(freq.items())):
    #     for item2 in range(item+1, len(freq.items())):
    #         if freq.items()[item][1]<freq.items()[item2][1]:
    #             temp = freq.items()[item2]
    #             freq.items()[item2] = freq.items()[item]
    #             freq.items()[item] = temp
    # print freq.keys()
