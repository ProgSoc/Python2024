# You should code this into a file, "input_demo.py"

print("Hi! I'm PyBot.")
name = input("What's your name? ")

print("Hi", name)
# print(f"Hi {name}! Nice to meet you.\nI calculated your name is {len(name)} characters long!")

x = int(input("Enter a number: "))
print(f"Now I'll add one to it: {x + 1}")

user_float = float(input("Enter a decimal: "))
print("input / 7 =", user_float / 7)

num = int(input("Enter a number: "))
print("Here's a statement...")
print("  Your number is odd.")
print("What I said was", num % 2 == 1)
