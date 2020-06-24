x=1
y=2
def f():
  global x,y
  a=x if y==2 else z
  print(x,y,z)
  hello(a)

f()
