x = 1;
print(x)

#binds x again, shadowing that old one from above
y = '6';
print(x+y)

#declare, init
something = None
x = 5
print("x, something", x, something)

something = x * 5
print("x, something", x, something)


#mutability
y = 0
y = y * 2 + x
print(y)

BLAH = 42 #only const by convention
y *= BLAH

