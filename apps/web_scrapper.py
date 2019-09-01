# imports
import bs4 as bs
import urllib.request
import os
import datetime

# functions
# removes quotes from any string to ensure the csv file is properly separated
def removeQuotes(str):
    string_no_quotes = ''
    for c in str:
        if c != ',':
            string_no_quotes += c
    return string_no_quotes

# returns the title of the html file
def findTitle(soup):
    return soup.title.string

# returns all javascript text from the html source code
def findScripts(soup):
    return soup.find_all("script", {"type":"text/javascript"})

# finds the information from the javascript text regarding the target variable
def findScriptInfo(string_scripts, target):
    scripts_begin_index = string_scripts.find("'", string_scripts.find(target)) + 1
    scripts_end_index = string_scripts.find("'", scripts_begin_index + 1)
    return string_scripts[scripts_begin_index : scripts_end_index]

# returns a tuple containing the item price, product id, and the product model
def findPriceIdTitle(script_list, target):
    for scripts in script_list:
        string_scripts = scripts.text
        outcome = string_scripts.find(target)
        if outcome != -1:
            price = 0
            product_id = ''
            product_title = ''
            price = findScriptInfo(string_scripts, 'product_sale_price')
            product_id = findScriptInfo(string_scripts, 'product_web_id')
            product_model = findScriptInfo(string_scripts, 'product_model')

            return (price, product_id, product_model)

    print("Could not find tag with target info")
    return False

def getCSVPath(id):
    return os.path.join(os.getcwd(), "csv", id + ".csv")
# main
def main():
    #webpage = input('Please enter the url of the item you would like to track:\n')
    webpage = 'https://www.newegg.com/gray-asus-vivobook-s-s510un-ms52-mainstream/p/N82E16834235015?Item=N82E16834235015'
    source_code = urllib.request.urlopen(webpage).read()
    soup = bs.BeautifulSoup(source_code, 'lxml')

    utag_data = 'utag_data'

    title_string = findTitle(soup)
    title_string = removeQuotes(title_string)
    script_blocks = findScripts(soup)
    price_id_title = findPriceIdTitle(script_blocks, utag_data)
    
    csv_path = getCSVPath(price_id_title[1])
    mode = 'w+'
    if(os.path.exists(csv_path)):
        mode = 'a'
    
    with open(csv_path, mode) as f:
        print(price_id_title[2] + ',' + price_id_title[0] + ',' + str(datetime.date.today()), file = f)
    f.close()


if __name__ == '__main__':
    main()