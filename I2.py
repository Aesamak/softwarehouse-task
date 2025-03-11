# Write a Python function to check if a given string is a palindrome (reads the same forwards and backwards). Ignore case and spaces.
a="RADAR"
b="A SANTA AT NASA"
def removeSpaces(string):
    string = string.replace(' ','')
    return string
def backwards(a1):
    a=a1
    c=a[-1:-(len(a)+1):-1]
    return c
def palindrome(sr):
    ns=removeSpaces(sr)
    bw=backwards(ns)
    if bw==ns:
        print(f"{sr} is a palindrome")
    else:
        print(f"{sr} is not a palindrome")
palindrome(b)
