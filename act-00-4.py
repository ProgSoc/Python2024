# Let's make a FizzBuzz checker

x = int(input("Enter a number: "))
if x % 15 == 0:
  print("Shout FizzBuzz!")
elif x % 5 == 0:
  print("Shout Buzz!")
elif x % 3 == 0:
  print("Shout Fizz!")
else:
  print("Say", x)
