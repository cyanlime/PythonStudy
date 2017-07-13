def sum_of_matrix_diagonal(two_D_array):
    sum = 0
    for item in range(len(two_D_array)):
        # if len(two_D_array)!=len(item):
        #     raise TypeError("The two_dimensional array is a %s X %s array") % (len(two_D_array), len(item))
        for item2 in range(len(two_D_array[item])):         
            if item == item2:
                sum+=two_D_array[item][item2]
    return len(two_D_array), sum



if __name__ == "__main__":
    two_D_array = [[1,2,3,4],[2,3,4,4],[3,4,5,6],[1,2,3,4]]
    sum = sum_of_matrix_diagonal(two_D_array)
    print "The sum of matrix diagonal of %sx%s two_D_array is %s" % (sum[0], sum[0], sum[1])