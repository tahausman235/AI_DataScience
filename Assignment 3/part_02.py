# PART 2
# Q:1
List = ["Tahir", 44, "AI and Data Science", True]
for item in List:
    print(item)

# Q:2

for items in List:
    if type(items)==str:
        print("STRING: ",items)
    elif type(items)==int:
        print("INTEGER: ",items)
    else:
        print("BOOLEAN: ",items)

# Q:3

list = ["apple", "raspberry", "pineapple", "cherry"]
# a:
if "apple" in list:
    index = list.index("apple")
    print("apple is present in index...",index)
else:
    print("apple not found")

# b:

list[1:3] = ["orange"]
print(list)

# c:
list.insert(2,"apricot")
print(list)

# d:
list.extend(["car","bike","aeroplane"])
print(list)

# Q:4

Scores_list = [40, 89, 90, 89, 23, 90, 50]
Scores_list.sort()
not_in_list = []
for i in Scores_list:
    if i not in not_in_list:
        not_in_list.append(i)
print(not_in_list)

first = not_in_list[-1]
print("First is ",first)
sec = not_in_list[-2]
print("Second is ",sec)

# Q:5

list = [32,54,66,11,77,10,90]

l = [num for num in list if num >= 20]
print(l)

l.sort()
print("Ascnding order: ",l)

l.sort(reverse=True)
print("Descending order: ",l)

# Q:6
Gadgets = ["Mobile", "Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]

strings = [item for item in Gadgets if isinstance(item, str)]
numbers = [item for item in Gadgets if isinstance(item, (int, float))]
print("Strings:", strings)
print("Numbers:", numbers)

ascend = sorted(strings)
descend = sorted(strings, reverse=True)
print("Ascending:", ascend)
print("Descending:", descend)

sort_str = sorted(strings)
print(sort_str)

sort_int_asc = sorted(numbers)
print("Ascending by length: ", sort_int_asc)
sort_int_desc = sorted(numbers, reverse=True)
print("Descending by length: ", sort_int_desc)























    
