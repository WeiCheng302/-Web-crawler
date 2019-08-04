import urllib.request
from bs4 import BeautifulSoup
import datetime
import urllib.request
import os

#Set initial value
url = 'https://qc.sentinel1.eo.esa.int/aux_poeorb/?page=1'

dateIwant ='20180121' #input("Please Enter Your Date As YYYYMMDD EX.20190805")
print(dateIwant)
daycheck=int(dateIwant)-int(20140801)
if daycheck<0:
    print('Please Enter The Date After 20140801')
    os._exit(1215)

data = 'B'#input('Enter A for SentinelA file, Enter B for SentinelB file')
print(data)
if data != 'A' and data != 'B' :
    print('Please Enter A or B')
    os._exit(1215)

date = datetime.datetime(int(dateIwant[0:4]), int(dateIwant[4:6]), int(dateIwant[6:8]))
dateshow=str(date)
print(dateshow)
dateIwant = str(date + datetime.timedelta(days=-1))
month1 = str(date + datetime.timedelta(days=32-int(dateIwant[5:7])))
month = month1[5:7]
year1 = str(date + datetime.timedelta(days=-365))
year = year1[0:4]


def get_content(url):
    html = urllib.request.urlopen(url)
    content = html.read().decode('utf-8')
    html.close()
    return content

get_content(url)

base_url = 'https://qc.sentinel1.eo.esa.int/aux_poeorb'
urls = [base_url]
check = 0
k=0
for i in range(1,1000):
    urlpage=base_url + "/?page=%d" % i
    print(urlpage)
    content = get_content(urlpage)
    soup = BeautifulSoup(content, "html.parser")
    filelinks = soup.find_all('td')
    a=0
    fileday = str(filelinks[a])
    if check== 1:
        print('finish')
        break
    if dateshow[8:10] == '01':
        for j in fileday:
            if fileday[105:109] == dateshow[0:4]:
                if  fileday[109:111] == dateIwant[5:7]:
                    if fileday[111:113] == dateIwant[8:10] and fileday[65] == data:
                        print(urlpage)
                        print(fileday)
                        link = str(fileday[13:140])
                        filename = fileday[63:140]
                        print('Begin Downloading：', str(fileday[63:66]), dateshow)
                        urllib.request.urlretrieve(link, filename)
                        print('Finish Downloading：', str(fileday[63:66]), dateshow)
                        check = 1
                        break
                    if fileday[111:113] == dateIwant[8:10] and fileday[65] != data:
                        a += 1
                        if a == len(filelinks):
                            break
                        fileday = str(filelinks[a])
                if fileday[109:111] != dateIwant[5:7]:
                    a += 1
                    if a==len(filelinks):
                        break
                    fileday = str(filelinks[a])
    if check== 1:
        print('finish')
        break
    if fileday[105:109] == dateIwant[0:4]: #year equal
        print(fileday)
        for j in range(100):
            if fileday[109:111] == dateIwant[5:7] :#or fileday[109:111] == dateshow[5:7]:
                print(fileday)
                if fileday[111:113] == dateIwant[8:10] and fileday[65] == data: #day equal and satelite equal
                    print(urlpage)
                    print(fileday)
                    link = str(fileday[13:140])
                    filename = fileday[63:140]
                    print('Begin Downloading：', str(fileday[63:66]), dateshow)
                    urllib.request.urlretrieve(link, filename)
                    print('Finish Downloading：', str(fileday[63:66]), dateshow)
                    check = 1
                    break
                if fileday[111:113] == dateIwant[8:10] and fileday[65] != data:
                    a+=1
                    fileday = str(filelinks[a])
                if fileday[111:113] != dateIwant[8:10] :
                    print(k)
                    k+=1
                    a+=1
                    if a==len(filelinks):
                        break
                    fileday = str(filelinks[a])
            if fileday[109:111] != dateIwant[4:6]:
                pass

