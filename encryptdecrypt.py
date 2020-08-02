def find_in_list(query, mainlist):
    mainlist_len = len(mainlist)
    range_for_loop = range(mainlist_len)
    index = None
    for i in range_for_loop:
        element = mainlist[i]
        if element == query:
            index = i
    return index
## print(find_in_list("o","broo"))
def encrypt_message(plain_msg):
    encrypted_msg = ""
    for character in plain_msg:
        if character in chars:
            char_index = find_in_list(character, chars)
            new_char = shifted_chars[char_index]
            encrypted_msg = encrypted_msg + new_char
        else:
            encrypted_msg = encrypted_msg + character
    return("meesage is encrypted:- "+""+str(encrypted_msg))
chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
## print(encrypt_message("snaaz"))
def decrypt_message(encrypted_msg):
    decrypted_msg = ""
    for character in encrypted_msg :
        if character in shifted_chars:
            char_index = find_in_list(character, shifted_chars)
            new_char = chars[char_index]
            decrypted_msg = decrypted_msg + new_char
        else:
            decrypted_msg = decrypted_msg + character
    return("message is decrypted:- "+""+str(decrypted_msg))
print(decrypt_message("pcxiwtwmwn"))
print(encrypt_message("navgurukul"))