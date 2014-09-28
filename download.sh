#!/bin/bash

download_file() {
    if [ ! -f $1 ]
    then
	axel -a -n 4 "http://download.geonames.org/export/dump/$1"
    fi
}

download_file "allCountries.zip"
download_file "alternateNames.zip"
download_file "admin1CodesASCII.txt"
download_file "admin2Codes.txt"
#download_file "iso-languagecodes.txt"
download_file "featureCodes_bg.txt"
download_file "featureCodes_en.txt"
download_file "featureCodes_nb.txt"
download_file "featureCodes_nn.txt"
download_file "featureCodes_no.txt"
download_file "featureCodes_ru.txt"
download_file "featureCodes_sv.txt"
download_file "timeZones.txt"
download_file "countryInfo.txt"
download_file "userTags.zip"
download_file "hierarchy.zip"
download_file "shapes_simplified_low.json.zip"
for f in *.zip
do
    d=${f%.zip}
    unzip -d $d $f
done
