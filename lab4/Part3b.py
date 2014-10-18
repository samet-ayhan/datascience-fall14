import unicodecsv
import re

fw = open("worldcup-python-output1.csv","w")
writer = unicodecsv.writer(fw, encoding="utf8", lineterminator="\n")
writer.writerow(("Team","Year","Position"))

f = open("worldcup.txt","r")
f.readline()

line = f.readline().strip()
while line!="|}":
    line = f.readline().strip()
    country = line.split("{{fb|")[1].split("}}")[0]
    for i in range(4):
        position = re.findall("\|\d{4}]]", f.readline().strip())
        for position in position:
            writer.writerow((country, position[1:-2], i+1))
    f.readline()
    line = f.readline().strip()
fw.close()
f.close()
