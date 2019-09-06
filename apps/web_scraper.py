# IMPORTS
import bs4 as bs
import urllib.request
import os
import datetime
import sys

sys.path.insert(1, os.path.join(os.getcwd(), "libs"))
import scraper_utils as scraper

MODEL = 0
PRICE = 1
DATE  = 2
ID    = 2

# PSUEDOCODE 
# 
# Get product page url
# Parse html source code
# Extract information such as price, id
# Check the existing csv files and cross check csv file name with id
# Create new csv file if csv file does not already exist
# if csv file exists then check price
# if price is different then append new information otherwise don't do anything
# if new information is appended then the user should be notified of the price change
#
# MAIN
def main():
    #webpage = input('Please enter the url of the item you would like to track:\n')
    webpage = 'https://www.newegg.com/gray-asus-vivobook-s-s510un-ms52-mainstream/p/N82E16834235015?Item=N82E16834235015'
    source_code = urllib.request.urlopen(webpage).read()
    soup = bs.BeautifulSoup(source_code, 'lxml')

    utag_data = 'utag_data'

    script_blocks = scraper.findScripts(soup)
    title_price_id = scraper.findTitlePriceId(script_blocks, utag_data)
    
    csv_path = scraper.getCSVPath(title_price_id[ID])
    mode = ''
    if(os.path.exists(csv_path)):
        with open(csv_path, 'r') as f:
            if(scraper.shouldUpdatePrice(f, title_price_id)):
                mode = 'a'
            f.close()
    else:
        mode = 'w+'
    
    if(mode != ''):
        with open(csv_path, mode) as f:
            if(mode == 'w+'):
                print('MODEL,PRICE,DATE', file = f)
            print(title_price_id[MODEL] + ',' + title_price_id[PRICE] + ',' + str(datetime.date.today()), file = f)
            f.close()


if __name__ == '__main__':
    main()