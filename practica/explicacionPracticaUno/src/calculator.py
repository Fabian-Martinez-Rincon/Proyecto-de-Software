from src import operations

def calculate():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    choice = input("Enter choice(1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1,"+",num2,"=", operations.add(num1,num2))

    elif choice == '2':
        print(num1,"-",num2,"=", operations.subtract(num1,num2))
#    elif choice == '3':
#        print(num1,"*",num2,"=", operations.multiply(num1,num2))
#
#    elif choice == '4':
#        print(num1,"/",num2,"=", operations.divide(num1,num2))
#    else:
#        print("Invalid input")

def main():
    calculate()

if __name__ == "__main__":
    main()