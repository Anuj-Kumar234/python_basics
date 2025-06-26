try:
    a=int(input('Enter an Integer: '))
    b=int(input('Enter an Integer: '))
    result=int(a/b)
    print(result)
except ValueError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)
try:
    file1=open("text.txt","r")
    for r in file1:
        print(r)
    file1.close()
except FileNotFoundError as err:
    print(err)