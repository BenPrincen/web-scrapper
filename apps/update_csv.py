# IMPORTS
import bs4 as bs
import urllib.request
import os
import datetime
import sys
from win10toast import ToastNotifier

sys.path.insert(1, os.path.join(os.getcwd(), "libs"))
import scraper_utils as scraper

# FUNCTIONS

# website url format: https://www.newegg.com/p/<web product id>
def generateProductUrl(product):
    return 'https://www.newegg.com/p/' + product


# PSUEDOCODE
# 
# Identify directory containing csv files
# Loop through csv files in directory and extract the file name
# Use the file name to access the product page
# Parse information from product page and update information in csv file if necessary
# If information is updated add it to the list of new info
# After updates for all csv files are complete, notify the user of the updated info if there is any
# Run this script a designated number of times per day
# Write a log file that has more detailed information on price updates
#
# MAIN
def main():
    product_list = scraper.trackedProductList()
    updated_info_list = []
    for product in product_list:
        webpage = generateProductUrl(product)
        source_code = urllib.request.urlopen(webpage).read()
        soup = bs.BeautifulSoup(source_code, 'lxml')

        utag_data = 'utag_data'

        script_blocks = scraper.findScripts(soup)
        title_price_id = scraper.findTitlePriceId(script_blocks, utag_data)
        
        csv_path = scraper.getCSVPath(title_price_id[2])
        
        mode = ''
        with open(csv_path, 'r') as f:
            if scraper.shouldUpdatePrice(f, title_price_id[1]):
                updated_info_list.append(title_price_id[0] + ': ' + str(title_price_id[1]))
                mode = 'a'
            f.close()

        if mode != '':
            with open(csv_path, mode) as f:
                print(title_price_id[0] + ',' + title_price_id[1] + ',' + str(datetime.date.today()), file = f)
                f.close()
    toast_notif_string = ''
    for update in updated_info_list:
        toast_notif_string += update + '\n'
    toast_notif_string += 'More info in log file'
    toast = ToastNotifier()
    toast.show_toast('Updated Product Prices', toast_notif_string, duration = 10)



if __name__ == '__main__':
    main()