# -*- coding: utf-8 -*-

import os
import sys
import codecs
from collections import namedtuple, defaultdict
import unittest

FeatureClass = namedtuple('FeatureClass', [
    'name',
    'description'
])

ISOLanguage = namedtuple('ISOLanguage', [
    'iso_639_3',
    'iso_639_2',
    'iso_639_1',
    'language_name'
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

class Dump(object):
    def __init__(self, downloaded_dir=None):
        self.downloaded_dir = downloaded_dir
        self.iso_languages_3 = {}
        self.iso_languages_2 = {}
        self.iso_languages_1 = {}
        self.feature_classes = {}
        self.feature_types_bg = {}
        self.feature_types_en = {}
        self.feature_types_nb = {}
        self.feature_types_nn = {}
        self.feature_types_no = {}
        self.feature_types_ru = {}
        self.feature_types_sv = {}
        self.countries = {}
        self.admin1_codes = {}
        self.admin2_codes = {}
        self.timezones = {}
        self.alternate_names = defaultdict(list)

    def fill(self):
        self.fill_iso_languages()
        self.fill_feature_classes()
        self.fill_feature_codes_bg()
        self.fill_feature_codes_en()
        self.fill_feature_codes_nb()
        self.fill_feature_codes_nn()
        self.fill_feature_codes_no()
        self.fill_feature_codes_ru()
        self.fill_feature_codes_sv()
        self.fill_country_info()
        self.fill_admin1_codes()
        self.fill_admin2_codes()
        self.fill_timezones()
        self.fill_alternate_names()


    def fill_iso_languages(self):
        filename = u'alternateNames/iso-languagecodes.txt'
        if self.downloaded_dir:
            filename = os.path.join(self.downloaded_dir, filename)
        with codecs.open(filename, encoding='utf8') as file:
            for line in file.readlines():
                line = line.split(u'\t')
                line = map(str.strip, line)
                iso_language = ISOLanguage(*line)
                self.iso_languages_3[iso_language.iso_639_3] = iso_language
                self.iso_languages_2[iso_language.iso_639_2] = iso_language
                self.iso_languages_1[iso_language.iso_639_1] = iso_language

    def fill_feature_classes(self):
        self.feature_classes = {
            'A': FeatureClass('A', 'country, state, region'),
            'H': FeatureClass('H', 'stream, lake'),
            'L': FeatureClass('L', 'parks, area'),
            'P': FeatureClass('P', 'city, village'),
            'R': FeatureClass('R', 'road, railroad'),
            'S': FeatureClass('S', 'spot, building, farm'),
            'T': FeatureClass('T', 'mountain, hill, rock'),
            'U': FeatureClass('U', 'undersea'),
            'V': FeatureClass('V', 'forest, heath'),
        }

    def fill_feature_codes_bg(self):
        filename = u'featureCodes_bg.txt'
        if self.downloaded_dir:
            filename = os.path.join(self.downloaded_dir, filename)
        with codecs.open(filename, encoding='utf8') as file:
            for line in file.readlines():
                line = line.split(u'\t')
                line = map(str.strip, line)
                feature_code = FeatureCode(*line)
                self.feature_types_bg[feature_code.name] = feature_code

    def fill_feature_codes_en(self):
        filename = u'featureCodes_en.txt'
        if self.downloaded_dir:
            filename = os.path.join(self.downloaded_dir, filename)
        with codecs.open(filename, encoding='utf8') as file:
            for line in file.readlines():
                line = line.split(u'\t')
                line = map(str.strip, line)
                feature_code = FeatureCode(*line)
                self.feature_types_en[feature_code.name] = feature_code

    def fill_feature_codes_nb(self):
        filename = u'featureCodes_nb.txt'
        if self.downloaded_dir:
            filename = os.path.join(self.downloaded_dir, filename)
        with codecs.open(filename, encoding='utf8') as file:
            for line in file.readlines():
                line = line.split(u'\t')
                line = map(str.strip, line)
                feature_code = FeatureCode(*line)
                self.feature_types_nb[feature_code.name] = feature_code

    def fill_feature_codes_nn(self):
        filename = u'featureCodes_nn.txt'
        if self.downloaded_dir:
            filename = os.path.join(self.downloaded_dir, filename)
        with codecs.open(filename, encoding='utf8') as file:
            for line in file.readlines():
                line = line.split(u'\t')
                line = map(str.strip, line)
                feature_code = FeatureCode(*line)
                self.feature_types_nn[feature_code.name] = feature_code

    def fill_feature_codes_no(self):
        filename = u'featureCodes_no.txt'
        if self.downloaded_dir:
            filename = os.path.join(self.downloaded_dir, filename)
        with codecs.open(filename, encoding='utf8') as file:
            for line in file.readlines():
                line = line.split(u'\t')
                line = map(str.strip, line)
                feature_code = FeatureCode(*line)
                self.feature_types_no[feature_code.name] = feature_code

    def fill_feature_codes_ru(self):
        filename = u'featureCodes_ru.txt'
        if self.downloaded_dir:
            filename = os.path.join(self.downloaded_dir, filename)
        with codecs.open(filename, encoding='utf8') as file:
            for line in file.readlines():
                line = line.split(u'\t')
                line = map(str.strip, line)
                feature_code = FeatureCode(*line)
                self.feature_types_ru[feature_code.name] = feature_code

    def fill_feature_codes_sv(self):
        filename = u'featureCodes_sv.txt'
        if self.downloaded_dir:
            filename = os.path.join(self.downloaded_dir, filename)
        with codecs.open(filename, encoding='utf8') as file:
            for line in file.readlines():
                line = line.split(u'\t')
                line = map(str.strip, line)
                feature_code = FeatureCode(*line)
                self.feature_types_sv[feature_code.name] = feature_code

    def fill_country_info(self):
        filename = u'countryInfo.txt'
        if self.downloaded_dir:
            filename = os.path.join(self.downloaded_dir, filename)
        with codecs.open(filename, encoding='utf8') as file:
            for line in file.readlines():
                if line.startswith(u'#'):
                    continue
                line = line.split(u'\t')
                line = map(str.strip, line)
                country = CountryInfo(*line)
                self.countries[country.ISO] = country

    def fill_admin1_codes(self):
        filename = u'admin1CodesASCII.txt'
        if self.downloaded_dir:
            filename = os.path.join(self.downloaded_dir, filename)
        with codecs.open(filename, encoding='utf8') as file:
            for line in file.readlines():
                line = line.split(u'\t')
                line = map(str.strip, line)
                admin = AdminCode(*line)
                self.admin1_codes[admin.code] = admin

    def fill_admin2_codes(self):
        filename = u'admin2Codes.txt'
        if self.downloaded_dir:
            filename = os.path.join(self.downloaded_dir, filename)
        with codecs.open(filename, encoding='utf8') as file:
            for line in file.readlines():
                line = line.split(u'\t')
                line = map(str.strip, line)
                admin = AdminCode(*line)
                self.admin2_codes[admin.code] = admin

    def fill_timezones(self):
        filename = u'timeZones.txt'
        if self.downloaded_dir:
            filename = os.path.join(self.downloaded_dir, filename)
        with codecs.open(filename, encoding='utf8') as file:
            for line in file.readlines()[1:]:
                line = line.split(u'\t')
                line = map(str.strip, line)
                timezone = TimeZone(*line)
                self.timezones[timezone.time_zone_id] = timezone

    def fill_alternate_names(self):
        filename = u'alternateNames/alternateNames.txt'
        if self.downloaded_dir:
            filename = os.path.join(self.downloaded_dir, filename)
        with codecs.open(filename, encoding='utf8') as file:
            for line in file.readlines()[:1000]:
                line = line.split(u'\t')
                line = map(str.strip, line)
                alternate_name = AlternateName(*line)
                self.alternate_names[alternate_name.geoname_id].append(alternate_name)


class TestDump(unittest.TestCase):
    def test_exist_iso_languages(self):
        self.assertEqual(
            dump.iso_languages_3['rus'],
            ISOLanguage(iso_639_3=u'rus', iso_639_2=u'rus', iso_639_1=u'ru', language_name=u'Russian')
        )
        self.assertEqual(
            dump.iso_languages_2['rus'],
            ISOLanguage(iso_639_3=u'rus', iso_639_2=u'rus', iso_639_1=u'ru', language_name=u'Russian')
        )
        self.assertEqual(
            dump.iso_languages_1['ru'],
            ISOLanguage(iso_639_3=u'rus', iso_639_2=u'rus', iso_639_1=u'ru', language_name=u'Russian')
        )

    def test_exist_feature_classes(self):
        self.assertEqual(
            dump.feature_classes['L'],
            FeatureClass(
                name='L',
                description='parks, area'
            )
        )

    def test_exist_feature_codes_bg(self):
        self.assertEqual(
            dump.feature_types_bg['H.CNL'],
            FeatureCode(
                name=u'H.CNL',
                short_description=u'канал',
                long_description=u'an artificial watercourse'
            )
        )

    def test_exist_feature_codes_en(self):
        self.assertEqual(
            dump.feature_types_en['H.CNL'],
            FeatureCode(
                name=u'H.CNL',
                short_description=u'canal',
                long_description=u'an artificial watercourse'
            )
        )

    def test_exist_feature_codes_nb(self):
        self.assertEqual(
            dump.feature_types_nb['H.CNL'],
            FeatureCode(
                name=u'H.CNL',
                short_description=u'kanal',
                long_description=u'an artificial watercourse'
            )
        )

    def test_exist_feature_codes_nn(self):
        self.assertEqual(
            dump.feature_types_nn['H.CNL'],
            FeatureCode(
                name=u'H.CNL',
                short_description=u'kanal',
                long_description=u'an artificial watercourse'
            )
        )

    def test_exist_feature_codes_no(self):
        self.assertEqual(
            dump.feature_types_no['H.CNL'],
            FeatureCode(
                name=u'H.CNL',
                short_description=u'kanal',
                long_description=u'an artificial watercourse'
            )
        )

    def test_exist_feature_codes_ru(self):
        self.assertEqual(
            dump.feature_types_ru['H.CNL'],
            FeatureCode(
                name=u'H.CNL',
                short_description=u'канал',
                long_description=u'искусственная река'
            )
        )

    def test_exist_feature_codes_sv(self):
        self.assertEqual(
            dump.feature_types_sv['H.CNL'],
            FeatureCode(
                name=u'H.CNL',
                short_description=u'kanal',
                long_description=u'an artificial watercourse'
            )
        )

    def test_exist_countries(self):
        self.assertEqual(
            dump.countries['RU'],
            CountryInfo(
                ISO=u'RU',
                ISO3=u'RUS',
                ISO_numeric=u'643',
                fips=u'RS',
                country=u'Russia',
                capital=u'Moscow',
                area=u'17100000',
                population=u'140702000',
                continent=u'EU',
                tld=u'.ru',
                currency_code=u'RUB',
                currency_name=u'Ruble',
                phone=u'7',
                postal_code_format=u'######',
                postal_code_regex=u'^(\\d{6})$',
                Languages=u'ru,tt,xal,cau,ady,kv,ce,tyv,cv,udm,tut,mns,bua,myv,mdf,chm,ba,inh,tut,kbd,krc,ava,sah,nog',
                geonameid=u'2017370',
                neighbours=u'GE,CN,BY,UA,KZ,LV,PL,EE,LT,FI,MN,NO,AZ,KP',
                equivalent_fips_code=u''
            )
        )

    def test_exist_admin1_codes(self):
        self.assertEqual(
            dump.admin1_codes['SI.L1'],
            AdminCode(
                code=u'SI.L1',
                name=u'Ribnica',
                ascii_name=u'Ribnica',
                geoname_id=u'3191679'
            )
        )

    def test_exist_admin2_codes(self):
        self.assertEqual(
            dump.admin2_codes['PE.15.1506'],
            AdminCode(
                code=u'PE.15.1506',
                name=u'Provincia de Huaral',
                ascii_name=u'Provincia de Huaral',
                geoname_id=u'3939284'
            )
        )

    def test_exist_timezones(self):
        self.assertEqual(
            dump.timezones['Europe/Moscow'],
            TimeZone(
                country_code=u'RU',
                time_zone_id=u'Europe/Moscow',
                GMT_offset=u'4.0',
                DST_offset=u'4.0',
                raw_offset=u'4.0'
            )
        )

    def test_exist_alternate_names(self):
        self.assertEqual(
            dump.alternate_names['17'][1],
            AlternateName(
                alternate_name_id=u'3556011',
                geoname_id=u'17',
                iso_language=u'fa',
                alternate_name=u'Kūh-e Shotor Khvāb',
                is_preferred_name=u'',
                is_short_name=u'',
                is_colloquial=u'',
                is_historic=u''
            )
        )

    def test_whitespace(self):
        for _dict in (dump.iso_languages_3, dump.feature_classes, dump.feature_types_bg, dump.feature_types_en, dump.feature_types_nb, dump.feature_types_nn, dump.feature_types_no, dump.feature_types_ru, dump.feature_types_sv, dump.countries, dump.admin1_codes, dump.admin2_codes, dump.timezones):
            for element in _dict.values():
                for field in element._fields:
                    self.assertNotRegex(getattr(element, field), r'\s+$', msg=element)
                    self.assertNotRegex(getattr(element, field), r'^\s+', msg=element)
        for _list in dump.alternate_names.values():
            for element in _list:
                for field in element._fields:
                    self.assertNotRegex(getattr(element, field), r'\s+$', msg=element)
                    self.assertNotRegex(getattr(element, field), r'^\s+', msg=element)


dump = Dump('downloaded')

if __name__ == '__main__':
    dump.fill()
    unittest.main()
