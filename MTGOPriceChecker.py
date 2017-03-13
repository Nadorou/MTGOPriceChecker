from bs4 import BeautifulSoup
import requests


def getCardPrice(cardName, cardSet):
    formatted_name = cardName.replace(' ', '+')
    formatted_set = cardSet.replace(' ', '+')
    target_url = 'https://www.mtggoldfish.com/price/' + formatted_set + '/' + formatted_name + '#online'
    target_page = request_page(target_url)
    price = priceScan(target_page.text)
    return price


def request_page(url):
    page = requests.get(url)
    return page


def priceScan(htmlString):
    souped_page = BeautifulSoup(htmlString, 'html.parser')
    scanned_price = souped_page.find(class_='price-box online').find(class_='price-box-price').string
    price = float(scanned_price)
    return price
