import unicodecsv
import re

fw = open("worldcup-python-output2.csv","w")
writer = unicodecsv.writer(fw, encoding="utf8", lineterminator="\n")

titles = {}
f = open("worldcup.txt","r")
f.readline()

line = f.readline().strip()
while line!="|}":
    line = f.readline().strip()
    country = line.split("{{fb|")[1].split("}}")[0]
    countrytitles = titles.get(country, {})
    for i in range(4):
        position = re.findall("\|\d{4}]]", f.readline().strip())
        for position in position:
            countrytitles[position[1:-2]] = i+1
    titles[country] = countrytitles
    f.readline()
    line = f.readline().strip()

f.close()

writer.writerow([i for i in range(1930,2015,4)])
for k in titles:
    m = [k]
    for i in range(1930, 2015, 4):
        m.append('-' if str(i) not in titles[k].keys() else titles[k][str(i)])
    writer.writerow(m)

fw.close()
