getName=input("Enter name: ")
f=open('demo.txt','a')
f.write(getName)
f.close()
f=open('demo.txt','r')
print(f.read())