# We'll make a interactive computer system for a user

passwords = {
  "admin": "password",
  "member": "pogsoc2024",
  "oli": "this-is-actually-my-1-real-password-or-is-it?"
}

username = input("Enter user name: ")
password_attempt = input("Enter password: ")
password_real = passwords[username]

if password_attempt == password_real:
  print("Access Granted.")
else:
  print("Access denied!!! Self-destruct: ENGAGED")
  print("Too much effort, do you have an account anyway?")
  print(username in set(passwords))

# sets can be written with {1, 2, 3}
# dictionaries can be on one line too { 1: "a", "c": 3 }
# tuples are like lists, but a fixed size
#   you can write them (4, 2, 3)
#   good for x/y/z coordinate systems
