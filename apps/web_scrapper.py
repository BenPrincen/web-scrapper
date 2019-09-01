# imports
import bs4 as bs
import urllib.request

# functions
def findTitle(soup):
    return soup.title.string

def findScripts(soup):
    return soup.find_all("script", {"type":"text/javascript"})

def findPrice_Id(script_list, target):
    for scripts in script_list:
        string_scripts = scripts.text
        outcome = string_scripts.find(target)
        if outcome != -1:
            price = 0
            product_id = ''
            scripts_begin_index = string_scripts.find("'", string_scripts.find('product_sale_price')) + 1
            scripts_end_index = string_scripts.find("'", scripts_begin_index + 1)
            price = string_scripts[scripts_begin_index : scripts_end_index]

            scripts_begin_index = string_scripts.find("'", string_scripts.find('product_web_id')) + 1
            scripts_end_index = string_scripts.find("'", scripts_begin_index + 1)
            product_id = string_scripts[scripts_begin_index : scripts_end_index]

            return (price, product_id)

    print("Could not find tag with target info")
    return False
            
# main
def main():
    webpage = 'https://www.newegg.com/gray-asus-vivobook-s-s510un-ms52-mainstream/p/N82E16834235015?Item=N82E16834235015'
    source_code = urllib.request.urlopen(webpage).read()
    soup = bs.BeautifulSoup(source_code, 'lxml')

    utag_data = 'utag_data'

    title_string = findTitle(soup)
    script_blocks = findScripts(soup)
    price = findPrice_Id(script_blocks, utag_data)
    print(price)


if __name__ == '__main__':
    main()