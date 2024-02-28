# This is all getting repetitive,
# especially having to restart the program every time!

# We're gonna build on that simple for-loop from earlier,
# and make our own REPL

# But first, some examples of these loops
# so we get an idea of how they work
# and how we can use them to help us

items = [2, 7, 3, 8]
for x in items:
  print(x)

i = 0
while i < 10:
  print(i)
  i += 1

skip = int(input("What number from 1-10 do you want to skip?"))
# remember, the second value is up-to-but-not-including
for i in range(1, 11):
  if i == skip:
    continue
  print(i)

cutoff = int(input("Normally we'd count all the way, but what number (1-10) do you want to cut off at?"))
for i in range(1, 11):
  if i == cutoff:
    break
  print(i)
