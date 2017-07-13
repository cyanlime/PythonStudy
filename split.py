import os

def split_fully(path):
    parent_path, name = os.path.split(path)
    if name == "":
        return (parent_path, )
    else:
        return split_fully(parent_path) + (name, )

def print_dir(dir_path):
    for name in os.listdir(dir_path):
        print (os.path.join(dir_path, name))

def print_tree(dir_path):
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        print full_path
        if os.path.isdir(full_path):
            print_tree(full_path)

if __name__ == "__main__":
    #print split_fully("/usr/bin/python")
    #print_dir('/Users/codemeow/GitHub/StudyPython/')
    print_tree('/Users/codemeow/GitHub/StudyPython/')
