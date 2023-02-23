# Import system modules
import arcpy
from arcpy import env

# To overwrite the existing project
arcpy.env.overwriteOutput = True

# Print the passed-down current workspace environment setting
arcpy.AddMessage("The passed-down current workspace is: %s" % arcpy.env.workspace)
arcpy.AddMessage("The passed-down scratch workspace is: %s" % arcpy.env.scratchWorkspace)

# Set a new workspace, overriding the passed-down workspace
arcpy.env.workspace = r"D:\URI MESM\NRS528\Class_04\Workspace"
arcpy.env.scratchWorkspace = r"D:\URI MESM\NRS528\Class_04\Scratch"
arcpy.AddMessage("The new current workspace is: %s" % arcpy.env.workspace)
arcpy.AddMessage("The new scratch workspace is: %s" % arcpy.env.scratchWorkspace)
# Setting up the default workspace and scratch directory

# ____________________________________________________________________________________________

# The select tools below, are set to extract the South Kingstown Boundaries

# Set local variables
in_features = r"D:\URI MESM\NRS528\Class_04\Class_04\Data\muni97d\muni97d.shp" #Change the data references
out_feature_class = r"D:\URI MESM\NRS528\Class_04\Class_04\Output\South_Kingstown.shp" #change the output
where_clause = '"NAME" = \'SOUTH KINGSTOWN\'' #(Optional) if we want extract another boudaries

# Execute Select
arcpy.Select_analysis(in_features, out_feature_class, where_clause) #Should not be alter