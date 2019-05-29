def adder(x,y):
 z=x+y

adder(12,14)
print("the sum of x and y is=",z)

def countdown(n):
      if n==0:
         print("blast off")
      else:
         print(n)
         countdown(n-1)    

countdown(5)
#print("countdown:")


def func1():
    print("line 1.")
    print("line 2.")
    
print("allow func",func1())

def func2(x): return 2*x
a=func2(5)
print(a)
    