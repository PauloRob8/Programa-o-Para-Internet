import requests
from lxml import html

def main():

    r = requests.get('https://github.com/PauloRob8/Programa-o-Para-Internet')

    page = requests.get('https://github.com/PauloRob8/Programa-o-Para-Internet')
    webpage = html.fromstring(page.content)
    hrefs = webpage.xpath('//a/@href')

    print(hrefs)


if __name__ == '__main__':
    main()