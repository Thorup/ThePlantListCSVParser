# Database Creator v1.00
# Created by Alexander Roed Thorup - alexander.roedthroup.dk

# File parts does not work

# -*- coding: cp865 -*-
import dataExtractor

plantList_floweringPlants = open("plantlist_csv_files/04_08_2016/output/spiioPlantList_floweringPlants.json", "w");

plantList_conifers = open("plantlist_csv_files/04_08_2016/output/spiioPlantList_conifers.json", "w");

plantList_ferns = open("plantlist_csv_files/04_08_2016/output/spiioPlantList_ferns.json", "w");

plantList_mosses = open("plantlist_csv_files/04_08_2016/output/spiioPlantList_mosses.json", "w");

plantList_floweringPlants.write("%s"
	% (
		"["
	)
);

plantList_conifers.write("%s"
	% (
		"["
	)
);

plantList_ferns.write("%s"
	% (
		"["
	)
);

plantList_mosses.write("%s"
	% (
		"["
	)
);


# The following for loop writes the values of plant json document
latestFloweringPlant = dataExtractor.plantObject("", "", "", "");
latestConifer = dataExtractor.plantObject("", "", "", "");
latestFern = dataExtractor.plantObject("", "", "", "");
latestMoss = dataExtractor.plantObject("", "", "", "");

for i in range(len(dataExtractor.plantList)):

	#######################################################
	# IF CATEGORY IS FLOWERING PLANTS
	if (dataExtractor.plantList[i].category == 'Flowering plants'):
		if(latestFloweringPlant.category == dataExtractor.plantList[i].category):

			plantList_floweringPlants.write('{ "category": "%s", "family": "%s", "genus": "%s", "species": "%s" },'
				% (
					latestFloweringPlant.category, latestFloweringPlant.family, latestFloweringPlant.genus, latestFloweringPlant.species
				)
			);

			latestFloweringPlant = dataExtractor.plantList[i];

		else:
			# THIS SHOULD ONLY HAPPEN WHEN 'latestFloweringPlant' IS NOT SET
			print ('First Flowering plant element: %s' % dataExtractor.plantList[i]);
			latestFloweringPlant = dataExtractor.plantList[i];

	#######################################################
	# IF CATEGORY IS CONIFERS
	elif (dataExtractor.plantList[i].category == 'Conifers'):
		if(latestConifer.category == dataExtractor.plantList[i].category):

			plantList_conifers.write('{ "category": "%s", "family": "%s", "genus": "%s", "species": "%s" },'
				% (
					latestConifer.category, latestConifer.family, latestConifer.genus, latestConifer.species
				)
			);

			latestConifer = dataExtractor.plantList[i];

		else:
			# THIS SHOULD ONLY HAPPEN WHEN 'latestConifer' IS NOT SET
			print ('First Conifer element: %s' % dataExtractor.plantList[i]);
			latestConifer = dataExtractor.plantList[i];


	#######################################################
	# IF CATEGORY IS FERNS
	elif (dataExtractor.plantList[i].category == 'Ferns'):
		if(latestFern.category == dataExtractor.plantList[i].category):

			plantList_ferns.write('{ "category": "%s", "family": "%s", "genus": "%s", "species": "%s" },'
				% (
					latestFern.category, latestFern.family, latestFern.genus, latestFern.species
				)
			);

			latestFern = dataExtractor.plantList[i];

		else:
			# THIS SHOULD ONLY HAPPEN WHEN 'latestConifer' IS NOT SET
			print ('First Fern element: %s' % dataExtractor.plantList[i]);
			latestFern = dataExtractor.plantList[i];


	#######################################################
	# IF CATEGORY IS MOSSES
	elif (dataExtractor.plantList[i].category == 'Mosses'):
		if(latestMoss.category == dataExtractor.plantList[i].category):

			plantList_mosses.write('{ "category": "%s", "family": "%s", "genus": "%s", "species": "%s" },'
				% (
					latestMoss.category, latestMoss.family, latestMoss.genus, latestMoss.species
				)
			);

			latestMoss = dataExtractor.plantList[i];

		else:
			# THIS SHOULD ONLY HAPPEN WHEN 'latestConifer' IS NOT SET
			print ('First Moss element: %s' % dataExtractor.plantList[i]);
			latestMoss = dataExtractor.plantList[i];

	#######################################################
	# IF CATEGORY IS NOT SET FOR SOME REASON
	else:
		print ('Error on Category: %s' % dataExtractor.plantList[i]);




plantList_floweringPlants.write('{ "category": "%s", "family": "%s", "genus": "%s", "species": "%s" }'
	% (
		latestFloweringPlant.category, latestFloweringPlant.family, latestFloweringPlant.genus, latestFloweringPlant.species
	)
);

plantList_conifers.write('{ "category": "%s", "family": "%s", "genus": "%s", "species": "%s" }'
	% (
		latestFloweringPlant.category, latestFloweringPlant.family, latestFloweringPlant.genus, latestFloweringPlant.species
	)
);

plantList_ferns.write('{ "category": "%s", "family": "%s", "genus": "%s", "species": "%s" }'
	% (
		latestFloweringPlant.category, latestFloweringPlant.family, latestFloweringPlant.genus, latestFloweringPlant.species
	)
);

plantList_mosses.write('{ "category": "%s", "family": "%s", "genus": "%s", "species": "%s" }'
	% (
		latestFloweringPlant.category, latestFloweringPlant.family, latestFloweringPlant.genus, latestFloweringPlant.species
	)
);

plantList_floweringPlants.write("%s"
	% (
		"]"
	)
);

plantList_conifers.write("%s"
	% (
		"]"
	)
);

plantList_ferns.write("%s"
	% (
		"]"
	)
);

plantList_mosses.write("%s"
	% (
		"]"
	)
);

