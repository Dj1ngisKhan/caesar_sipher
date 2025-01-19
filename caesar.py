import tkinter as tk

latin = list("abcdefghijklmnopqrstuvwxyz")

#encrypt_msg = input("")
#encrypt_key = input("")

msg = "a"
key = 26

def enkryptera(msg, key):
    new_msg = ""
    for stav in msg:
        while True:
            try:
                new_msg += latin[latin.index(stav) + key]
                break
            except Exception:
                key = key - len(latin)

    return new_msg


krp = enkryptera(msg, key)

print(krp)



def dekryptera_key(krypt_msg, key):
    dekrypt_msg = ""
    decrypt_key = 0
    for bit in krypt_msg:
        while True:
            try:
                decrypt_key = latin.index(bit) - key
                dekrypt_msg += latin[decrypt_key]
                break
            except Exception:
                key = key - len(latin)


    return dekrypt_msg

meddelande = dekryptera_key(krp, key)

print(meddelande)




def find_word(decrypt_msg):
    pass