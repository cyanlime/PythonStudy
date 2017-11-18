#!/usr/bin/env python 3.1

def do_plus(parm1, parm2):
    if type(parm1)==type("") and type(parm2)==type(""):
        result=parm1+parm2
    elif type(parm1)==int and type(parm2)==int:
        result=parm1+parm2
    else:
        raise TypeError("Param type is %s and %s, not the same" % (type(parm1), type(parm2)))
    return result

if __name__ == '__main__':
    number_result = do_plus(1, 2)
    str_result = do_plus("a", "b")
    result = do_plus(1, "a")
    print "Number result is %s" % number_result
    print "String result is %s" % str_result
    print "Result is %s" % result