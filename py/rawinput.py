import os

def make_text_file():
    a = open('test.txt', "w")
    a.write("this is how you create a new text file")
    a.close()

def make_another_file():
    if os.path.isfile('test.txt'):
        print ("You are trying to create a file that already exists!")
    else:
        f = open('test.txt', 'w')
        f.write("This is how you create a new text file")

def add_some_text():
    a = open('test.txt', "a")
    a.write("Here is some additional text!")

def even_more_text():
    a = open('test.txt', "a")
    a.write("""
        here is
        more
        text""")
    
def print_line_lengths():
    a = open("test.txt", "r")
    text = a.readlines()
    for line in text:
        print(len(line))

if __name__ == "__main__":
    make_another_file()
    add_some_text()
    even_more_text()
    f = open("test.txt", "r")
    # text = f.read()
    # print(text)
    print (f.readline())
    