# Write a Python function that takes a list as input and returns a new list containing only the unique elements of the original list, preserving the order.
lis=["apple","banana","apple","toy","car","bus","car"]
def unlis(l):
    a=set(l)
    l=list(a)
    return l
print(unlis(lis))