scores = []
name = []
maxscores = 0
minscores = 100
total = 0
people = int(input('人數:'))
index = 0
hi = 0

for i in range(people):
    a = input("名字:")
    n = int(input("成績:"))
    scores.append(n)
    name.append(a)
    
    if n > maxscores:
        maxscores = n
        index = i
    if n < minscores:
        minscores = n
        hi = i
        
    total = total + n
    
s = total/len(scores)
print("總分:",total)
print("平均:",s)
print("最高分:",maxscores,name[index])
print("最低分:",minscores,name[hi])