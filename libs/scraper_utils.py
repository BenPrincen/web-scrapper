import os

MODEL = 0
PRICE = 1
DATE  = 2
ID    = 2

def extractInfoFromLine(line):
    return line.split(',')

def shouldUpdatePrice(csv_file, extracted_price):
    csv_file = csv_file.readlines()
    for line in csv_file:
        pass
    line_info = extractInfoFromLine(line)
    return not line[PRICE] == extracted_price


def trackedProductList():
    csv_dir_path = os.path.join(os.getcwd(), "csv")
    product_id_list = []
    for csv_files in os.listdir(csv_dir_path):
        if csv_files.endswith(".csv"):
            product_id_list.append(os.path.splitext(csv_files)[0])
    return product_id_list

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
def findTitlePriceId(script_list, target):
    for scripts in script_list:
        string_scripts = scripts.text
        outcome = string_scripts.find(target)
        if outcome != -1:
            price = findScriptInfo(string_scripts, 'product_sale_price')
            product_id = findScriptInfo(string_scripts, 'product_web_id')
            product_model = findScriptInfo(string_scripts, 'product_model')

            return (product_model, price, product_id)

    print("Could not find tag with target info")
    return False

def getCSVPath(id):
    return os.path.join(os.getcwd(), "csv", id + ".csv")