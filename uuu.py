with open("sample_data.csv", "r") as b:
    lines = b.readlines()
for i in lines:
    print(i)

with open("sample_data.csv", "a") as b:
    b.write("ali,23,lahore")
