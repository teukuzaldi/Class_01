import arcpy, os
arcpy.env.overwriteOutput = True


#Edit this line below___________________________________________________
arcpy.env.workspace = r"D:\NRS528_Python\NRS528\Class_10\CC_10\Class_10"
#Edit this line above___________________________________________________


theworkspace = f"{arcpy.env.workspace}"+"\Landsat_data_lfs"
if not os.path.exists(os.path.join(arcpy.env.workspace, "B_NDVI_Results")):
    os.mkdir(os.path.join(arcpy.env.workspace, "B_NDVI_Results"))
    print("Created folder: "+os.path.join(arcpy.env.workspace, "B_NDVI_Results")+"\n")
else:
    print("Folder already exists: "+os.path.join(arcpy.env.workspace, "B_NDVI_Results") +"\n")

result_folder = os.path.join(arcpy.env.workspace, "B_NDVI_Results")

for dirpath, dirnames, filenames in os.walk(theworkspace):
    for dirname in dirnames:
        output_folder = os.path.join(result_folder, dirname)
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
            print("Created folder: "+output_folder)

        b4_vis_red = ''
        b5_nir = ''

        for filename in os.listdir(os.path.join(dirpath, dirname)):
            if filename.endswith('B4.tif'):
                b4_vis_red = os.path.join(dirpath, dirname, filename)
            elif filename.endswith('B5.tif'):
                b5_nir = os.path.join(dirpath, dirname, filename)

        if b4_vis_red and b5_nir:
            expression = "(Float('{0}') - Float('{1}')) / (Float('{0}') + Float('{1}'))".format(b5_nir, b4_vis_red)

            # run raster calculator
            output_raster = os.path.join(output_folder, dirname + ".tif")
            arcpy.gp.RasterCalculator_sa(expression, output_raster)
            print("Calculated NDVI for "+dirname+"\n")

os.startfile(result_folder)

print("Created by: Teuku Zaldiansyah"+"\n"+
      "Script Created: 04/14/2023")
