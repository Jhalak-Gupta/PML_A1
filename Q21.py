list=eval(input("Enter the list of numbers:"))
el=eval(input("Enter the element:"))
cnt=0
for i in range(0,len(list)):
    if el==list[i]:
        cnt+=1
if cnt==0:
    print("Not found")
else:
    print("Frequency=",cnt)
