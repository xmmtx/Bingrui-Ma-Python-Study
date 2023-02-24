a=10
def func():
    global a
    a=20
    print(a)
func()
print(a)