num=eval(input("Enter the number:"))
sum=0
while num>0:
    d=num%10
    sum=sum+d
    num//=10
print("Sum of digits=",sum)
