import csv
import json

towers = []
with open('dove.txt') as f:
    csv_reader = csv.DictReader(f, delimiter="\\")
    for row in csv_reader:
        towers.append({
            "DoveID": row["DoveID"],
            "Place": row["Place"],
            "Dedicn": row["Dedicn"],
            "Bells": row["Bells"],
            "Practise": row["PracN"],
            "ExtraInfo": row["ExtraInfo"],
            "lon": row["Long"],
            "lat": row["Lat"],
        })

with open("dove.json", "w") as f:
    f.write("var towers = %s;" % json.dumps(towers))
