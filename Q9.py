s=input("Enter the string:")
ss=input("Enter the sub string:")
sx=s.split()
c=0
for i in sx:
    if i==ss:
        c+=1
if c>0:
    print("The substring is present in the string")
else:
    print("The substring is not present in the string")
