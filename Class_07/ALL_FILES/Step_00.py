
#####
# Step 1 - Searching directories for files and list them
#####

# Handling files is a critical part of any GIS (and analysis) workflow. This is particularly true if you are
# working with large amounts of files as we often do. In this step, we cover several ways of searching and
# listing files. We will use a mix of different methods and packages to do this. There are no right or
# wrong ways, providing you get the data you require.

# Part 1 - List files in the Step_1 directory using glob.glob: https://docs.python.org/2/library/glob.html

import glob
import os

# # List all Python files in current directory
# print(glob.glob("*.py"))
# # # Change to parent of current directory (dangerous as you might struggle to change it back later...)
# os.chdir("../") #../ go back one level directory
# print(glob.glob("*")) # no pattern match, lists all folders and files
# # If you changed directory, you may need to change it back:
# #
# #
# # Part 2 - List files using os (more painful)
# all = os.listdir(os.curdir)# files and directories
# print(all)
# files = list(filter(os.path.isfile, os.listdir(os.curdir)))  # files only, might not find anything
# print(files)
#
# for file in os.listdir(os.curdir):
#     if file.endswith(".txt"): #not found anything because there is no csv file from the prev directory
#         print(file)
#
# # Part 3 - List files using arcpy, note: all will return None
# import arcpy
#
# # ListFiles ({wild_card}) https://pro.arcgis.com/en/pro-app/arcpy/functions/listfiles.htm
# print(arcpy.ListFiles("*"))
# #
# # ListDatasets ({wild_card}, {feature_type}) https://pro.arcgis.com/en/pro-app/arcpy/functions/listdatasets.htm
# print(arcpy.ListDatasets("*",  "Feature"))
# # ListFeatureClasses ({wild_card}, {feature_type}, {feature_dataset}) https://pro.arcgis.com/en/pro-app/arcpy/functions/listfeatureclasses.htm
# print(arcpy.arcpy.ListFeatureClasses("*"))
#
# # ListRasters ({wild_card}, {raster_type})  https://pro.arcgis.com/en/pro-app/arcpy/functions/listrasters.htm
# print(arcpy.ListRasters("*", "TIF"))
#
#
# Tasks
# 1 - Using the supplied data in Step_1.zip (extract to a folder named Step_1), do the following:
# Hint, you should change your directory to Step_1
import arcpy
os.chdir(r"D:\URI MESM\NRS528\Class_07\ALL_FILES\Step_1")
arcpy.env.workspace = r"D:\URI MESM\NRS528\Class_07\ALL_FILES\Step_1"

# a - List and count all shapefiles, how many are there?
print('\n' + r'A.Shapefile Section')
print(arcpy.arcpy.ListFeatureClasses("*"))
print('.shp file count: ' + str(len(arcpy.arcpy.ListFeatureClasses("*"))) + '\n')
# for file_shp in os.listdir(os.curdir):
#     if file_shp.endswith(".shp"): #not found anything because there is no csv file from the prev directory
#         print(file_shp)
# print('.shp file Count: ' + str(len(file_shp)) + '\n')

# b - List and count all csv, how many are there?
print('\n'+r'B.CSV section')
for file in os.listdir(os.curdir):
    if file.endswith(".csv"): #not found anything because there is no csv file from the prev directory
        print(file)
print('.CSV file Count: ' + str(len(file)) + '\n')

# c - List and count all folders, how many are there?
print('\n'+r'C.Folders')
all = os.listdir(os.curdir)# files and directories
print(all)
print('Folders count : ' + str(len(all)) + '\n')
files = list(filter(os.path.isfile, os.listdir(os.curdir)))  # files only, might not find anything
print(files)
print('Folders count : ' + str(len(files)) + '\n')

# # d - List and count all rasters in GRID format, how many are there?
print('\n'+r'D.GRID section')
print(arcpy.ListRasters("*", "TIF"))
print('.GRID file Count :' + str(len(arcpy.ListRasters("*", "GRID"))))

# # e - List and count all rasters in TIF format, how many are there?
#
print('\n'+r'E.TIF section')
print(arcpy.ListRasters("*", "TIF"))
print('.TIF file Count :' + str(len(arcpy.ListRasters("*", "TIF"))))
#
# # f - List and count all folders beginning with the letter/character S_, how many are there?
print(arcpy.ListFiles("*"))
