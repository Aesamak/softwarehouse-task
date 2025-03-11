# Write a Python function that calculates the factorial of a given non-negative integer using recursion.
def factorial(x):
    if x == 0:
        return 1  
    else:
        return x * factorial(x - 1)  

a = factorial(5)
print(a)


# def factorial(x):
#     ans=1
#     if x == 0:
#         ans= 1  
#     else:
#         ans= x * factorial(x - 1) 
#     return ans 

# a = factorial(3)
# print(a)