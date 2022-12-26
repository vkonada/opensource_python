def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

'''
first == Geeks
mid == for
last == Geeks
'''


#Python program to illustrate *args with a first extra argument

def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)
 
 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

'''
First argument : Hello
Next argument through *argv : Welcome
Next argument through *argv : to
Next argument through *argv : GeeksforGeeks
'''


def myFun(*argv):
    for arg in argv:
        print(arg)
 

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
