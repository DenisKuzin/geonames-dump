# -*- coding: utf-8 -*-

from collections import namedtuple

ISOLanguage = namedtuple('ISOLanguage', [
    'iso_639_3',
    'iso_639_2',
    'iso_639_1',
    'language_name'
])

FeatureClass = namedtuple('FeatureClass', [
    'name',
    'description'
])

FeatureCode = namedtuple('FeatureCode', [
    'name',
    'short_description',
    'long_description'
])

CountryInfo = namedtuple('CountryInfo', [
    'ISO',
    'ISO3',
    'ISO_numeric',
    'fips',
    'country',
    'capital',
    'area', # Area(in sq km)
    'population',
    'continent',
    'tld',
    'currency_code',
    'currency_name',
    'phone',
    'postal_code_format',
    'postal_code_regex',
    'Languages',
    'geonameid',
    'neighbours',
    'equivalent_fips_code'
])

AdminCode = namedtuple('AdminCode', [
    'code', 
    'name', 
    'ascii_name',
    'geoname_id'
])

TimeZone = namedtuple('TimeZone', [
    'country_code',
    'time_zone_id',
    'GMT_offset',
    'DST_offset',
    'raw_offset'
])

AlternateName = namedtuple('AlternateName', [
    'alternate_name_id',
    'geoname_id',
    'iso_language',
    'alternate_name',
    'is_preferred_name',
    'is_short_name',
    'is_colloquial',
    'is_historic'
])

Geoname = namedtuple('Geoname', [
    'geoname_id',
    'name',
    'asciiname',
    'alternate_names',
    'latitude',
    'longitude',
    'feature_class',
    'feature_code',
    'country_code',
    'cc2',
    'admin1_code',
    'admin2_code',
    'admin3_code',
    'admin4_code',
    'population',
    'elevation',
    'dem',
    'timezone',
    'modification_date'
])
