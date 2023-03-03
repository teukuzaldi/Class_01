import arcpy
import csv
arcpy.env.overwriteOutput = True

#Input the "Workspace" path below
Declare_workspace = r"D:\URI MESM\NRS528\Class_05\Coding_Challenge_5\Raw_Data\Workspace"
#DO NOT alter or delete the path of (\Species_data\Swordfish_n_salmon.csv)
Declare_csv = f"{Declare_workspace}\Species_data\Swordfish_n_salmon.csv"

# 1. Convert Swordfish_n_salmon.csv to a shapefile.
arcpy.env.workspace = Declare_workspace
speciesList = []
with open (Declare_csv) as species_csv:
    next(species_csv)
    for row in csv.reader(species_csv):
        species = row[0]
        if species not in speciesList:
            speciesList.append(species)

#Create shapefile for the table
in_Table = Declare_csv
x_coords = "decimallongitude" #Longitude is the X axis
y_coords = "decimallatitude" #Latitude is the Y axis,
z_coords = ""
out_Layer = "Salmonandswordfish"
saved_Layer = r"Salmon_n_swordfish_Output.shp"

# Set the spatial reference
spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984

lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)

print(arcpy.GetCount_management(out_Layer))
arcpy.CopyFeatures_management(lyr, saved_Layer)
#
if arcpy.Exists(saved_Layer):
    print("Csv files for Juvenile_Salmon are created file successfully!")
#Done for converting the table into shapefile

# Set local variables
in_table = saved_Layer
for species in speciesList:
    point_out_feature_class = f"{species}_point.shp"
    where_clause = f'"name" = \'{species}\''
    arcpy.Select_analysis(in_table, point_out_feature_class, where_clause)
    if arcpy.Exists(point_out_feature_class):
        print(f"{point_out_feature_class} point data is created successfully!")

# 2. Extact the Extent, i.e. XMin, XMax, YMin, YMax of the generated respective species shapefile.
        # Get extent of the shapefile
        desc = arcpy.Describe(point_out_feature_class)
        print(f"\nExtent of {point_out_feature_class}:"
              f"\nYMin: {desc.extent.YMin}, "
              f"\nYMax: {desc.extent.YMax}, "
              f"\nXMin: {desc.extent.XMin}, "
              f"\n"f"XMax: {desc.extent.XMax}"
              f"\nSpatial Reference: {desc.spatialReference.name}, "
              f"\nType: {desc.spatialReference.type}\n")

# 3. Generate a fishnet,
        arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

        outFeatureClassNet = f"{species}_fishnet.shp"  # Name of output fishnet

        # Set the origin of the fishnet
        originCoordinate = str(desc.extent.XMin) + ' ' + str(desc.extent.YMin)  # Left bottom of our point data
        yAxisCoordinate = str(desc.extent.XMin) + ' ' + str(desc.extent.YMin + 10)  # This sets the orientation on the y-axis, so we head north
        cellSizeWidth = '1'
        cellSizeHeight = '1'
        numRows = ""  # Leave blank, as we have set cellSize
        numColumns = ""  # Leave blank, as we have set cellSize
        oppositeCorner = str(desc.extent.XMax) + ' ' + str(desc.extent.YMax)  # i.e. max x and max y coordinate
        labels = "NO_LABELS"
        templateExtent = "#"  # No need to use, as we have set yAxisCoordinate and oppositeCorner
        geometryType = "POLYGON"  # Create a polygon, could be POLYLINE

        arcpy.CreateFishnet_management(outFeatureClassNet, originCoordinate, yAxisCoordinate,
                                       cellSizeWidth, cellSizeHeight, numRows, numColumns,
                                       oppositeCorner, labels, templateExtent, geometryType)
        if arcpy.Exists(outFeatureClassNet):
            print(f"{outFeatureClassNet} is created successfully!")

# 4. Undertake a Spatial Join to join the fishnet to the observed points.
        target_features = f"{species}_fishnet.shp"
        join_features = saved_Layer
        out_feature_class = f"{species}_output.shp"
        join_operation = "JOIN_ONE_TO_ONE"
        join_type = "KEEP_ALL"
        field_mapping = ""
        match_option = "INTERSECT"
        search_radius = ""
        distance_field_name = ""

        arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                                   join_operation, join_type, field_mapping, match_option,
                                   search_radius, distance_field_name)

        if arcpy.Exists(out_feature_class):
            print(f"{out_feature_class} the final output is created successfully!")

        # 5. Check that the heatmap is created and delete the intermediate files (e.g. species shapefile and fishnet). Hint:
        # arcpy.Delete_management()..

        if arcpy.Delete_management(outFeatureClassNet):#deleting the fishnet
            print(f"\n{outFeatureClassNet} was successfully deleted!")
        if arcpy.Delete_management(point_out_feature_class):#deleting the point data
            print(f"{point_out_feature_class} was successfully deleted!\n")

if arcpy.Delete_management(saved_Layer):  # deleting the table shapefile data
    print(f"{saved_Layer} was successfully deleted!")

# 6. Visualize in ArcGIS Pro

# Hint: To stop your script failing due to unable to overwriteOutput error, use the overwriteOutput environment setting:
# If you get "already exists error" even when True, ensure file is not open in
# ArcGIS Pro or an other program such as Excel.