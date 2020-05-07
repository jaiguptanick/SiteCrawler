import urllib.request   #this module helps to connect with the u=URLs
import io

def get_robots_txt(url):
    if url.endswith('/'):   # adding /after url if user didnt added
        path = url
    else :
        path = url + "/"
    req = urllib.request.urlopen(path + "robots.txt", data=None)
    data = io.TextIOWrapper(req, encoding='utf-8') #This converts recieved data in UTF8 and changes line
    return data.read()
#print(get_robots_txt('https://www.google.com'))