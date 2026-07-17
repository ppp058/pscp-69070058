"""INK"""
def main():
    """asdasd"""
    first=str(input()).split(" ")
    area=float(first[0])
    N=int(first[1])
    time=0
    r=0
    for _ in range(N):
        home=str(input()).split(" ")
        x=int(home[0])
        y=int(home[1])
        while (x**2+y**2)**0.5-r > 0:
            r=((area*time)/3.1416)**(1/2)
            time+=1
        if time == 0:
            print(0)
        else:
            print(time-1)
main()
