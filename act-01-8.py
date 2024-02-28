# We're going to refactor our last example
# with functions.
# that loop is already starting to get messy!

from random import randint
from datetime import datetime

MAX_FAILED = 3
FAILS = 0
USERS = {
  "admin": {
    "name": "Administrator",
    "password": "password",
  },
  "member": {
    "name": "ProgSoc Guest Account",
    "password": "pogsoc2024",
  },
  "oli": {
    "name": "Oli",
    "password": "this-is-actually-my-1-real-password-or-is-it?",
  }
}

def log(text):
  with open("act-01-8-log.txt", "a") as f:
    f.write(f"[{datetime.now()}] {text}\n")

def plural(word, count):
  if count != 1:
    word += 's'
  return f"{count} {word}"

def fibonacci(n):
  if n < 2:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

def cmd_sum():
  a = float(input("Number a: "))
  b = float(input("Number b: "))
  print("Result a + b =", a + b)

def cmd_fib():
  n = int(input("n = "))
  print("fib(n) =", fibonacci(n))

def cmd_dice():
  print(randint(1, 6))

def cmd_help():
  print("+=@ Help Page @=+")
  print("* help")
  print("* exit")
  print("* sum")
  print("* fib")
  print("* rtd")

def prompt_login():
  username = input("Username: ")
  password = input("Password: ")
  if username in USERS:
    user = USERS[username]
    if password == user["password"]:
      log("Successful login for " + username + user["name"])
      return user
  return None

def prompt_command(user):
  command = input("Command> ")
  match command:
    case "exit":
      log("Log out for " + user["name"])
      return False
    case "sum":
      cmd_sum()
    case "fib":
      cmd_fib()
    case "rtd":
      cmd_dice()
    case _:
      cmd_help()
  return True

print("="*40)
print("Welcome to the Python Repl for Offline Grokking of Snake Oriented Code (PROGSOC)")
print("="*40)

# log-in loop
attempts = 0
while True:
  if attempts == MAX_FAILED:
    print("MAXIMUM FAILED ATTEMPTS REACHED!!!")
    print("COMMENCE SYSTEM SELF-DESTRUCT")
    break
  user = prompt_login()
  if user is None:
    attempts += 1
    print("Incorrect username or password.")
    remaining_attempts = MAX_FAILED - attempts
    print(f"You have {plural("attempt", remaining_attempts)} remaining!")
    continue

  print("Access Granted")
  with open("act-01-8-motd.txt") as f:
    print(f.read())

  # command loop
  while True:
    running = prompt_command(user)
    if not running:
      break
