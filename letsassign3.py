#using all arguments in one function or
#passing multiple arguments in a function 
#positional arguments
#default arguments 
#variable length arguments
#keyword grguments

def func1(a,b=12, *args, **kwargs): 
    c=a+b
    print(c)
    for i in args:
        print(i,end=" ")
    for i in kwargs:
        print(i)
func1(10,17)
func1(18)
func1(1,3,4,5,6)
func1(12,13,14,15,16)
#output
27
30
4
4 5 6 25
14 15 16 

