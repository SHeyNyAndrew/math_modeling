def area(figura, data):
    if figura == 'круг':
        print()
        res = 3.14*(a**2)
    if figura == 'квадрат':
        a,b = data
        res = a*b
    if figura == 'треугольник':
        res = (a*b)/2
    return (res)
    
figura = input('фигура ')
data = input(a, b)
print(area(figura))