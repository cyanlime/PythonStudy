#list = [1, 2, 3, 4]

if __name__ == "__main__":
    i=0
    for num1 in range(1, 5):
        for num2 in range(1, 5):
            for num3 in range(1, 5):
                if (num1==num2) or (num1==num3) or (num2==num3):
                    continue
                num = num1*100+num2*10+num3
                i+=1
                print i,num

    