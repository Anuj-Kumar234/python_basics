def sayhi(name):
    print(f'Hi {name} !!')
sayhi('Anuj')
# ---------------------------------------------------
def add(a,b):
    return a+b
result=add(12.5,11)
print(result)
#-----------------------------------------------------
def check(a):
    if a % 2 ==0:
        print('Even')
    else:
        print('Odd')
check(3)                
# ------------------------------------------------------------------
def grade(mark):
    if mark == 10:
        print('Eggcellent !!')
    else:
        print('idiot !!')
grade(10)
# ----------------------------------------------------------------
def login(username,password):
    if username=='aka_harsh0' and password==123456:
        print('Login successfull ! ')
    else:
        print('Login failed !')
login('aka_harsh0',12345)