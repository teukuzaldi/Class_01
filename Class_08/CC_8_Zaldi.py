import arcpy
import os
import csv
arcpy.env.overwriteOutput = True

def clipnselect_tools(Workspace, feature, Boundaries, Table_boundaries, Select_row, temp_folder_path, result_folder_path):

    arcpy.env.workspace = Workspace
    Temporary_Data = temp_folder_path
    print(f"Checking 1st path")
    if not os.path.exists(Temporary_Data):
        print(f"the {Temporary_Data} is not exist")
    else:
        print(f"the {Temporary_Data} is available")

    Output_data = result_folder_path
    print(f"Checking 2nd path")
    if not os.path.exists(Output_data):
        print(f"the {Output_data} is not exist")
    else:
        print(f"the {Output_data} is available")

    print("\n"+r"10% . . . Processing")

    Towns = []

    with open(Table_boundaries) as boundaries_csv:
        next(boundaries_csv)
        for row in csv.reader(boundaries_csv):
            town_name = row[Select_row]
            if town_name not in Towns:
                Towns.append(town_name)

                outputDirectory = f"{Temporary_Data}" + r"\Temp_files_" + str(town_name)
                if not os.path.exists(outputDirectory):
                    os.mkdir(outputDirectory)
                ResultDirectory = f"{Output_data}" + r"\Final_result_" + str(town_name)
                if not os.path.exists(ResultDirectory):
                    os.mkdir(ResultDirectory)

                print(r". . . Processing boundaries of " + town_name)

                in_features = Boundaries
                out_feature_class_select = os.path.join(outputDirectory, f"{town_name}" + "_boundary" + ".shp")
                where_clause = f'"NAME" = \'{town_name}\''

                # Run Select
                arcpy.analysis.Select(in_features, out_feature_class_select, where_clause)

                # Set local variables
                in_features = feature
                clip_features = out_feature_class_select
                out_feature_class_clip = os.path.join(ResultDirectory, f"{town_name}" + "_with_feature" + ".shp")

                # Run Clip
                arcpy.analysis.Clip(in_features, clip_features, out_feature_class_clip)

    print (r"100% complete")
    return Workspace, feature, Boundaries, Table_boundaries, Select_row


def make_folders(Workspace, User_Temp_Folder, User_Result_Folder):
    arcpy.env.workspace = Workspace
    if not os.path.exists(os.path.join(arcpy.env.workspace, User_Result_Folder)):
        print(f"Creating {User_Result_Folder} Directory")
        os.mkdir(os.path.join(arcpy.env.workspace, User_Result_Folder))
    else:
        print("The 1st folder is exist")
    if not os.path.exists(os.path.join(arcpy.env.workspace, User_Temp_Folder)):
        print(f"Creating {User_Temp_Folder} Directory"+"\n")
        os.mkdir(os.path.join(arcpy.env.workspace, User_Temp_Folder))
    else:
        print("The 2nd folder is exist"+"\n")
    result_path = os.path.join(arcpy.env.workspace, User_Result_Folder)
    temp_path = os.path.join(arcpy.env.workspace, User_Temp_Folder)
    return temp_path, result_path

#JUST CHANGE THIS LINE BELOW_____________________________________
Workspace = r"D:\URI MESM\NRS528\Class_08\ALL_FILES\Step_0"
#JUST CHANGE THIS LINE ABOVE_____________________________________

#(OPTIONAL) change the name of the foldar as you like______
User_Temp_Folder = r"Temp"
User_Result_Folder = r"Output"
#__________________________________________________________

#(OPTIONAL) 1 = for town | 2 = for county
Select_row = 2
#Feel free to change it___________________

feature = f"{Workspace}\RIDOTrds16\RIDOTrds16.shp"
Boundaries = f"{Workspace}\muni97d\muni97d.shp"
Table_boundaries = f"{Workspace}\Lab1_Town_Table\Lab1_Town_Table.csv"

temp_folder_path, result_folder_path = make_folders(Workspace, User_Temp_Folder, User_Result_Folder)
print(r"Your 1st path: "+temp_folder_path)
print(r"Your 2st path: "+result_folder_path+"\n")
clipnselect_tools(Workspace, feature, Boundaries, Table_boundaries, Select_row, temp_folder_path, result_folder_path)



