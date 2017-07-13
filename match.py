def match(array):
    commands = ['reset', 'reset board', 'board add', 'board delet', 'reboot backplane', 'backplane abort']

    split_commands = {}
    split_key1 = []
    split_key2 = []
    for command in commands:
        if len(command.split(' '))==1:
            item = 1
            while len(split_key1)<len(command):
                split_key1.append(command[:item])
                item+=1
            split_commands[command] = split_key1
            split_key1 = []
        if len(command.split(' '))==2:
            key1, key2 = command.split(' ')
            item = 1
            while len(split_key1)<len(key1):
                split_key1.append(key1[:item])
                item+=1
            item = 1
            while len(split_key2)<len(key2):
                split_key2.append(key2[:item])
                item+=1
            split_commands[command] = []
            split_commands[command].append(split_key1)
            split_commands[command].append(split_key2)
            split_key1 = []
            split_key2 = []

    for item in array:
        if len(item.split(' '))==1:
            keyword = item
            if keyword in split_commands['reset']:
                print 'reset what'
            else:
                print "unknown command"
           
        if len(item.split(' '))==2:
            keyword1, keyword2 = item.split(' ')
            if (keyword1 in split_commands['reset board'][0]) and (keyword2 in split_commands['reset board'][1]):
                print 'board fault'
            elif (keyword1 in split_commands['board add'][0]) and (keyword2 in split_commands['board add'][1]):
                if (keyword1 in split_commands['backplane abort'][0]) and (keyword2 in split_commands['backplane abort'][1]):
                    print 'unknow command'
                    continue
                print 'where to add'
            elif (keyword1 in split_commands['board delet'][0]) and (keyword2 in split_commands['board delet'][1]):
                print 'no board at all'
            elif (keyword1 in split_commands['reboot backplane'][0]) and (keyword2 in split_commands['reboot backplane'][1]):
                print 'impossible'
            elif (keyword1 in split_commands['backplane abort'][0]) and (keyword2 in split_commands['backplane abort'][1]):
                print 'install first'
            else:
                print "unknown command"
        
if __name__ == "__main__":
    match(['reset', 'reset board', 'board add', 'board delet', 'reboot backplane', 'backplane abort', 'r', 'res', 'reb', 'r b', 'b a', 'bo a'])