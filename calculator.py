def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
def precent(a,b):
    return a/b*100

def calculator():
    print("Select Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Precentage")

    while True:
        choice = input("Enter Choice (1,2,3,4,5): ")

        if choice in ['1','2','3','4','5']:
            try:
                a=float(input("Enter First Number: "))
                b=float(input("Enter Second Number: "))
            except ValueError:
              print("Invalid ! Please enter a number")
              continue
            if choice == '1':
              print(f"{a}+{b}={add(a,b)}")

            elif choice == '2':
              print(f"{a}-{b}={sub(a,b)}")
              
            elif choice == '3':
              print(f"{a}*{b}={multi(a,b)}")
              
            elif choice == '4':
              print(f"{a}/{b}={div(a,b)}")

            elif choice == '5':
              print(f"{a}/{b}*100={precent(a,b)}")
              
            else:
              print("Invalid Input!")

            next_calculation = input("Press for next calculation [Yes(y)/No(n)]: ")
            if next_calculation.lower() != 'y':
                break
calculator()
