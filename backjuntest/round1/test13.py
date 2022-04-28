# 2588
# 1의 자리를 구하려면 : a%10, b%10
# 10의 자리를 구하려면 : (a%100)-(a%10) (b%100)-(b%10)
# 100의 자리를 구하려면 : a-(a%100) b-(b%100)
a = int(input())
b = int(input())
c=a*(b%10)
d=a*((b%100)-(b%10))
e=a*(b-(b%100))
f=c+d+e
print(c)
print(d//10)
print(e//100)
print(f)