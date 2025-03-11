def common_elements(list1, list2):
    common = list(set(list1) & set(list2))  
    common.sort()  
    return common


list1 = ["apple","banana","apple","toy","car","car"]
list2 = ["apple","banana","apple","bus","car"]
print(common_elements(list1, list2))  
