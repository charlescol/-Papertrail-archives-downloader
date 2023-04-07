import requests
import json
import os
import gzip
import argparse
from datetime import datetime
from progressbar import ProgressBar, Percentage, Bar, ETA, FileTransferSpeed


""" Add input arguments """
argParser = argparse.ArgumentParser()
argParser.add_argument("-s", "--start", type=str, help="Date from which start to download archives", required=True)
argParser.add_argument("-e", "--end", type=str, help="Date from which end to download archives", required=True)
argParser.add_argument("-t", "--token", type=str, help="Papertrail token", required=True)
argParser.add_argument("-o", "--output", type=str, help="Output path", required=False, default="./logs/")

args = argParser.parse_args()

""" Format Input """
url = "https://papertrailapp.com/api/v1/archives"
headers = {"X-Papertrail-Token": args.token}
result_path = args.output
result_zipped_path = result_path + "zip/"
start_date = datetime.strptime(args.start, "%Y-%m-%d")
end_date = datetime.strptime(args.end, "%Y-%m-%d")

""" Download a given url """
def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True, headers=headers)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

""" Create directory """
if not os.path.isdir(result_zipped_path):
   os.makedirs(result_zipped_path)

response = requests.get(url, headers=headers)
archives_urls = []
archives = json.loads(response.text)

""" Build progressbar """
print('Start downloading archives from ' + args.start + ' to ' + args.end + '...');
widgets = ["State : " , Percentage(), ' ', Bar(marker='0',left='[',right=']'), ' ', ETA(), ' ', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets, maxval=len(archives))
pbar.start()

""" Download archives """
count = 0
for archive in archives : 
	date = datetime.strptime(archive['start'][:10], "%Y-%m-%d")
	if start_date <= date <= end_date:
		""" Download archives """
		href = archive["_links"]["download"]["href"]
		download_url(href, result_zipped_path + archive["filename"])
		
		""" Extract the downloaded file """
		with gzip.open(result_zipped_path + archive["filename"], 'rb') as f:
			file_content = f.read()
            
		""" Write the extracted file content to a new file """
		with open(result_path + archive["filename"][:-3], 'wb') as f:
			f.write(file_content)

	""" Update progressbar """			
	count += 1
	pbar.update(count)

#find logs -type f -print0 | xargs -0 grep -rE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'