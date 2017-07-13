def encrypt(num):
    thousands = num/1000
    hundreds = (num-thousands*1000)/100
    tens = (num-thousands*1000-hundreds*100)/10
    units = num-thousands*1000-hundreds*100-tens*10

    thousands = (thousands+5)%10
    hundreds = (hundreds+5)%10
    tens = (tens+5)%10
    units = (units+5)%10

    print units*1000+tens*100+hundreds*10+thousands

if __name__ == '__main__':
    encrypt(1000)