# python function scope tests
def scope_test():
    spam = "global spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "make it global baby spam"
    def do_local():
        spam = "local spam"

        def do_nonlocal1():
            nonlocal spam
            spam = "nonlocal1 spam"
        def do_local1():
            spam = "local spam1"


        do_nonlocal1()
        print(f'nonlocal1 spam is {spam}')
        do_local1()
        print(f'local spam 1 is {spam}')
    do_nonlocal()
    print(f'nonlocal spam is {spam}')
    do_global()
    print(f'global spam is {spam}')
    do_local()
    print(f'local spam is {spam}')

scope_test()
print(f'scope_test spam is {spam}')
