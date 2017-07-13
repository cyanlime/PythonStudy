def error_record(array):
    records = {}
    for item in array:
        splited = item.split(' ')
        val = None
        if splited[0] not in records:
            val = records[splited[0]] = []
        else:
            val = records[splited[0]]
        val.append(splited[1])
    #return records
    # records = {}
    # for item in array:
    #     is_dir = 0
    #     info = []
    #     for char in range(len(item)):
    #         if item[char]!=' ':
    #             info.append(item[char])
    #         if item[char]==' ' and is_dir==0:
    #             dir = ''.join(map(lambda x: str(x), info))
    #             is_dir = 1
    #             info = []
    #             continue
    #         if char==len(item)-1:
    #             linenum = ''.join(map(lambda x: str(x), info))
    #     if dir not in records:
    #         records[dir] = []
    #         records[dir].append(int(linenum))
    #     else:
    #         records[dir].append(int(linenum))
    # return records

    error_records = []
    for key in records.keys():
        filenames = []
        for item in range(len(key)-1,-1,-1):
            if key[item]!='\\':
                filenames.append(key[item])
            if key[item]=='\\':
                if len(filenames)>16:
                    filenames=filenames[:16]
                filenames=filenames[::-1]
                filename = ''.join(map(lambda x: str(x), filenames))
                break
        linenum = {}
        for value in records[key]:
            if value not in linenum:
                linenum[value]=1
            else:
                linenum[value]+=1
        for key, value in linenum.items():
            record = filename+' '+key+' '+str(value)
            error_records.append(record)
    return error_records

if __name__ == "__main__":
    error_records = error_record(['E:\\V1R2\\product\\abc.c 1325', 'E:\V1R2\product\\abc.c 1325', 'E:\V1R2\product\\bcd.c 1326',
    'D:\V1R2\product\\def.c 1326', 'E:\V1R2\product\\bcd.c 1325'])
    for error in error_records:
        print error