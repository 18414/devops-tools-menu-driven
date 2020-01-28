import os
#import urllib
import urllib.request 
#import urllib
#import urlopen

try:
    from urllib.request  import urlopen
except ImportError:
    from urllib2 import urlopen


url_ends_with = ".tar.gz\""         # Use line for Non-Windows
#url_ends_with = "windows-x64.zip\"" # Use line for Windows-x64

url_starts_with = "\"http"
dir_to_contain_download = "/tmp/"
tomcat_apache_org_frontpage_html = "tomcat.apache.org.frontpage.html"
download_page = "https://tomcat.apache.org/download-90.cgi"

try:
    if not os.path.exists(dir_to_contain_download):
        os.makedirs(dir_to_contain_download, exist_ok=True)

    htmlfile = urllib.request.urlretrieve(download_page, dir_to_contain_download + tomcat_apache_org_frontpage_html)
    fp = open(dir_to_contain_download + tomcat_apache_org_frontpage_html)
    line = fp.readline()
    cnt = 1
    while line:
        line = fp.readline()
        cnt += 1
        if url_ends_with in line and url_starts_with in line:
            tomcat_url_index = line.find(url_ends_with)
            tomcat_url = line[line.find(url_starts_with) + 1 : tomcat_url_index + len(url_ends_with) - 1]
            print ("Downloading: " +  tomcat_url)
            print ("To file: " + dir_to_contain_download + tomcat_url[tomcat_url.rfind("/")+1:])
            zipfile = urllib.request.urlretrieve(tomcat_url, dir_to_contain_download + tomcat_url[tomcat_url.rfind("/")+1:])
            break
finally:
    fp.close()
    os.remove(dir_to_contain_download + "/" + tomcat_apache_org_frontpage_html)
