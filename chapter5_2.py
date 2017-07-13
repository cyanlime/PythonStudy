#!/usr/bin/env python 3.1

def do_plus(first, second):
    for param in (first, second):
        if type(param)!=type("") and type(param)!=type(1):
            raise TypeError("This function needs a string or an integer")
        return first+second

if __name__ == "__main__":
    num_result = do_plus(1, 3)
    str_result = do_plus("a", "b")
    #result = do_plus(1, "a")
    print "num_result is %s" % num_result
    print "str_result is %s" % str_result
    #print "result" % result
