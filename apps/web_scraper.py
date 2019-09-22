# IMPORTS
from libs import scraper_utils as scraper
import bs4 as bs
import urllib.request
import os
import datetime
import sys


def neweggSetup(soup):
    script_blocks = scraper.findScripts(soup)
    title_price_id = scraper.findTitlePriceId_ne(
        script_blocks, scraper.findTitle(soup))
    csv_path = scraper.getCSVPath(title_price_id[ID])
    writeCSV(csv_path, title_price_id)


def amazonSetup(soup):
    lines = scraper.findData(soup)
    title_price_id = scraper.findTitlePriceId_am(lines, )
    csv_path = scraper.getCSVPath(title_price_id[ID])
    writeCSV(csv_path, title_price_id)


def writeCSV(csv_path, title_price_id):
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
                print('MODEL,PRICE,DATE', file=f)
            print(title_price_id[MODEL] + ',' + title_price_id[PRICE] +
                  ',' + str(datetime.date.today()), file=f)
            f.close()


# CONSTANTS
MODEL = 0
PRICE = 1
DATE = 2
ID = 2

NEWEGG = 0
AMAZON = 1

WEBSITE = -1

website_list = ['newegg', 'amazon']
website_func_list = {
    0: neweggSetup,
    1: amazonSetup,
}

# PSUEDOCODE
#
# Get product page url
# Parse html source code
# Extract information such as price, id
# Check the existing csv files and cross check csv file name with id
# Create new csv file if csv file does not already exist
# if csv file exists then check price
# if price is different then append new information otherwise don't do anything
# if new information is appended then the user should be notified of the change


def main():
    webpage = input(
        'Please enter the url of the item you would like to track:\n')

    iterator = 0
    valid_website = False
    for string in website_list:
        if webpage.lower().find(string) != -1:
            print('able to find webpage')
            WEBSITE = iterator
            valid_website = True
            break
        iterator += 1

    if not valid_website:
        # print error and break from program
        print('Website entered is not supported')

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = opener.open(webpage)
    source_code = response.read()
    soup = bs.BeautifulSoup(source_code, 'lxml')
    #source_code = urllib.request.urlopen(webpage).read()
    #soup = bs.BeautifulSoup(source_code, 'lxml')

    # call the respective function based on the website url
    website_func_list[WEBSITE](soup)


if __name__ == '__main__':
    main()
