#1+1/2+1/3+1/4......1/n
summ = 0

n = int(input("n = "))
num = list(range(1,n+1,1))

for x in num:
    summ = summ+(1/x)
print(summ)    
