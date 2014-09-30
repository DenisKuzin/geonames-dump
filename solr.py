# -*- coding: utf-8 -*-

from dump import Dump
import simplejson
import requests

BUCKET_SIZE = 100000

class Solr(object):
    def __init__(self, geonames_dump):
        self.geonames_dump = geonames_dump
        
    def post(self, docs):
        json = simplejson.dumps(docs)
        requests.post('http://127.0.0.1:8080/solr/trbd/update/json', data=json, headers={'content-type': 'application/json'})

    def send(self):
        buckets_count = 0
        docs = []
        for geoname in self.geonames_dump.get_geoname():
            doc = {}
            for field in geoname._fields:
                doc[field] = getattr(geoname, field)
            doc['id'] = 'geonames:all_countries:%s' % geoname.geoname_id
            doc['geometry_rpt'] = '%s %s' % (geoname.latitude, geoname.longitude)
            docs.append(doc)
            if len(docs) == BUCKET_SIZE:
                self.post(docs)
                del docs[:]
                buckets_count += 1
                print("Posted %s documents" % (buckets_count * BUCKET_SIZE))
        if len(docs) > 0:
            self.post(docs)
        json = '{"commit": { }}'
        requests.post('http://127.0.0.1:8080/solr/trbd/update/json', data=json, headers={'content-type': 'application/json'})
        print("Done")

if __name__ == '__main__':
    geonames_dump = Dump('downloaded')
    #dump.fill()
    solr = Solr(geonames_dump)
    solr.send()
