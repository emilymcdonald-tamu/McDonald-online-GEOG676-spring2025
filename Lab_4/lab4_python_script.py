
# create a gdb and garage feature
import arcpy

# I used arcpy.management.CreateFileGDB instead of arcpy.CreateFileGDB_management to fix
# AttributeError: module 'arcpy' has no attribute 'CreateFileGBD_management

arcpy.env.workspace = r'C:\Users\anna2\OneDrive\Documents\GEOG676ClassMaterial\codes_env'
folder_path = r'C:\Users\anna2\OneDrive\Documents\GEOG676ClassMaterial'
gdb_name = 'Test.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.management.CreateFileGDB(folder_path, gdb_name)

csv_path = r'C:\Users\anna2\OneDrive\Documents\GEOG676ClassMaterial\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

# open campus gdb, copy building feature to our gdb
campus = r'C:\Users\anna2\OneDrive\Documents\GEOG676ClassMaterial\Campus.gdb'
buildings_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus, buildings)

# Re-Projection
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_reprojected', spatial_ref)

# buffer the garages
garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path +'\Garage_Points_buffered', 150)

# Intersect our buffer with the buildings
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Buildings_Intersection', 'ALL')

# I added the r to fix SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3:

arcpy.TableToTable_conversion(gdb_path + '\Garage_Buildings_Intersection.dbf', r'C:\Users\anna2\OneDrive\Documents\GEOG676ClassMaterial', 'nearbyBuildings.csv')
