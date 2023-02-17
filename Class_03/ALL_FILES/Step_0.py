
#####
# Step 0 - Practice tasks before we start.
#####

# Express these items as a list using list append (i.e. .append) and print it:

item1 = "data1.txt"
item2 = "data2.txt"
item3 = "data3.txt"

list=[item1, item2, item3]

all_item = [] #create empty list first

all_item.append(item1) #adding the all of item 1 by 1 using .append
all_item.append(item2)
all_item.append(item3)

print(all_item)

# Print out how many files are in the list? Hint, we can use len(NAME OF YOUR LIST)
print(len(all_item)) # use len to count the total item that inputted

# Take this list of files (file_list), and using a for loop, go through each file name and add
# a new file extension (.csv) and print new_extension_file_list.

# new_extension_all_item= []
#
# for item in all_item:
#     # data1.txt.csv
#     new_item = item + ".csv"
#     new_extension_all_item.append(new_item)
#
# print(new_extension_all_item)

new_extension_all_item_split= []

for item in all_item:
    # data1.txt.csv
    new_item = item.split('.')[0] + '.csv'
    # print(new_item)
    new_extension_all_item_split.append(new_item)

print(new_extension_all_item_split)