def three_tuple(array):
    i = 0
    for item in range(0, len(array)):
        for item2 in range(0, len(array)):
            for item3 in range(0, len(array)):
                if array[item] == array[item2]+array[item3]:
                    print "(array[%s]=array[%s]+array[%s])" % (item, item2, item3)
                    i+=1
    return i

def _01(sequence):
    pre_1 = 0
    seq_1 = 1
    post_sequence = []
    for item in str(sequence):
        if item=='1' and pre_1==0:
            pre_1=1
            post_sequence.append(item)
            continue

        if pre_1==1:
            if item=="1":
                seq_1+=1
                post_sequence.append(item)
                continue
            if item=="0" and seq_1==5:
                pre_1=0
                seq_1=1
                continue
            if item=="0":
                pre_1 = 0
                seq_1 = 1
                post_sequence.append(item)
                continue

        if item=='0':
            pre_1 = 0
            seq_1 = 1
            post_sequence.append(item)

    sequence = ''.join(map(lambda x: str(x), post_sequence))
    return sequence

def matrix(n, m):
    i = 0
    for item in range(1, n+1):
        if m%item==0 and m/item<=n:
            i+=1
    return i

def print_matrix(n):
    matrix_array = []
    array = []
    for item in range(1, n+1):
        matrix_array.append(array)

    matrix=0
    for matrix in range(0, len(matrix_array)):
        for item in range(1, n+1):
            matrix_array[matrix].append(item*(matrix+1))
    
    origin = matrix_array
    for item in range(len(matrix_array)):
        start = item*n
        end = (item+1)*n
        matrix_array=matrix_array[item][start:end]
        print ' '.join(map(lambda x: str(x), matrix_array))
        matrix_array = origin

def copy(s,l,r):
    t = s[l:r+1]
    return s,t
    
def cut(s,l,r):
    t = s[l:r+1]
    s_items = []
    for item in range(len(s)):
        if item<l or item>r:
            s_items.append(s[item])
    s = ''.join(map(lambda x: str(x), s_items))
    return s, t

def paste(s,t,p):
    s_items = []
    for item in range(p+1):
        s_items.append(s[item])
    for item in range(len(t)):
        s_items.append(t[item])
    for item in range(p+1,len(s)):
        s_items.append(s[item])
    s = ''.join(map(lambda x: str(x), s_items))
    return s


if __name__ == "__main__":
    print three_tuple([0,0])
    print _01('1111100111101111000000111110')
    print_matrix(8)

    s,t = cut('abcde',1,2)
    s1,t1 = copy(s,0,1)
    s2 = paste(s1, 'pqr', 1)
    s3 = paste(s2, 'pqr', 1)    
    s4,t4 = cut(s3,1,3)
    print s,s1,s2,s3,s4
   