def foo (x, y):
    c = x > y
    return c

print(foo(1,2))

def fun(a,b):
  max = a if foo(a,b) else b
  return max

print (fun(1,2))

