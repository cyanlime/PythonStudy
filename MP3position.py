def MP3_position(nums,operate):
    up = 0
    down = 0
    for item in range(len(operate)):
        if operate[item]=='U':
            up+=1
        if operate[item]=='D':
            down+=1
    if up>down:
        up-=down
        up%=nums
        down = 0
    else:
        down-=up
        down%=nums
        up = 0

    if up>0:
        if 0<up<5:
            num = nums-up+1
            numbers = []
            for item in range(nums-3, nums+1):
                numbers.append(item)

        if 5<=up<nums-4:
            num = nums-up+1
            numbers = []
            for item in range(num, num+4):
                numbers.append(item)

        if nums-4<=up<nums+1:
            num = nums-up+1
            numbers = []
            for item in range(1, 5):
                numbers.append(item)

    if down>0:
        if 0<=down<4:
            num = 1+down
            numbers = []
            for item in range(1,5):
                numbers.append(item)

        if 4<=down<nums-4:
            num = 1+down
            numbers = []
            for item in range(num, num+5):
                numbers.append(item)

        if nums-4<down<nums:
            num = 1+down
            numbers = []
            for item in range(nums-3,nums+1):
                numbers.append(item)
    return num, numbers

if __name__ == "__main__":
    num, numbers = MP3_position(23,'UUUUUDDDDDDUDUDUDDDUUUUUDDDDUUU')
    print num, numbers