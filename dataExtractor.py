# Data extractor v1.00
# Created by Alexander Roed Thorup - alexander.roedthroup.dk
# This program is used to extract data from the CSV files taken from
# http://www.theplantlist.org/.

# -*- coding: cp865 -*-
import os;
import codecs;
import re as regex;

class plantObject():
	plantObjectCount = 0;

	def __init__(self, category, family, genus, species):
		self.id = plantObject.plantObjectCount;
		self.category = category;
		self.family = family;
		self.genus = genus;
		self.species = species;
		plantObject.plantObjectCount += 1

	def displayCount(self):
		print "plantObject declared: " % (plantObject.plantObjectCount);

	def __str__(self):
		return "id: %s, category: %s, family: %s, genus: %s, species: %s" %(self.id, self.category, self.family, self.genus, self.species);

# Declaring arrays before using
# The order of the arrays is the same as the order of execution.
plantList = [];

plantObjectCheck = '(.*),(.),(.*),(.*),(.*),(.*),"(.*)",(.*),"(.*)","(.*)",(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*),"(.*)"';

path_0 = "floweringplants/";
for filename in os.listdir(path_0):
	print filename
	openFile = codecs.open(path_0 + filename, "r", "utf8");
	for line in openFile.xreadlines():
		match = regex.match(plantObjectCheck, line);
		if match:
			newPlantObject = plantObject("Flowering plants", match.group(3), match.group(5), match.group(7));
			plantList.append(newPlantObject);
		else: print "plantObject no match %s" % line;
	openFile.close();

path_1 = "conifers/";
for filename in os.listdir(path_1):
	print filename
	openFile = codecs.open(path_1 + filename, "r", "utf8");
	for line in openFile.xreadlines():
		match = regex.match(plantObjectCheck, line);
		if match:
			newPlantObject = plantObject("Conifers", match.group(3), match.group(5), match.group(7));
			plantList.append(newPlantObject);
		else: print "plantObject no match %s" % line;
	openFile.close();

path_2 = "ferns/";
for filename in os.listdir(path_2):
	print filename
	openFile = codecs.open(path_2 + filename, "r", "utf8");
	for line in openFile.xreadlines():
		match = regex.match(plantObjectCheck, line);
		if match:
			newPlantObject = plantObject("Ferns", match.group(3), match.group(5), match.group(7));
			plantList.append(newPlantObject);
		else: print "plantObject no match %s" % line;
	openFile.close();

path_3 = "mosses/";
for filename in os.listdir(path_3):
	print filename
	openFile = codecs.open(path_3 + filename, "r", "utf8");
	for line in openFile.xreadlines():
		match = regex.match(plantObjectCheck, line);
		if match:
			newPlantObject = plantObject("Mosses", match.group(3), match.group(5), match.group(7));
			plantList.append(newPlantObject);
		else: print "plantObject no match %s" % line;
	openFile.close();


# Test of data file extraction
#print "Plants in list: %s" % len(plantList);
#print "Test extraction 1:"
#print plantList[0];
#print "Test extraction 2:"
#print plantList[100000];
#print "Test extraction 3:"
#print plantList[200000];
#print "Test extraction 4:"
#print plantList[300000];
#print "Test extraction 5:"
#print plantList[400000];
#print "Test extraction 6:"
#print plantList[500000];
#print "Test extraction 7:"
#print plantList[510000];
#print "Test extraction 8:"
#print plantList[520000];
#print "Test extraction 9:"
#print plantList[540000];
#print "Test extraction 10:"
#print plantList[560000];
#print "Test extraction 11:"
#print plantList[580000];
#print "Test extraction 12:"
#print plantList[59141];
#print "Test extraction 13:"
#print plantList[3000];
#print "Test extraction 14:"
#print plantList[4000];
#print "Test extraction 15:"
#print plantList[5000];
#print "Test extraction 16:"
#print plantList[6000];
#print "Test extraction 17:"
#print plantList[7000];
#print "Test extraction 18:"
#print plantList[8000];
#print "Test extraction 19:"
#print plantList[8200];