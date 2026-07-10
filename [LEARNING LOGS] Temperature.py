"""docstring"""
def main():
    """sada"""
    num=float(input())
    a=input()
    b=input()
    c=float
    if a=="F":
        c=((num-32)*5)/9
    elif a=="K":
        c=num-273.15
    elif a=="R":
        c=((num*5)/9)-273.15
    elif a=="C":
        c=num
    match b :
        case "F":
            result=((c*9)/5)+32
            print(f"{result:.2f}")
        case "K":
            result=c+273.15
            print(f"{result:.2f}")
        case "R":
            result=((c+273.15)*9)/5
            print(f"{result:.2f}")
        case "C":
            result=c
            print(f"{result:.2f}")
main()
