import os

def print_dir(path):
    dirs = []
    files = []
    if not os.path.exists(path):
        raise IOError("'%s' doesn't exist." % path)
    
    #path = sorted(os.listdir(path))
    for name in sorted(os.listdir(path)):
        listpath = os.path.join(path, name)
        if os.path.isdir(listpath):
            #print "dirpath of %s is %s" % (path, listpath)
            path, dirname = os.path.split(listpath)
            dirs.append(dirname)

        if os.path.isfile(listpath):
            path, filename = os.path.split(listpath)
            files.append(filename)

    print "dirs is %s" % dirs
    print "filesname is %s" % files

if __name__ == "__main__":
    print_dir('/Users/codemeow/GitHub/StudyPython')

        


            