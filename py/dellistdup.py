if __name__ == "__main__":
    a = "abcdegzefegehedgeeddhc"
    #print a
    import sys
    print "please input a string:"
    a = str(sys..readline())
    if len(a)>100 or len(a)=0:
        print "please input a string, length no more than 100" 
    simplelist = []
    for item in a:
        if item not in simplelist:
            simplelist.append(item)
            print item
    