def win(a, b):
    if 1<=len(b)<5:
        card = {}
        for item in range(len(b)):
            if b[item]!=b[0]:
                return "please play again"
            else:
                if b[item] not in card:
                    card[b[item]]=1
                else:
                    card[b[item]]+=1

        nums = []
        for item in range(len(a)-len(b)+1):
            if int(a[item])>int(card.keys()[0]):
                for item2 in range(item, item+len(b)):
                    if int(a[item2])>int(card.keys()[0]):
                        nums.append(a[item2])
                
                for num in range(1,len(nums)):
                    if nums[num]!=nums[0]:
                        nums = []
                        break

                if len(nums)>1 and num==len(nums)-1 and nums[num]==nums[0]:
                    return "a is bigger"
                if len(nums)==1:
                    return "a is bigger"    
            if item==len(a)-len(b):
                return "a is smaller"

    if len(b)==5:
        card = {}
        for item in range(1,len(b)):
            if int(b[item])!=int(b[item-1])+1:
                return "please play again"
            else:
                if b[item] not in card:
                    card[b[item]]=1
                else:
                    card[b[item]]+=1
        card[b[0]]=1

        cards = {}
        for item in range(len(a)):
            if a[item]>b[0]:
                if a[item] not in cards:
                    cards[a[item]] = 1
                else:
                    cards[a[item]]+=1

        sorted_card = []
        for item in cards.keys():
            sorted_card.append(int(item))
        sorted_card.sort()

        single_card = ''.join(map(lambda x: str(x), sorted_card))

        single_cards = []
        if len(single_card)>=len(b):
            for item in range(len(single_card)-len(b)+1):
                if single_card[item]>b[0]: 
                    for item2 in range(item+1, item+len(b)):
                        if int(single_card[item2])==int(single_card[item2-1])+1:
                            single_cards.append(single_card[item2])
                        else:
                            new_single_card = single_card[item2]
                            single_cards = []
                            single_cards.append(new_single_card)
                    if len(single_cards)==len(b)-1 and int(single_cards[0])==int(single_card[item])+1:
                        single_cards.append(single_card[item])
                        return ''.join(map(lambda x: str(x), single_cards))
                    else:
                        single_cards = []

            if len(single_cards)!=len(b):
                return 'a is smaller than b'
        else:
            return 'a is smaller than b'

if __name__ == "__main__":
    # print win('1223345566677', '3')   
    # print win('1223345566677', '33')
    # print win('667788', '333')
    # print win('1223345566677', '333')
    # print win('122334455666677', '3333')
    print win('122356667789', '23456')
    print win('1223356667789', '34567')
    print win('12233446667789', '45678')
    print win('122334456667789', '56789')