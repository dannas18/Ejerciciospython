años=int(input("digite el año"))
if años%4==0 and años%100!=0 or años%400==0:
    print(f"el{años} es bisiesto")
else:
    print(f"el {años} no es bisiesto")
    