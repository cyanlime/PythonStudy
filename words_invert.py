def words_invert(string):
    invert_strings = []
    word = []
    for item in range(len(string)-1, -1, -1):
        if string[item]!=' ':
            word.append(string[item])
            continue
        if string[item]==' ':
            word = word[::-1]
            w = ''.join(map(lambda x: str(x), word))
            invert_strings.append(w)
            word = []
    invert_strings.append(string[item])
    string = ' '.join(map(lambda x: str(x), invert_strings))
    return string

def passintercept(string):
    positions = []
    for item2 in range(len(string)-1, -1, -1):

        item = 0
        while (item!=item2 or item!=item2-1) and item<len(string)-1:
            while string[item]!=string[item2]:
                item+=1
            
            #continue_item = item
            if string[item]==string[item2] and item!=item2:
                while string[item]==string[item2]:
                    positions.append(item)
                    item+=1
                    item2-=1
                    if (item==item2-1 or item==item2):
                        positions.append(item)
                        return positions

                if string[item]!=string[item2]:
                    item2 = len(string)-1
                    positions = []
                    item+=1
                    continue
            # else:
            #     item2 = len(string)-1
            #     positions = []
            #     item+=1


if __name__ == "__main__":
    print words_invert('I am a student')
    print passintercept('3454342511112332111114235445')