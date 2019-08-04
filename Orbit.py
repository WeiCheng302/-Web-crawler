import urllib.request
from bs4 import BeautifulSoup
import datetime
import urllib.request

url='https://qc.sentinel1.eo.esa.int/aux_poeorb/?page=1'
f = open('filelist.txt','a')
f.write('==============New Practice==============')
def get_content(url):
    html = urllib.request.urlopen(url)
    content = html.read().decode('utf-8')
    html.close()
    return content

get_content(url)

base_url='https://qc.sentinel1.eo.esa.int/aux_poeorb'
urls=[base_url]

for i in range(2, 5):
    urls.append(base_url+"/?page=%d"%i)
    print(urls)

Dlist=[ ]
for url in urls[:3]:
    content= get_content(url)
    soup = BeautifulSoup(content,  "html.parser")
    filelinks = soup.find_all('td')
    Dlist.append(filelinks[0],)
    for i in range(len(filelinks)):
        Dlist.append(filelinks[i])

print(Dlist)
count=0
link=str(Dlist[13:140])
print('123')
print(link)
print('123')

for i in range(len(Dlist)):
    currentfile = str(Dlist[count])
    link = str(currentfile[13:140])
    date = datetime.datetime(int(currentfile[105:109]), int(currentfile[109:111]), int(currentfile[111:113]))
    day = str(date + datetime.timedelta(days=1))
    filename = currentfile[63:140]
    print('Begin Downloading：', str(currentfile[63:66]), day)
    urllib.request.urlretrieve(link, filename)
    f.write(filename)
    f.write('\n')
    count+=1
    print('Finish Downloading：', str(currentfile[63:66]), day)

f.close()




