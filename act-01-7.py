# Basic Functions

def sum(a, b):
  return a + b

sum(2, 3)

def my_add(a, b=2):
  return a + b

my_add(5)

def stub():
    pass

def complex_add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def adv_fn(arg0, *args, **kwargs):
  print(arg0)
  print(args)
  print(kwargs)
