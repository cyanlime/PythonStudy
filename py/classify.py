def classify(characters):
    letter = 0
    space = 0
    digit = 0

    for item in range(0, len(characters)):
        if characters[item].isalpha():
            letter+=1
        if characters[item].isspace():
            space+=1
        if characters[item].isdigit():
            digit+=1     
    return characters, letter, space, digit

if __name__ == "__main__":
    characters, letter, space, digit = classify('adbj  33d 33 dddd')
    print 'Of %s, the number of letter is %s, space is %s, digit is %s' % (characters, letter, space, digit)
