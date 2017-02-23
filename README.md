# Expedia Crawler

Simple script to get best offers from expedia given codes for departure and destination cities, departure and return dates, and other dates on the future based on these dates

**date format: mm/dd/yyyy**

**use 3 letter code for cities**, if you are not sure what the code for a city is you can see it here:
*http://www.iata.org/publications/Pages/code-search.aspx* choose location name and enter the city

## Example:
if you want to travel from New York(NYC) to San Francisco(SFO) from 03/15/2017 to 03/25/2017 but want to also see offers from 2 dates in advance(03/02 and 03/03):

**python3 crawl NYC SFO 03/01/2017 03/18/2017 2**

## Requirements:
**python 3**: https://www.python.org/downloads/

**firefox**: https://www.mozilla.org/en-US/firefox/new/

**geckodriver** you can get it using the script here https://gist.github.com/tristandostaler/2f8b28f2bf503db4422a5549e8fed538

## Download
Unix: https://github.com/Shadi-A/ExpediaCrawler/blob/master/dist/ExpediaCrawler-1.0.linux-x86_64.tar.gz

Windows: https://github.com/Shadi-A/ExpediaCrawler/blob/master/dist/ExpediaCrawler-1.0.linux-x86_64.exe