"""undone"""

# 10,0,0
# 9+1
# 8+2 8,1,1  8,2
# 7+3 7,1,2  7,0,3
# 6+4 6,2,2  6,1,3  6,0,4
# 5+5 5,5,0  5,1,4  5,2,3  
# 4+6 4,6,0  4,5,1  4,4,2  4,3,3

# 1
# 2
# 3  1,2  3,0
# 4    2,2  3,1  4,0
# 5    5,0  4,1  3,2 
# 6    6,0  5,1  4,2  3,3
# 7    7,0  6,1  5,2  4,3  
# 8    8,0  7,1  6,2  5,3  4,4
# 9    9,0  8,1  7,2  6,3  5,4


# 32   32,0 .                   16,16



def put_apples(apples, plates):
    sum = 1
    for item in range(1,apples-1):
        sum+=(int(item/2)+1)
    return sum



    # all_plates = []
    # all_apples = []
    # apple = 0
    # origin_apples = apples
    # while len(all_plates)<plates:
    #     while apple<origin_apples and len(all_plates)<plates-1:
    #         all_plates.append(apple)
    #         apples-=apple
    #     if len(all_plates)==plates-1:
    #         all_plates.append(apples-apple)
    #     apple+=1
    #     all_apples.append(all_plates)
    #     all_plates = []

if __name__ == "__main__":
    put_apples(7,3)