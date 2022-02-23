from utils.star_parser import star3_to_topaz

pixelSize = 2.74 # Important
boxSize = 256 # Not so important

# Important to check column 3,4,6,7 of the star file 
# Column 3 = CoordinateX
# Column 4 = CoordinateY
# Column 6 = rlnOriginXAngst
# Column 7 = rlnOriginYAngst

parser = star3_to_topaz("group2_P13_J38_bin2.star", "box_g2", [3,4], [3,4,6,7], pixelSize, name_index = 2, optional_attributes = [boxSize,boxSize,-6,], header = "x_coord\ty_coord\tbox_x\tbox_y\tscore\n")

parser.parse()

