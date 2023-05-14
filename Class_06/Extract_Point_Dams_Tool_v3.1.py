# Title: Documenting and Creating point layer in Boundaries for Rhode Island Town
# Created by: Teuku Zaldiansyah | 02/14/2023 | Updated: 05/13/2023
#
# What does the tool do?
# In short, It automatically counts and creates a point layer inside an area or boundaries,
# organizing the layer in each folder, then it documented the result in a spreadsheet.
#
# The step executed below are:
# - Clip the points into boundaries (RI Town)
# - Project all of them into Rhode Island State Plane (Meter)
# - Count each point inside the respective boundaries
# - The resulting layer contains points in each boundary
# - Automatically documented the point into a .csv file
# - Organize file automatically for each town labeled with their respective town name.
# -------------------------------------------------------------------------------------------------------------------

import arcpy
import os
import csv

arcpy.env.overwriteOutput = True

#CHANGE THIS SECTION ONLY------------------------
Workspace = r"D:\NRS528_Python\NRS528\Class_06_01_MidTerm_Coding_Challenge\Class_06_v2\Midterm_Dams_Tools_v3.2\Point_Layer"
#------------------------------------------------

input_directory = Workspace
Town_table = f"{Workspace}\A_Input\Lab1_Town_Table\Lab1_Town_Table.csv"
Town_shp = f"{Workspace}"+r"\A_Input\Lab_1_Data\towns.shp"
Dams_Input = f"{Workspace}"+r"\A_Input\Dams_Input\Dams.shp"
result_sheet_csv = f"{Workspace}" + r"\result_sheet.csv"

if not os.path.exists(os.path.join(input_directory, "B_Process_Data")):
    os.mkdir(os.path.join(input_directory, "B_Process_Data"))
if not os.path.exists(os.path.join(input_directory, "C_Results")):
    os.mkdir(os.path.join(input_directory, "C_Results"))

result_sheet_csv = f"{Workspace}" + r"\result_sheet.csv"

process_data = f"{Workspace}\B_Process_Data"
result = f"{Workspace}\C_Results"

Towns = []
Counties = []
dam_counts = {}

with open(Town_table) as boundaries_csv:
    next(boundaries_csv)
    for row in csv.reader(boundaries_csv):
        town_name = row[1]
        if town_name not in Towns:
            Towns.append(town_name)

            outputDirectory = f"{process_data}" + r"\Temp_files_" + str(town_name)
            if not os.path.exists(outputDirectory):
                os.mkdir(outputDirectory)
            ResultDirectory = f"{result}" + r"\Final_result_" + str(town_name)
            if not os.path.exists(ResultDirectory):
                os.mkdir(ResultDirectory)

            print(r". . . Processing boundaries of "+town_name)

            in_features = Town_shp
            out_feature_class_select = os.path.join(outputDirectory, f"{town_name}"+"_boundary"+".shp")
            where_clause = f'"NAME" = \'{town_name}\''

            # Run Select
            arcpy.analysis.Select(in_features, out_feature_class_select, where_clause)

#Clip_Features-----------------------------------------------------------------------

            in_features = Dams_Input
            clip_features = out_feature_class_select
            out_feature_class_clip = os.path.join(outputDirectory, f"{town_name}"+"_dams_clipped"+".shp")

            # Run Clip
            arcpy.analysis.Clip(in_features, clip_features, out_feature_class_clip)

            print('. . . clipping dams to '+f"{town_name}")
            if arcpy.Exists(out_feature_class_clip):
                print(f"{town_name}"+"_dams_clipped"+".shp"+ " is created successfully!")

#Project(RI-Meter)---------------------------------------------------------

            input_features = out_feature_class_clip
            output_feature_class_projected = os.path.join(ResultDirectory, f"{town_name}"+"_dams_Meter"+".shp")
            out_coordinate_system = arcpy.SpatialReference(32130)
            arcpy.Project_management(input_features, output_feature_class_projected, out_coordinate_system)

            print('. . . projecting to meter')
            if arcpy.Exists(output_feature_class_projected):
                print(f"{town_name}"+"_dams_Meter_output.shp"+" is created successfully!")

#Get Count------------------------------------------------------------------

            Row_Count = arcpy.management.GetCount(in_rows=output_feature_class_projected)[0]
            dam_counts[town_name] = Row_Count

            print(r"Total dams in " + f"{town_name}" + " is: " + Row_Count)

print("\n"+r'Finalizing result into csv files'+
          "\n"+ "95% Completed"+"\n")

#Creating CSV------------------------------------------------------------------

with open(result_sheet_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'total_points'])
    for town_name, count in dam_counts.items():
        writer.writerow([town_name, count])

print(f"Opening CSV file from this path: {result_sheet_csv}")
print(f"Opening result folder from this path path: {Workspace}")

Result_Report_csv = f"{result_sheet_csv}"
path = os.path.abspath(Result_Report_csv)
os.startfile(path)
os.startfile(Workspace)

#Deleting Temp files_____________________________________________________
arcpy.Delete_management(process_data)
if not os.path.exists(process_data):
    print("\n"+r"Temporary files -B_Process_Data-" + " is deleted successfully!" +
          "\n"+ "100% Completed")
#------------------------------------------------------------------------
