def add3(x,y,z):
    num = x+y+z
    return num

a = int(input('請輸入第一個數字:'))
b = int(input('請輸入第二個數字:'))
c = int(input('請輸入第三個數字:'))
total = add3(a,b,c)
print('總和',total)