def count_weight(weights, quantitys):
    quants = []
    quant = []

    item = 0
    for num in range(quantitys[item]+1):
        item+=1
        for num2 in range(quantitys[item]+1):
            item+=1
            for num3 in range(quantitys[item]+1):
                quant.append(num)
                quant.append(num2)
                quant.append(num3)
                quants.append(quant)
                quant = []
            item = 1
        item=0

    allweight = []
    for quant in quants:
        count = weights[0]*quant[0]+weights[1]*quant[1]+weights[2]*quant[2]
        allweight.append(count)

    reallweight = []
    for weight in allweight:
        if weight not in reallweight:
            reallweight.append(weight) 
    return reallweight

if __name__ == "__main__":
    print count_weight([1,2,5],[2,1,5])