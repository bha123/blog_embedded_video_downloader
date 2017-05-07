import sys
import datetime
import time
import os
from shutil import copyfile
from urlparse import urlparse
import urllib2
from bs4 import BeautifulSoup
import requests
import base64
import urllib

# Global variables

links_file = "Download_href_links.txt"
headers = {'Referer' :'http://cksvforu.blogspot.in/', 'X-Requested-With': 'ShockwaveFlash/24.0.0.221', 'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}


# Read links file and make a copy with  file name <date-time-task>

links_file = os.path.abspath(links_file)
#timestr = time.strftime('%d_%m_%Y-%H%M%S-task')+ ".txt"
timestr = 'Download-task.txt'
#fo = open(timestr,"wb")
#fo.close()
dest_file = os.path.abspath(timestr)
print links_file
print dest_file
print "Created the task file " , dest_file

if not os.path.exists(dest_file):
    copyfile(links_file,dest_file)
    
# Read the first line of the dest_file
fo = open(timestr,'r')
line = str(fo.readline())
while line:
    print line
    fo.close()
    # Extract Endpoint
    o = urlparse(line)
    endpoint = (o.path.split('/')[-1]).split('.')[0]
    # Extract download links from given file
    response = urllib2.urlopen(line)
    soup = BeautifulSoup(response, 'html.parser')
    if not os.path.exists('d_v'):
        os.mkdir('d_v')
    temp_urls = []
    itr = 0
    
    for link in soup.find_all('embed'):
        number_retries = 0
        url = urllib.unquote(str(str(link.get('flashvars').split('&iurl')).split('=')[1]).split("'")[0]).decode('utf-8')  
        r = requests.get(url, headers=headers, stream=True)
        while r.status_code != 200 and number_retries < 5:
            print "Entering While loop for max 5 tries"
            time.sleep(5)
            r = requests.get(url, headers=headers, stream=True)
            number_retries += 1
        print r
        print url
        file_name = endpoint+"_"+str(itr)+".mp4"
        file_abs_path = os.path.join("d_v\\"+file_name)
        print file_abs_path    
        with open(file_abs_path, 'wb') as handle:
            if not r.ok:
                # Something went wrong
                print "Block failed for file ", file_name
                print r
            for block in r.iter_content(1024):
                handle.write(block)
            itr = itr + 1
    
    print "Download completed"
    #Removing the first line from file
    with open(dest_file, 'r') as fin:
        print "Entering Reading of file"
        data = fin.read().splitlines(True)
    with open(dest_file, 'w') as fout:
        print "Entering Deleting the line of file"
        fout.writelines(data[1:])
    #Reading the next line
    fo = open(timestr,'r')
    line = str(fo.readline())
    
    
