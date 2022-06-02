
'''accept a character from the user findout the given char
is vowel or con '''

n=input("Enter any char : ")  #X
lst=['A','a','E','e','I','i','O','o','U','u'] #list
s="AaEeIiOoUu" #str

#if n=='a' or n=='A' or n=='e' or n=='E' or n=='i' or n=='I' or n=='o' or n=='O' or n=='u' or n=='U':
#if n in lst:

if n in s:
    print("Vowel")
else:
    print("Not Vowel")
