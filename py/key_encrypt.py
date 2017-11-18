def key_encrypt(key, data):
    """ generate alphabet """
    rekey = []
    for item in range(len(key)):
        if key[item] not in rekey:
            rekey.append(key[item])
    for alp in range(ord('A'), ord('Z')+1):
        if chr(alp) not in rekey:
            rekey.append(chr(alp))

    alphabet = []
    for alp in range(ord('A'), ord('Z')+1):
        alphabet.append(chr(alp))

    alphabet_items = []
    upper_items = []
    space_items = []
    for item in range(len(data)):
        if data[item].isupper():
            upper_items.append(item)
        for alpitem in range(len(alphabet)):
            if (data[item]).upper()==alphabet[alpitem]:
                alphabet_items.append(alpitem)
        if data[item]==' ':
            space_items.append(item)

    ciphertext = []
    for item in alphabet_items:
        cip = rekey[item]
        if len(ciphertext) not in upper_items:
            cip = cip.lower()
        ciphertext.append(cip)
        if len(ciphertext) in space_items:
            ciphertext.append(' ')

    cipher = ''.join(map(lambda x: str(x), ciphertext))
    return cipher

if __name__ == "__main__":
    cipher = key_encrypt('TRAILBLAZERS', 'Attack AT DAWN')
    print cipher