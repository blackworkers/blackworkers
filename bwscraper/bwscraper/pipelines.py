# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
import json
import requests
import datetime
from scrapy.exceptions import DropItem

class BwscraperPipeline(object):

    def open_spider(self, spider):
        global etl_time
        etl_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%MS")

    #def close_spider(self, spider):


    def process_item(self, item, spider):

        def reverse_geocode(lat, lon):
            url = "http://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode?f=pjson&featureTypes=&location=" + str(lon) + "," + str(lat)

            req = requests.get(url)

            query=req.json()

            location = {}



            #raise DropItem("############ LOOK FOR THE LOCATION DICT HERE:", query)

            location['city'] = query['address']['City']
            location['state'] = query['address']['Region']
            location['country']=query['address']['CountryCode']

            return location

        conn = psycopg2.connect("dbname=bw user=postgres password=bwadmin")
        cur = conn.cursor()

        if item['loc_name'] is not None:

            location = reverse_geocode(item['loc_lat'],item['loc_long'])
            #location = []
            cur.execute("INSERT INTO staging.posts_raw VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (item['job_hashtag'], item['id'],item['scraped_timestamp'],item['shortcode'],item['caption'],
            item['display_url'],item['loc_id'],item['loc_name'],item['loc_lat'],item['loc_long'],item['owner_id'],item['owner_name'],item['likes'],item['taken_at_timestamp'],location['city'],location['state'],location['country'],etl_time))
            conn.commit()
            cur.close()
            conn.close()
            print("############## ITEM HAS BEEN COMMITTED BY NOW")
        else:
            raise DropItem("DROPPING ITEM DUE TO MISSING LOCATION: %s" % item['loc_name'])
            cur.close()
            conn.close()
        return item
