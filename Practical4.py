def letter_to_int(letter: chr) -> int:
    return ord(letter.upper()) - 65

def word_to_int(word: str) -> list:
    nums = []
    for char in word:
        if char == " ":
            nums += [32]
        else:
            nums += [ord(char.upper()) - 65]
    return nums

def get_letter(num: int) -> str:
    return chr(num + 65)

def get_word(nums: list) -> str:
    word = ""
    for num in nums:
        if num == 32:
            word += " "
        else:
            word += get_letter(num)
    return word

def caesar_encrypt(message: str, key: int) -> str:
    salad = []
    for num in word_to_int(message):
        if num != 32:
            num += key
            salad += [num % 26]
        else:
            salad += [32]
    return(get_word(salad))

print(caesar_encrypt("abcxyz", 1))

def caesar_decrypt(message: str, key: int) -> str:
    salad = []
    for num in word_to_int(message):
        if num != 32:
            num -= key
            salad += [num % 26]
        else:
            salad += [32]
    return(get_word(salad))

def brute_force(ctext):
    for key in range(26):
        print(caesar_decrypt(ctext, key))

print("Caeser Cipher")
print("---------------------------------")

print(caesar_decrypt(caesar_encrypt("abcxyz", 1), 1))

print(brute_force("QJLTRWP RB ODW"))



from string import ascii_uppercase

subkey = ["F", "N", "R", "U", "Z", "J", "M", "P", "L", "X", "D", "S", "E", "H", "V", "W", "Y", "A", "C", "T", "B", "G", "I", "O", "K", "Q"]
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def substitution_encrypt(message: str) -> str:
    newMessage = ""
    for char in message:
        if char != " ":
            newMessage += subkey[letter_to_int(char)]
        else:
            newMessage += " "
    return newMessage


def substitution_decrypt(message: str) -> str:
    oldMessage = ""
    for char in message:
        if char != " ":
            oldMessage += alphabet[subkey.index(char)]
        else:
            oldMessage += " "
    return oldMessage
print("---------------------------------")
print("")
print("Substitution Cipher")
print("---------------------------------")

print(substitution_encrypt("Help Me"))

print(substitution_decrypt(substitution_encrypt("Help Me")))



def rank_in_block(plaintext: str, block_len: int):
    count = 0
    for char in plaintext:
        print(count)
        count += 1
        if count == block_len:
            count = 0

def encrypt_vigenere(plaintext: str, keystream: list):
    viniger = []
    count = 0
    for num in word_to_int(plaintext):
        if num != 32:
            num += keystream[count]
            viniger += [num % 26]
        else:
            viniger += [32]
        count += 1
        if count == len(keystream):
            count = 0
    return(get_word(viniger))

def decrypt_vigenere(ciphertext: str, keystream: list):
    viniger = []
    count = 0
    for num in word_to_int(ciphertext):
        if num != 32:
            num -= keystream[count]
            viniger += [num % 26]
        else:
            viniger += [32]
        count += 1
        if count == len(keystream):
            count = 0
    return(get_word(viniger))


print("---------------------------------")
print("")
print("Vigenère  Cipher")
print("---------------------------------")

rank_in_block("HelloWorld", 3)
print(encrypt_vigenere("Please kill me", [0,1,2,3]))
print(decrypt_vigenere(encrypt_vigenere("Please kill me", [0,1,2,3]), [0,1,2,3]))

print("---------------------------------")
print("")
print("Statistical  Cryptanalysis")
print("---------------------------------")

def statistics(ciphertext: str) -> list:
    frequencies = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],alphabet]

    for char in ciphertext:
        if char.isalpha():
            frequencies[0][ord(char.lower()) - 97] += 1
    return frequencies

def statistics_sort(frequencies: list):
    for x in range(len(frequencies[0])):
        for y in range(0, len(frequencies[0])-x-1):
            if frequencies[0][y] < frequencies[0][y+1]:
                frequencies[0][y], frequencies[0][y+1] = frequencies[0][y+1], frequencies[0][y]
                frequencies[1][y], frequencies[1][y+1] = frequencies[1][y+1], frequencies[1][y]
    return frequencies

ciphertext = "GFS WMY OG LGDVS MF SFNKYHOSU ESLLMRS, PC WS BFGW POL DMFRQMRS, PL OG CPFU M UPCCSKSFO HDMPFOSXO GC OIS LMES DMFRQMRS DGFR SFGQRI OG CPDD GFS LISSO GK LG, MFU OISF WS NGQFO OIS GNNQKKSFNSL GC SMNI DSOOSK. WS NMDD OIS EGLO CKSJQSFODY GNNQKKPFR DSOOSK OIS 'CPKLO', OIS FSXO EGLO GNNQKKPFR DSOOSK OIS 'LSNGFU' OIS CGDDGWPFR EGLO GNNQKKPFR DSOOSK OIS 'OIPKU', MFU LG GF, QFOPD WS MNNGQFO CGK MDD OIS UPCCSKSFO DSOOSKL PF OIS HDMPFOSXO LMEHDS. OISF WS DGGB MO OIS NPHISK OSXO WS WMFO OG LGDVS MFU WS MDLG NDMLLPCY POL LYEAGDL. WS CPFU OIS EGLO GNNQKKPFR LYEAGD MFU NIMFRS PO OG OIS CGKE GC OIS 'CPKLO' DSOOSK GC OIS HDMPFOSXO LMEHDS, OIS FSXO EGLO NGEEGF LYEAGD PL NIMFRSU OG OIS CGKE GC OIS 'LSNGFU' DSOOSK, MFU OIS CGDDGWPFR EGLO NGEEGF LYEAGD PL NIMFRSU OG OIS CGKE GC OIS 'OIPKU' DSOOSK, MFU LG GF, QFOPD WS MNNGQFO CGK MDD LYEAGDL GC OIS NKYHOGRKME WS WMFO OG LGDVS"

print(statistics_sort(statistics(ciphertext)))


    