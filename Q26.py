s1=input("Enter the string:")
sp=input("Enter the prefix:")
sf=input("Enter the suffix:")
if s1[0]==sp:
    print("String starts with the prefix")
else:
    print("String does not start with the prefix")
if s1[-1]==sf:
    print("String ends with the suffix")
else:
    print("String does not end with the suffix")
