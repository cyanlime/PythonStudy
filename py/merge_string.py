def merge_string(s1,s2):
    array = []

    if len(s1)>len(s2):
        rest = s1[len(s2):len(s1)]
    else:
        rest_s2 = s2[:len(s2)-len(s1)]
        reverse_s2 = []
        for item in range(len(rest_s2)-1, -1, -1):
            reverse_s2.append(rest_s2[item])
        rest = ''.join(map(lambda x: str(x), reverse_s2))

    for item in range(len(s1)):
        for item2 in range(len(s2)-1, -1, -1):
            if item+item2==len(s2)-1:
                array.append(s1[item])
                array.append(s2[item2])

    s = ''.join(map(lambda x: str(x), array))
    s+=rest
    return s, s1, s2

if __name__ == "__main__":
    s,s1,s2 = merge_string('abcdhhhkkk', 'defeee')
    print "%s merge to %s: %s" % (s1, s2, s)