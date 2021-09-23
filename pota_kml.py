# This is a simple Python script to convert the POTA CSV to a KML file
# Save the text of this script to your machine as pota_kml.py
# Python needs to be installed
# I would suggest pip also be installed and added to the path
# use pip to install simplekml and pandas
# run script with py pota_kml.py
# you can edit the last line to change the output file location
# example: kml.save("C:\\path\\to\\pota.kml")

import simplekml
import pandas
df=pandas.read_csv("https://pota.us/all_parks_ext.csv")

kml=simplekml.Kml()

for ref,nom,lat,long in zip(df["reference"],df["name"],df["latitude"],df["longitude"]):
	kml.newpoint(name=[(str(ref) + " " + str(nom))],coords=[(lat,long)])
kml.save("pota.kml")
