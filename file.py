f=open('demo.txt','w')
f.write("kenya")#content to add to the file demo.txt
f.close()
f=open('demo.txt','r')
print(f.read()) 