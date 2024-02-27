def valid_encryption(et, cv):
    if et == "AES" and cv == "True" or et == "RSA" and cv == "True":
        return f"cbrc_CTF({et}:{cv}:connection_secure)"
    else:
        return f"cbrc_CTF({et}:{cv}:connection_not_secure)"
        
        

for i in range(4):
    word = input()
    splitword = word.split(":")
    hey = splitword[0]
    fong = splitword[1]
    print(valid_encryption(hey, fong))
    
    

    
