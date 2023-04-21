import arcpy, os
arcpy.env.overwriteOutput = True
# Set workspace environment - USER INPUT BELOW
arcpy.env.workspace = r"C:\Data\Students_2023\Zaldi\Class_09\FHWP12"
# Set workspace environment - USER INPUT ABOVE

input_directory = arcpy.env.workspace
if not os.path.exists(os.path.join(input_directory, "B_Results")):
    os.mkdir(os.path.join(input_directory, "B_Results"))
    print("Creating: "+os.path.join(input_directory, "B_Results")+"\n")
else:
    print(os.path.join(input_directory, "B_Results") +" is exist"+"\n")

result = os.path.join(input_directory, "B_Results")
fc = arcpy.ListFeatureClasses()[0]
fields = ["Site", "Species", "photo"]

species_list = []
photo_count = 0
no_photo_count = 0

arcpy.AddField_management(fc, "HasPhoto", "TEXT")


with arcpy.da.UpdateCursor(fc, fields + ["HasPhoto"]) as cursor:
    for row in cursor:
        site_name = row[0]
        species_name = row[1]
        photo = row[2]
        if photo and "y" in photo.lower():
            photo_count += 1
            if species_name not in species_list:
                species_list.append(species_name)
            row[3] = "Yes"
        else:
            no_photo_count += 1
            row[3] = "No"
        cursor.updateRow(row)

# Print results
print(f"Point has Photo: {photo_count}")
print(f"Point w/o Photo: {no_photo_count}")
print(f"Total Uniqes Species: {len(species_list)}"+"\n")
print(r"Uniques Species Code List : "+ str(species_list)+"\n")

# Write species_list to a text file and open it
species_list_file = os.path.join(result, "species_list.txt")
with open(species_list_file, "w") as file:
    file.write("\n".join(species_list))


photo_shp = arcpy.management.SelectLayerByAttribute(fc, "NEW_SELECTION", "HasPhoto = 'Yes'")
arcpy.management.CopyFeatures(photo_shp, f"{result}\\photo.shp")

if arcpy.Exists(f"{result}\\photo.shp"):
    print(f"{result}\\photo.shp" + " is created successfully!")

no_photo_shp = arcpy.management.SelectLayerByAttribute(fc, "NEW_SELECTION", "HasPhoto = 'No'")
arcpy.management.CopyFeatures(no_photo_shp, f"{result}\\no_photo.shp")

if arcpy.Exists(f"{result}\\no_photo.shp"):
    print(f"{result}\\no_photo.shp" + " is created successfully!")

os.startfile(os.path.join(input_directory, "B_Results"))
os.startfile(species_list_file)