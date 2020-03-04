def perfectdivision(a,b):
    try:
        return a//b
    except ZeroDivisionError:
        print("Divisor can't be zero")
print(perfectdivision(12,6))
print(perfectdivision(12,0))
