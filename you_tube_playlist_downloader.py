from pytube import YouTube
import bs4,requests

import pprint
url = input('Enter the url of the playlist: ')
res = requests.get(url)
#print (pprint.pformat(res.text,indent=4))
soup = bs4.BeautifulSoup(res.text,'html.parser')
table = soup.find_all('table',{'class':'pl-video-table'})
list1 = table[0].find_all("tr")
for i in range(len(list1)):
    k = list1[i].get('data-video-id')
    url = 'http://www.youtube.com/watch?v='+k
    yt = YouTube(url)
    video = yt.get('mp4', '360p')
    print ('downloading video... ')
    video.download('C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python36\\programs')    
