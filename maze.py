def maze(array):
    tunnels = []
    min = 0
    for item in range(len(array)):
        for item2 in range(min, len(array[item])):
            if array[item][item2]==0:
                tunnels.append((item, item2))
            item2+=1
            if item2==len(array[item]):
                min = item2-1
                break
            else:
                if array[item][item2]==1:
                    min = item2-1
                    break
    return tunnels

if __name__ == '__main__':
    tunnels = maze([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,0,0],[0,1,1,1,0],[0,0,0,1,0]])
    for tunnel in tunnels:
        print tunnel