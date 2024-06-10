si = input("Enter the string:")
p='''!()-[]{};:'",<>./?@#$%^&*_~'''
sip = ""
for i in si:
    if i not in p:
        sip = sip + i
print(sip)
