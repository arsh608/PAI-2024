a = ["He", "th", "i", "sal"]
b = ["llo", "is", "s", "man"]

c = zip(a,b)
result=[]
for i,j in c:
    result.append(i+j)

print(result)
