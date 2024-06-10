string1=input("Enter the first string: ")
string2=input("Enter the second string: ")
stringx1=sorted(string1)
stringx2=sorted(string2)
if len(stringx1)!=len(stringx2):
    print("The strings are not anagrams of each other.")
else:
    if stringx1==stringx2:
        print("The strings are anagrams of each other.")
    else:
        print("The strings are not anagrams of each other.")
