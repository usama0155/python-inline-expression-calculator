#Using single line to get complete data from user
def main():
    x, y, z = rec_conv_data()
    print(f"Output using {y} Operator: {calculations(x,y,z)}")

def rec_conv_data():

    user_data = input("Enter Your Statements: ").replace(" ", "")
    for op in ["+", "-", "*", "/"]:
        if op in user_data:
            x, z = user_data.split(op)
            return int(x), op, int(z)

def calculations(x,y,z):
    if y == "+":
        return x + z 
    elif y == "-":
        return x- z
    elif y == "*":
        return x * z
    elif y == "/":
        if z != 0:
            return x / z
        else:
            return "Cant Divide by zero"
    else:
        return "Operator not found!"

main()