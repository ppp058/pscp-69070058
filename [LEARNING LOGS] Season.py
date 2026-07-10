"""docstring"""
def main():
    """docstring"""
    month=int(input())
    day=int(input())
    if month <=3:
        if month==3:
            if day>=21:
                print("spring")
            else :
                print("winter")
        else:
            print("winter")
    elif month>3 and month<=6:
        if month==6:
            if day>=21:
                print("summer")
            else :
                print("spring")
        else:
            print("spring")
    elif month>6 and month<=9:
        if month==9:
            if day>=21:
                print("fall")
            else :
                print("summer")
        else:
            print("summer")
    elif month>9 and month<13:
        if month==12:
            if day>=21:
                print("winter")
            else :
                print("fall")
        else:
            print("fall")
main()
