from utils.star_parser import star3_to_topaz

parser = star3_to_topaz("P6_J232_bin2.star", "fitting_correct_g2", [3,4], [3,4,6,7], 2.74, name_index = 2, optional_attributes = [-6,], header = "x_coord\ty_coord\tscore\n")

parser.parse()
