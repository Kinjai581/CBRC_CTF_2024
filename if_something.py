'''You are writing a part of a program that is checking to see if a password is of the approrpriate length ( >= 8 characters ).

You will recieve a string value from the user below some_number = input(). You will need to:

    Turn it into a number (an integer) - technically called casting to an int
    evaluate the number to see if it is 8 or more characters
    return the flag cbrc_CTF(valid_password_length:[len])

where len is the length of the password'''





some_number = input()
number1 = int(some_number)

print(f"cbrc_CTF(valid_password_length:{number1})")
