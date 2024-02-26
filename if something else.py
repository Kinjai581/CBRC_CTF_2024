password1 = int(input())
password2 = int(input())

if password1 >= 8 and password2 >= 8:
  print(f"cbrc_CTF(password1:valid_password2:valid)")

if password1 < 8 and password2 >= 8:
  print(f"cbrc_CTF(password1:invalid_password2:valid)")

if password1 >= 8 and password2 < 8:
  print(f"cbrc_CTF(password1:valid_password2:invalid)")

if password1 < 8 and password2 < 8:
  print(f"cbrc_CTF(password1:invalid_password2:invalid)")
