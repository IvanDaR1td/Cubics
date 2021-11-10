name = input("What's your name?")
print("Hey",name.capitalize(),",I maybe can solve cubics")
a = int(input("a"))
b = int(input("b"))
c = int(input("c"))
d = int(input("d"))

def solvecubics1(a,b,c,d):
    alpha=(-b**3/27*a**3)+(b*c/6*a**2)-(d/2*a)
    beta=(((-b**3/27*a**3)+(b*c/6*a**2)-(d/2*a))**2)+((((c/3*a)-((b**2/9*a**2)))**3))**(1/2)
    delta=(b/3*a)
    root= (((alpha + beta) ** (1 / 3))+((alpha-beta) ** (1 / 3))-delta)
    return(root.real)
print("Root is",solvecubics1(a,b,c,d))

