a,b,c = [float(i) for i in input("Enter a,b,c for ax^2+bx+c=0:").split()]
x1,x2 = (-b + (b ** 2 - 4 * a * c) ** 0.5)/(2*a),(-b - (b ** 2 - 4 * a * c) ** 0.5)/(2*a)
print(x1,",",x2)
