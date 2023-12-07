def square(fig, *args):
    if fig == 'круг':
        S =2 * 3.14*args[0]**2
    if fig == 'прямоугольник':
        S = args[0] * args[1]
    if fig == 'треугольник':
        S = (args[0] * args[1])/2
    return (S)

print(square('круг', 2))
    
