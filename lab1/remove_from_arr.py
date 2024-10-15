a=[]
for x in range(0,10):
    b=int(input("Enter a number: "))
    a.append(b)

c=int(input("Enter a number to delete less: "))

for x in a[:]:
    if x < c:
        a.remove(x)

print(a)
