
#####
# Step 1 - os - operating system
#####

# The os package gives you functions that allow you to interface with the operating system:
import os

# Part a - Executing a Shell/Command Prompt command
os.system("dir c:") #DIR is a Windows command to list contents of current directory

# Other notable commands - mkdir = make directory, rmdir = delete directory

# # Task - Use os.system to make a directory in your current directory, check if it is created
# # delete it and check again.
#
os.system('mkdir test')
os.system('dir')
os.system('rmdir test')
os.system('dir')


# Part b - Other interesting functions you can use within Python
# path = "test_dir"

# Create a directory
# os.mkdir(path)

#
# Return a list of the entries in the directory given by path.
# list = os.listdir(path) #ngasih tau apa isi didalam folder (path) itu
# print(list)
#
# Rename the file or directory src to dst.
# os.rename("test_dir", "test_dir2")
#
# Remove directories recursively.
# os.removedirs(path + "2")
#
# # # Remove (delete) the file path.
# os.remove(path)
#
# # # Remove (delete) the directory path.
# os.rmdir(path)
#
# # Bonus Task 2 - Use os to make a directory in your root directory, add a subdirectory inside it, check if it is created,
# # delete the subdirectory and the main directory. Check if the main directory exists, print "name dir EXISTS" or "name dir NOT EXISTS"

# import os
#
# os.mkdir('D:\main_directory')
# os.mkdir('D:\main_directory\sub_directory')
#
# list = os.listdir('D:\main_directory') #ngasih tau apa isi didalam folder (path) itu
# print(list)
#
# if'sub_directory' in list:
#     print('name sub_directory EXISTS')
# else:
#     print('name sub_directory MISSING')
#
# # os.removedirs('D:\main_directory\sub_directory')
# # os.removedirs('D:\main_directory')
# #
# if'main_directory' in list:
#     print('name main_directory EXISTS')
# else:
#     print('name main_directory MISSING')
#
# list = os.listdir('c:') #ngasih tau apa isi didalam folder (path) itu
# print(list)