import os
from google.cloud import storage

def upload_to_gstorage(bucket_name, blob_name, file_name):
	# Setup google cloud storage
	os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credential.json'
	client = storage.Client()
	
	# Trying upload image to google cloud storage
	try:
		bucket = client.get_bucket(bucket_name)
		blob = bucket.blob(blob_name)
		blob.upload_from_filename(file_name)
		link = 'https://storage.googleapis.com/{}/{}'.format(bucket_name, blob_name)
		print('success')
		print('your img link is:', link)
		return(link)
	except Exception as e:
		print('error')
		print(e) 	
		return(e)
