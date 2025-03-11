# Write a Python function that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string (case-insensitive).
def count_vowels(str):
    c=0
    vl=["a", "e", "i", "o", "u"]
    for i in str:
        if i in vl:
            c+=1
    return c 
a="aesam"
print(count_vowels(a))   