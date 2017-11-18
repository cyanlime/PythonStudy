#  1

#  1 3
#  2

#  1 3
#  2

#  1 3 6
#  2 5
#  4

#  1 3 6 10
#  2 5 9
#  4 8
#  7

def snake_matrix(num):
    """ [[1],[2,3],[4,5,6],[7,8,9,10]] """
    digit = []
    nums = []
    origin_item = 0
    for item in range(num):
        while len(digit)<item+1:
            digit.append(origin_item+1)
            origin_item+=1
        nums.append(digit)
        origin_item = digit[len(digit)-1]    
        digit = []

    matrix = []
    lines = []
    item2 = 0
    for item in range(len(nums)):
        while item2<len(nums):
            lines.append(nums[item2][item])
            item2+=1
        matrix.append(lines)
        lines = []
        item2 = item+1

    snake_matrix = []
    lines = []
    item2 = 0
    for item in range(len(matrix)):
        while item2<len(matrix[item]):
            lines.append(matrix[item2][item])
            item2+=1
        snake_matrix.append(lines)
        lines = []
        item2 = 0
    return snake_matrix

if __name__ == "__main__":
    snake_matrix = snake_matrix(7)
    for line in snake_matrix:
        print ' '.join(map(lambda x: str(x), line))
