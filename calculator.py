def calculateSum():
    print("*****Calculate Sum*****")
    value1=int(input("Enter value 1: "))
    value2=int(input("Enter value 2: "))
    sum=value1+value2
    print(sum)
def calculateProduct():
    print("*****Calculate Product*****")
    value1=int(input("Enter value 1: "))
    value2=int(input("Enter value 2: "))
    product=value1*value2
    print(product)
def menu():
    print("Welcome to our calculator")
    print("1.Sum")
    print("2.Multiplication")
    choice=int(input("Enter choice: "))
    if choice ==1:
        calculateSum()
    elif choice ==2:
        calculateProduct()
    else:
        print("Invalid choice")
menu()