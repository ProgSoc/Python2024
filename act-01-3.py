# We'll make a interactive computer system for a user

users = {
  "admin": {
    "name": "Administrator",
    "password": "password"
  },
  "member": {
    "name": "ProgSoc Guest Account",
    "password": "pogsoc2024"
  },
  "oli": {
    "name": "Oli",
    "password": "this-is-actually-my-1-real-password-or-is-it?"
  }
}

username = input("Enter user name: ")
password_attempt = input("Enter password: ")

if users[username]["password"] == password_attempt:
  print("Access Granted.")
  print(f"Welcome {users["username"]}!")
else:
  print("Access denied!!! Self-destruct: ENGAGED")
