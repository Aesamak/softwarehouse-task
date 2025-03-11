# Write a Python function that takes a list of numbers as input and returns their average. Handle empty lists by returning None.
lis=[]
def average(lis):
    sum=0
    for i in lis:
        sum+=i
    avg=sum//(len(lis))
    print(avg)

if lis:
    average(lis)
else:
    print("list is empty")