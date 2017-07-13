def derivate(a,b,c,d,x0):
    de = 3*x0*x0*a+2*b*x0+c
    print "f'(x0)=%s" % de

if __name__ == "__main__":
    derivate(1,1,1,1,1)