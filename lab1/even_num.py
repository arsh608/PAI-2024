a=[]
count=0
for x in range(0,10):
    b=int(input("Enter a number: "))
    a.append(b)
    if b%2==0:
        count +=1
print(a)
print("Even numbers are: ",count)
