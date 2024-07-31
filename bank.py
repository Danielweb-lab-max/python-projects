records={
    "client":"Steve",
    "account":"1234",
    "balance":10000

}
def getBalance():
    account=input("Enter account: ")
    if account == "1234":
        print(records["balance"])
    else:
        print("Invalid account")
def menu():
    print("Welcome to Jamia Bank")
    print("1.check balance")
    choice=int(input("Enter choice: "))
    if choice==1:
        getBalance()
    else:
        print("Invalid choice")
def calc():
    return 1+1
print(calc())