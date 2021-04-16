x = 1

def func():
    #x = 2 
    def innerfunc():
        #x = 3
        print('locals',x) #1
    innerfunc()
    print('enclosing function locals',x) #1
func()
print('global',x) #1

#程式執行順序
# 1 > 10 > 3 > 4 > 8 > 5 > 6 > 7 > 9 > 11