b = int(input('Первый член?'))
q = int(input('знаменатель?'))
n = int(input('количество членов прогрессии?'))
for i in range(n):
f += 1
c = b * q ** f
print(c)