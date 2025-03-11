# Write a Python program that reads a text file and prints the total number of words in the file.
with open("AA.txt", "r") as b:
    lines = b.readlines()
nw=0
for line in lines:
    l=line.split(" ")
    nw+=len(l)
print(f"total number of words in the file is : {nw}")