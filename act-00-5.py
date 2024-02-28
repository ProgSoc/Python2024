# Let's make a FizzBuzz counter

# for x in range(50):
# for x in range(1, 100, 2):
for x in range(1, 100):
  if x % 15 == 0:
    print("Shout FizzBuzz!")
  elif x % 5 == 0:
    print("Shout Buzz!")
  elif x % 3 == 0:
    print("Shout Fizz!")
  else:
    print("Say", x)
