# imports
import bs4 as bs
import urllib.request

# functions
def findTitle(soup):
    return soup.title.string

# main
def main():
    webpage = 'https://www.newegg.com/asus-geforce-rtx-2080-ti-rog-strix-rtx2080ti-o11g-gaming/p/N82E16814126263?Description=rog%20strix%202080ti&cm_re=rog_strix_2080ti-_-14-126-263-_-Product'
    source_code = urllib.request.urlopen(webpage).read()
    soup = bs.BeautifulSoup(source_code, 'lxml')

    title_string = findTitle(soup)
    print(title_string)


if __name__ == '__main__':
    main()