import svgwrite
from svgwrite import cm, mm 
import os

from csv import DictReader


dwg = svgwrite.Drawing('test3.svg', size=(1000, 1000))
dwg.add(dwg.image(os.path.abspath("index.png")))
dwg.defs.add(dwg.style("""
.bold {
    font-weight: bold;
}
.normal {
    font-weight: normal;
}
"""))


with open("texts.csv", "r") as input:
    reader = DictReader(input, delimiter=";")
    for item in reader:
        g = dwg.add(dwg.g())
        ellipse = g.add(dwg.ellipse(center=(int(item["x"]), int(item["y"])), r=('3cm', '2cm')))
        ellipse.fill('white', opacity=1)
        g.add(dwg.text(
            item["text"], insert=(int(item["x"]), int(item["y"])),
            fill="black",
            class_=item["style"]))

dwg.save()