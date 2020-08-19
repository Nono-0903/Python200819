def circle_area(x):
    num = x*x*3.14
    return num


n=int(input("請輸入半徑:"))
n=circle_area(n)
print("圓面積:",n)

def circle_circum(y):
    n = y*2*3.14
    return n

n=int(input("請輸入半徑:"))
n=circle_circum(n)
print("圓周長:",n)