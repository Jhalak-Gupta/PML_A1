lines=[]
while True:
    line=input("Enter text lines:")
    if line!=" ":
        lines.append(line)
    else:
        break
for line in lines:
    print(line)
