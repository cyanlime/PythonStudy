import math
def num(max):
    nums = []
    for item in range(0, max):
        x = int(math.sqrt(item+100))
        y = int(math.sqrt(item+268))
        if (x*x==item+100) and (y*y==item+268):
            nums.append(item)
    return nums

def insert(array, num):
    if num>array[len(array)-1]:
        array.append(num)

    for item in range(0, len(array)):
        if num<array[item]:
            temp = array[item]
            array[item] = num

            if item+1<len(array):
                temp2 = array[item+1]
                array[item+1] = temp

            for item2 in range(item+1, len(array)-1):
                temp = temp2              
                temp2 = array[item2+1]           
                array[item2+1] = temp

            if item+1==len(array):
                array.append(temp)
            else:
                array.append(temp2)
            break
    return array

if __name__ == "__main__":
    print insert([1,2,3,4,6,7,9],5)
    print num(10000)