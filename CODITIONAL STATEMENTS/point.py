def point(x,y):
    match(x,y):
        case(x,0):
            return f"x-axis at x={x}"
        case(0,y):
            return f"y-axis at y={y}"
        case _:
            return "don't exist"
print (point(7,0))
