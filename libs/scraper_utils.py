import os


PROJECT_FOLDER = 'C:\\Users\\Benjamin Princen\\Workspace\\projects\\web_scrapper\\web-scrapper\\'
MODEL = 0
PRICE = 1
DATE = 2
ID = 2


def extractInfoFromLine(line):
    return line.split(',')


def shouldUpdatePrice(csv_file, extracted_price):
    """
    checks if csv file should be updated or not

    Checks if the extracted price is the same as
    the last updated price in the csv file

    Parameters:
    csv_file (file object): Opened csv file. Will throw error if file mode is not 'r'
    extracted_price (int): The price extracted from html source code

    Returns:
    boolean: Returns true if the csv file should be updated with new info, false if otherwise
    """
    csv_file = csv_file.readlines()
    for line in csv_file:
        pass
    line_info = extractInfoFromLine(line)
    print(line_info[PRICE])
    return not line_info[PRICE] == extracted_price


def trackedProductList():
    """
    Checks csv directory and returns the list of tracked product ids

    Iterates through csv directory and returns a list of all of the
    file names without the extension

    Parameters:
    None

    Returns:
    string list: List of file names without extension
    """
    csv_dir_path = os.path.join(
        PROJECT_FOLDER, "csv")
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
    return soup.find_all("script", {"type": "text/javascript"})

# finds the information from the javascript text regarding the target variable


def findScriptInfo_am(string_line, target):
    begin_index = string_line.find('"', string_line.find(target)) + 1
    end_index = string_line.find('"', begin_index)
    return string_line[begin_index: end_index]


def findScriptInfo_ne(string_scripts, target):
    """
    Extracts information from javascript text.

    Extracts information from javascript text based on
    the target passed in. The method of extracting text is
    based on the format observed in the Newegg.com html source
    code.

    Parameters:
    string_scripts (string): javascript text
    target (string): The javascript variable the user is looking to extract

    Returns:
    string: Returns the information contained within the target variable
    stored in the javascript text
    """
    scripts_begin_index = string_scripts.find(
        "'", string_scripts.find(target)) + 1
    scripts_end_index = string_scripts.find("'", scripts_begin_index + 1)
    return string_scripts[scripts_begin_index: scripts_end_index]


def findData(soup):
    return soup.find("div", {"id": "cerberus-data-metrics"})


def findTitlePriceId_am(line, title):
    string_line = line.text
    price = findScriptInfo_am(string_line, 'data-asin-price')
    product_id = findScriptInfo_am(string_line, 'data-asin')
    product_title = title
    return (product_title, price, product_id)


def findTitlePriceId_ne(script_list, target='utag_data'):
    for scripts in script_list:
        string_scripts = scripts.text
        outcome = string_scripts.find(target)
        if outcome != -1:
            price = findScriptInfo_ne(string_scripts, 'product_sale_price')
            product_id = findScriptInfo_ne(string_scripts, 'product_web_id')
            product_model = findScriptInfo_ne(string_scripts, 'product_model')

            return (product_model, price, product_id)

    print("Could not find tag with target info")
    return False


def getCSVPath(id):
    return os.path.join(PROJECT_FOLDER, "csv", id + ".csv")
