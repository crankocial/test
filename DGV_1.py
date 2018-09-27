def foo (x, y):
    c = x > y
    return c

def fun(a,b):
  max = a if foo(a,b) else b
  return max



print ("enter numbers to compare")
print ("a=", end='')
a=input()
print ("b=", end='')
b=input()

if fun(a,b)==a:
    min=b;
else:

    min=a;


print (fun(a,b), '>', min)

