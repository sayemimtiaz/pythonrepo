with open(self.models) as oldfile, open(new_name, 'w+') as newfile:
 a=2

with A() as a, B() as b, C() as c:
 doSomething(a,b,c)

with (A(),
      B(),
      C()):
 doSomething(a,b,c)

with A():
 hello()

with A() as b:
 hello()

with A() as a,B(),C() as c:
 hello()

with A(),B(),C() as c:
 hello()

with A(),B() as b,C():
 hello()

with A() as a:
    with B() as b:
        suite

with (A(),
      B(),
      C()) as T:
 doSomething(a,b,c)

with (A(),
      B(),
      C()) as T, B():
 doSomething(a,b,c)

with message_writer.open_file() as my_file: 
    my_file.write('hello world') 

def fun(a,*b,c):
	pass

def fun(a,*b,**c):
	pass

def fun(a,*b,*,d):
	pass

def fun(a,*b,*,**d):
	pass

def fun(*,a):
	pass

def fun(a,b=None,c:int):
	pass

def fun(**a):
	pass

def fun(b,*,c,**d):
    pass
