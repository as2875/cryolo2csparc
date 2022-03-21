import argparse
import glob
import os

parser = argparse.ArgumentParser()
parser.add_argument("--cryolo", metavar="PATTERN",
                    help="STAR files written by crYOLO")
parser.add_argument("--output",
                    help="Location of output STAR file")
parser.add_argument("--doseweighted", action="store_true", default=False,
                    help="Whether to append '_doseweighted' to filenames")
args = parser.parse_args()

complete_file = ["\n",
                 "data_\n",
                 "\n",
                 "loop_\n",
                 "_rlnMicrographName #1\n",
                 "_rlnCoordinateX #2\n",
                 "_rlnCoordinateY #3\n"]

for star_file in glob.glob(args.cryolo):
    with open(star_file) as f:
        star_contents = f.readlines()
    for line in star_contents:
        if line.startswith("_"):
            continue
        fields = line.split()
        if len(fields) == 2:
            if args.doseweighted:
                filename = os.path.splitext(os.path.split(star_file)[1])[0] + "_doseweighted.mrc"
            else:
                filename = os.path.splitext(os.path.split(star_file)[1])[0] + ".mrc"

            new_line = filename + "\t" + line
            complete_file = complete_file + [new_line]

with open(args.output, "w") as f:
    f.writelines(complete_file)
