# Database Creator v1.00
# Created by Alexander Roed Thorup - alexander.roedthroup.dk

# File parts does not work

# -*- coding: cp865 -*-
import dataExtractor

plantListFile = open("04_08_2016_plantlist_csv_files/output/spiioPlantList.json", "w");

#plantListFile.write("%s\n"
#	% (
#		"{"
#	)
#);

# The following for loop writes the values of plant json document
for i in range(len(dataExtractor.plantList)):
	if (dataExtractor.plantList[i] != dataExtractor.plantList[len(dataExtractor.plantList)-1]):
		plantListFile.write('{ "category": "%s", "family": "%s", "genus": "%s", "species": "%s" },\n'
			% (
				dataExtractor.plantList[i].category, dataExtractor.plantList[i].family, dataExtractor.plantList[i].genus, dataExtractor.plantList[i].species
			)
		);
	else:
		plantListFile.write('{ "category": "%s", "family": "%s", "genus": "%s", "species": "%s" }\n'
			% (
				dataExtractor.plantList[i].category, dataExtractor.plantList[i].family, dataExtractor.plantList[i].genus, dataExtractor.plantList[i].species
			)
		);

#plantListFile.write("%s\n"
#	% (
#		"}"
#	)
#);