import os
import shutil
import split

def make_version_path(path, version):
    if version == 0:
        return path
    else:
        return path + "." + str(version)

def rotate(path, max_keep, version=0):
    old_path = make_version_path(path, version)
    if not os.path.exists(old_path):
        raise IOError("'%s' doesn't exist" % path)

    new_path = make_version_path(path, version+1)
    if os.path.exists(new_path):
        if version < max_keep - 1:
            rotate(path, max_keep, version+1)
        else:
            os.remove(new_path)
    shutil.move(old_path, new_path)

    # if new_path == path+"."+str(max):
    #     os.remove(new_path)

    # path, filename = os.path.split(new_path)
    # name, ver = os.path.splitext(filename)

if __name__ == "__main__":
    #split.print_tree('/Users/codemeow/GitHub/StudyPython')
    file('/Users/codemeow/GitHub/StudyPython/web.log', "w")
    rotate('/Users/codemeow/GitHub/StudyPython/web.log', 5, 0)
