print("1. celsius to F \n 2. F to Celsius \n 3. Exit")

while True:
    n = int(input("Choice.:"))
    if n=="":
        print("please select correct choice")
        continue 
    if n==1:
        c = float(input("ENTER TEMP.:"))
        f = ((9/5)*c + 32)
        print(f)
    if n==2:
        f = float(input("ENTER TEMP.:"))
        c = (f-32)*(5/9)
        print(c)
    if n==3:
        break
     
