# We're going to refactor our last example
# with a guard clause
# this makes our code tidier

MAX_FAILED = 3

# our users database is similar to a constant.
# although we might add users, it's something
# global (at the top-level, on the left) and it's
# good to differentiate it. we use it mostly like a constant
USERS = {
  "admin": {
    "name": "Administrator",
    "password": "password",
    "failed": 0,
  },
  "member": {
    "name": "ProgSoc Guest Account",
    "password": "pogsoc2024",
    "failed": 0,
  },
  "oli": {
    "name": "Oli",
    "password": "this-is-actually-my-1-real-password-or-is-it?",
    "failed": 0,
  }
}

# log-in loop
while True:
  print("="*40)
  print("Welcome to the Python Repl for Offline Grokking of Snake Oriented Code (PROGSOC)")
  print("="*40)
  username = input("Username: ")
  password = input("Password: ")

  if username in USERS:
    user = USERS[username]
    if password != user["password"]:
      user["failed"] += 1
      print(f"Access Denied. {MAX_FAILED - user["failed"]} attempts remaining.")
      if user["failed"] >= MAX_FAILED:
        print("ALARM RAISED. SELF-DESTRUCT SEQUENCE ENGAGING...")
        break
      continue

    print("Access Granted.")
    print(f"Welcome {user["name"]} to PROGSOC!")
    while True:
      cmd = input("Enter Command> ")
      if cmd == "exit":
        print("Thank you for using PROGSOC. Have a good day!")
        break
      elif cmd == "sum":
        a = float(input("Enter number a: "))
        b = float(input("Enter number b: "))
        print("Result a + b =", a + b)
      else:
        print("+=@ Help Page @=+")
        print("Command List:")
        print("* help")
        print("* exit")
        print("* sum")
  else:
    print("Sorry, we don't know that user. Try again.")
