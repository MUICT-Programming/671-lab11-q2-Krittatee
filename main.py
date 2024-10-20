def sum(list1, list2):
    updated_list = [list1[i] + list2[i] for i in range(len(list1))]
    return updated_list

def mm(list):
    return (min(list), max(list))
n = int(input())
list1 = []
list2 = []

for i in range(n):
    list1.append(int(input()))

for i in range(n):
    list2.append(int(input()))

updated_list = sum(list1, list2)
print(updated_list)

min_val, max_val = mm(updated_list)
print(((min_val), (max_val)))
