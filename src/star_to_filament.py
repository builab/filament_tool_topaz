import sys
sys.path.append(".")
from utils.parsers import star_to_helix

star_to_helix("P6_J125_bin2.star", 2.74, "test_output_folder", -6)
