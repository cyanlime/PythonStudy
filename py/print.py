# 1 [1*, 2, 3, 4, 5] 
# 2 [1, 2*, 3, 4, 5] 
# 3 [1, 2, 3*, 4, 5] 
# 4 [2, 3, 4*, 5, 6] 
# 5 [3, 4, 5*, 6, 7] 
# 6 [4, 5, 6*, 7, 8] 
# ...
# 16 [14, 15, 16*, 17, 18]
# 17 [15, 16, 17*, 18, 19]
# 18 [16, 17, 18*, 19, 20]
# 19 [16, 17, 18, 19*, 20]
# 20 [16, 17, 18, 19, 20*]


def printf(max):
    array = []
    for num in range(1,max+1):
        array.append(num)

    for row in range(1,4):
        lines = array[:5]
        for item in range(0, len(lines)):
            if lines[item]==row:
                lines[item]=str(lines[item])+'*'
        print "%s %s" % (row, lines)
    
    for row in range(4, max-1):
        lines = array[row-3:row+2]
        lines[2]=str(lines[2])+'*'
        print "%s %s" % (row, lines)

    for row in range(max-1, max+1):
        lines = array[-5:]
        for item in range(0, len(lines)):
            if lines[item]==row:
                lines[item]=str(lines[item])+'*'
        print "%s %s" % (row, lines)





if __name__ == "__main__":
    printf(20)