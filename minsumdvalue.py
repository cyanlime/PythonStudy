def sort(a, b):  
    for num in b:
        a.append(num)
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if a[i]>a[j]:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
    Source = a
    return Source

def sum(source):
    total = 0
    for item in source:
        total+=item
    return total

if __name__ == "__main__":
    Source=sort([1,34,23,2,2,4,5,6],[7,44,55,6,5,67,666,789,98,75,4,3,2,1])
    print Source
    Big=Source[-1]
    Small=Source[-2]

    max = []
    min = []
    for item in range(0, len(Source[:-2])):
        if item%2==0:
            min.append(Source[item])
        else:
            max.append(Source[item])
    print min,max
    min.append(Big)
    max.append(Small)
    min_sum = sum(min)
    max_sum = sum(max)
    print min_sum,max_sum
    if min_sum>max_sum:
        temp = min
        min = max
        max = temp

        temp2=min_sum
        min_sum=max_sum
        max_sum=temp2
        
    print '%s sum of min is %s, %s sum of max is %s' % (min, min_sum, max, max_sum)