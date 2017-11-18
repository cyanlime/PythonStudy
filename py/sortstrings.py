def integer_in(num):
    ins = []
    item = 0
    string = num[item]
    while item<len(num)-2:
        item+=1
        string+=num[item]
        ins.append(string)

    item = 1
    cir_item = item
    while item<len(num)-1:
        string = num[item]
        cir_item = item
        while cir_item<len(num)-1:
            cir_item+=1
            string+=num[cir_item]
            ins.append(string)
        item+=1    
    return ins

def string_sort(string):
    words = string.split(' ')
    word_array = []
    words_array = []
    for word in words:
        for item in range(len(word)):
            word_array.append(word[item])
        for item in range(len(word_array)):
            if not (ord('a')<=ord(word_array[item])<=ord('z') or ord('A')<=ord(word_array[item])<=ord('Z')):
                continue
            for item2 in range(item+1, len(word_array)):
                if word_array[item].lower()>word_array[item2].lower():
                    temp = word_array[item]
                    word_array[item] = word_array[item2]
                    word_array[item2] = temp
        wordjoin = ''.join(map(lambda x: str(x), word_array))
        words_array.append(wordjoin)
        word_array = []
    string = ' '.join(map(lambda x: str(x), words_array))
    return string

def string_fully_sort(string):
    word_array = []
    words_array = []
    others_array = []
    space_items = []
    colon_items = []
    for item in range(len(string)):
        if not (ord('a')<=ord(string[item])<=ord('z') or ord('A')<=ord(string[item])<=ord('Z')):
            if string[item]==' ':
                space_items.append(item)
            elif string[item]==':':
                colon_items.append(item)
            else:
                others_array.append(string[item])
        else:
            word_array.append(string[item])

    for item in range(len(word_array)):
        for item2 in range(item+1, len(word_array)):
            if word_array[item].lower()>word_array[item2].lower():
                temp = word_array[item]
                word_array[item] = word_array[item2]
                word_array[item2] = temp
    
    wordjoins = []
    for word in word_array:
        if len(wordjoins) in colon_items:
            wordjoins.append(':')
        if len(wordjoins) in space_items:
            wordjoins.append(' ')
        wordjoins.append(word)
    wordjoins.append(' ')
    wordjoins.extend(others_array)
    wordjoin = ''.join(map(lambda x: str(x), wordjoins))
    return wordjoin    

if __name__ == "__main__":
    print integer_in('123456789')
    print string_sort('A Famous Saying: Much Ado About Nothing (2012/8).')
    print string_fully_sort('A Famous Saying: Much Ado About Nothing (2012/8).')