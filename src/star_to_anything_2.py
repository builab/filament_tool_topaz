from utils.star_parser import star3_to_topaz

parser = star3_to_topaz("P6_J125_bin2.star", "fitting_correct", [3,4], [3,4,6,7], 2.74, name_index = 2, optional_attributes = [256,256,-6,], header = "x_coord\ty_coord\tbox_x\tbox_y\tscore\n")

parser.parse()
