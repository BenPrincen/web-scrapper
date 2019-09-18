from libs import scraper_utils as scraper


def main():
    line = '''<div id="cerberus-data-metrics" style="display: none;" 
        data-asin="B07KVKRLG2" data-asin-price="1200.00" data-asin-shipping="" 
        data-asin-currency-code="" data-substitute-count="20" data-device-type="WEB" 
        data-display-code="Cerberus displayed" >'''

    target = 'data-asin-price'
    price = scraper.findScriptInfo_am(line, target)

    target = 'data-asin'
    web_id = scraper.findScriptInfo_am(line, target)

    print('price: ' + price)
    print('web id: ' + web_id)


if __name__ == '__main__':
    main()
