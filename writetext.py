import svgwrite
from csv import DictReader
import os
import argparse

parser = argparse.ArgumentParser(description='Add text to images')
parser.add_argument('image', type=str,
                    help='image filename')
parser.add_argument('-t', dest='csv_input', action='store', required=True,
                    help='name of the text csv file')
parser.add_argument('-o', dest='output', action='store', required=True,
                    help='name of the output file')

args = parser.parse_args()


drawing = svgwrite.Drawing(args.output, size=(1000, 1000))
drawing.add(drawing.image(os.path.abspath(args.image)))
drawing.defs.add(drawing.style("""
.bold {
    font-weight: bold;
}
.normal {
    font-weight: normal;
}
"""))


with open(args.csv_input, "r") as input:
    reader = DictReader(input, delimiter=";")
    for item in reader:
        g = drawing.add(drawing.g())
        ellipse = g.add(drawing.ellipse(center=(int(item["x"]), int(item["y"])), r=('3cm', '2cm')))
        ellipse.fill('white', opacity=1)
        g.add(drawing.text(
            item["text"], insert=(int(item["x"]), int(item["y"])),
            fill="black",
            class_=item["style"]))

drawing.save()