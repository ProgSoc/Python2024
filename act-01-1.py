# We'll make a interactive computer system for a user

passwords = ["password", "pogsoc2024", "when4server?"]

user_id = int(input("Enter user id #: "))
password_attempt = input("Enter password: ")
password_real = passwords[user_id]

if password_attempt == password_real:
  print("Access Granted.")
else:
  print("Access denied!!! Self-destruct: ENGAGED")
