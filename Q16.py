string=input("Enter the string:")
dict={}
for ch in string:
    if ch in dict:
        dict[ch]+=1
    else:
        dict[ch]=1
for key in dict:
    print(key,":",dict[key])
