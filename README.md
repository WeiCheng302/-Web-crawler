# -Web-crawler
 Web crawler on python to automatically download POD Precise Orbit Ephemerides from https://qc.sentinel1.eo.esa.int/aux_poeorb
Download all the files to the same folder.

Orbit.py can help Batch download the Precise Orbit Ephemerides of Sentinel 1A and Sentinel 1B 
from 'https://qc.sentinel1.eo.esa.int/aux_poeorb/".
By adjusting the parameter in the for loop, the range of the downloading can be changed.

Specificdayorbitdownload.py can help download the Precise Orbit Ephemerides of Sentinel 1A and Sentinel 1B ON SPECIFIC DAY
from 'https://qc.sentinel1.eo.esa.int/aux_poeorb/".
After enterning the program, type the date as YYYYMMDD, and type A for S1A while B for S1B.

Python 3.7
BeautifulSoup 4.8.0
Datetime 4.3
Requeat 2.22.0