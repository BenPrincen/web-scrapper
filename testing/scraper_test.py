from libs import scraper_utils as scraper
import unittest
import os


class TestWebScrapperMethods(unittest.TestCase):

    def testExtractLineInfo(self):
        line = 'S258FG,129.99,12/2/2019'
        line_info = scraper.extractInfoFromLine(line)
        self.assertEqual(line_info[0], 'S258FG')
        self.assertEqual(line_info[1], '129.99')
        self.assertEqual(line_info[2], '12/2/2019')

    def testfindScriptInfo_ne(self):
        script = '''<script type='text/javascript'>
      var utag_data = {
            page_breadcrumb:'Home &gt; Computer Systems &gt; Desktop Computers &gt; Gaming Desktops &gt; iBUYPOWER &gt; Item#:N82E16883227879',
            page_tab_name:'Computer Systems',
            product_category_id:['228'],
            product_category_name:['Desktop Computers'],
            product_subcategory_id:['3742'],
            product_subcategory_name:['Gaming Desktops'],
            product_id:['83-227-879'],
            product_web_id:['N82E16883227879'],
            product_title:['iBUYPOWER Gaming Desktop Trace2 R7X70 Ryzen 7 2nd Gen 2700X &amp;#40;3.70 GHz&amp;#41; 16 GB DDR4 2 TB HDD 240 GB SSD NVIDIA GeForce RTX 2070 Windows 10 Home 64-bit'],
            product_manufacture:['iBUYPOWER'],
            product_sale_price:['1250.00'],
            product_default_shipping_cost:['0.01'],
            product_model:['Trace2 R7X70'],
            product_instock:['1'],
            product_group_id:['17804620'],
            page_type:'Product',
            site_region:'USA',
            site_currency:'USD',
            page_name:'NewProductDetail',
            search_scope:jQuery('#haQuickSearchStore option:selected').text(),
            user_nvtc:Web.StateManager.Cookies.get(Web.StateManager.Cookies.Name.NVTC),
            user_name:Web.StateManager.Cookies.get(Web.StateManager.Cookies.Name.LOGIN,'LOGINID6'),
            third_party_render:['2a5e772a0f941c862180037f8a5c118c7abf2f7d']
            
      };
      </script>'''

        target = 'product_web_id'
        script_web_id = scraper.findScriptInfo_ne(script, target)

        target = 'product_sale_price'
        script_price = scraper.findScriptInfo_ne(script, target)

        target = 'product_model'
        script_model = scraper.findScriptInfo_ne(script, target)

        self.assertEqual(script_web_id, "N82E16883227879")
        self.assertEqual(script_price, "1250.00")
        self.assertEqual(script_model, "Trace2 R7X70")

    def testfindScriptInfo_am(self):
        line = '''<div id="cerberus-data-metrics" style="display: none;" 
        data-asin="B07KVKRLG2" data-asin-price="" data-asin-shipping="" 
        data-asin-currency-code="" data-substitute-count="20" data-device-type="WEB" 
        data-display-code="Cerberus displayed" >'''

        target = 'data-asin-price'
        price = scraper.findScriptInfo_am(line, target)

        target = 'data-asin'
        web_id = scraper.findScriptInfo_am(line, target)
        self.assertEqual(price, "")
        self.assertEqual(web_id, "B07KVKRLG2")


if __name__ == '__main__':
    unittest.main()
