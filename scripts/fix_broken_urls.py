import requests
from bs4 import BeautifulSoup
import re
import json
from pg import DB

file = open('broken_urls_failures.out','w')

def connect_db():
	global con
	con = DB(dbname='bw', host='localhost', port=5432, user='bw_admin', passwd='')

def get_new_url(instagram_handle):
	r = requests.get('https://www.instagram.com/{}/'.format(instagram_handle))
	soup = BeautifulSoup(r.content, features="lxml")
	scripts = soup.find_all('script', type="text/javascript", text=re.compile('window._sharedData'))
	stringified_json = scripts[0].get_text().replace('window._sharedData = ', '')[:-1]

	try:
		parsed = json.loads(stringified_json)['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
	except Exception as e:
		print("Unable to fix this broken url for user '{}'. Operation failed with error '{}'".format(instagram_handle, str(e)))
		return('0','URL Permanently Broken')

	iter = 0

	final_likes = 0
	img_url = ''
	caption = ''
	shortcode = ''

	for i in parsed:
		try:
			if iter == 0:
				final_likes = i['node']['edge_media_preview_like']['count']
			iter = iter + 1
			caption = i['node']['edge_media_to_caption']['edges'][0]['node']['text']
			likes = i['node']['edge_media_preview_like']['count']
			img_url = i['node']['thumbnail_resources'][4]['src']
			shortcode = i['node']['shortcode']

			if likes > final_likes:
				final_likes = likes
		except Exception as e:
			print("Failed to gather data for user '{}'".format(instagram_handle))
			file.write("Failed to gather data for user '{}'\n".format(instagram_handle))
			break

	return(final_likes, img_url, caption, shortcode)

def get_urls():
	cmd = "SELECT instagram_handle, display_url FROM artists_artistsraw WHERE likes > 100 ORDER BY likes "
	query = con.query(cmd).getresult()
	return query


def validate_urls():
	for i in get_urls():
		instagram_handle = i[0]
		r = requests.get(i[1])
		soup = BeautifulSoup(r.content, features="lxml")
		response = soup.get_text()
		if response == "URL signature expired":
			print("Expired URL signature found for user '{}', getting latest images".format(instagram_handle))
			new_urls = get_new_url(instagram_handle)
			print("New data obtained for user '{}', updating now".format(instagram_handle))
			try:
				likes = new_urls[0]
				img_url = new_urls[1]
				caption = new_urls[2].replace("'", "").replace("\"", "")
				shortcode = new_urls[3]
				update_db_urls(caption, likes, img_url, shortcode, instagram_handle)
			except Exception as e:
				print("Could not update row for user '{}' despite getting new data. Update failed with error '{}'".format(instagram_handle, str(e)))
				file.write("Could not update row for user '{}' despite getting new data. Update failed with error '{}'\n".format(instagram_handle, str(e)))

def update_db_urls(caption, likes, img_url, shortcode, instagram_handle):
	cmd = "UPDATE artists_artistsraw SET caption = '{}', likes = '{}', display_url = '{}', shortcode = '{}' WHERE instagram_handle = '{}'".format(caption, likes, img_url, shortcode, instagram_handle)
	print("Attempting update statement on instagram user '{}'".format(instagram_handle))

	try:
		con.query(cmd)
		print("Successfully updated row for user '{}'".format(instagram_handle) )
	except Exception as e:
		print("Error when updating row with for user '{}' with following error'{}'".format(instagram_handle,str(e)))
		file.write("Error when updating row with for user '{}' with following error'{}'\n".format(instagram_handle,str(e)))

def main():
	connect_db()
	validate_urls()

main()

file.close()
