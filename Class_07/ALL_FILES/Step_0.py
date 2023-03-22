
#####
# Step 0 - Practice tasks before we start.
#####

# For each filename in the list_of_file_names, replace the . with _ and append a new file extension of ".shp"
# each filename should look like: "file1_csv.shp", print the output filename.
list_of_file_names = ["file1.csv", "file2.csv", "file3.csv", "file4.csv", "file5.csv"]

for files in list_of_file_names:
    print(files.replace('.','_')+'.shp')


# How many files are in the list?
print(len(list_of_file_names))

# What is the first file name in the list_of_file_names?
print(list_of_file_names[0])

# Write the following data to a csv file called species1.csv (hint, just write it to a file):
data = "\nscientificName,	decimalLongitude,	decimalLatitude\n" \
       "Desmophyllum pertusum,	-88.37752,	29.06926\n" \
       "Desmophyllum dianthus,	-119.4718,	33.91861"


file_create = open('Step_0.csv', 'w')
file_create.write(data)
file_create.close()
file_read = open('Step_0.csv', 'r')
file_contents = file_read.read()
file_read.close()
print(file_contents)
print('\n'+r'File are read succesfully')


# Run through some examples from Coding Challenge 6.

