import urllib.request
import certifi
from bs4 import BeautifulSoup
import smtplib, ssl
import time
from fp.fp import FreeProxy
from random import randint
from fake_useragent import UserAgent

gpu_list = "http://www.newegg.ca/p/pl?Submit=Property&Subcategory=48&N=100007708%20601359415%20601361654%20601357248%20601357247%20601357250%208000&IsPowerSearch=1&PageSize=96"
def send_message(product):
    receiver_email = '' #yournumber@msg.telus.com
    password = ''

    # For SSL
    port = 465
    smtp_server = ''
    sender_email = ''

    msg = f"In stock here:{product}"

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)
def get_latest_webdata(list):
    ua = UserAgent()
    proxy = FreeProxy(rand=True).get()
    proxy_support = urllib.request.ProxyHandler({"http":proxy})
    authinfo = urllib.request.HTTPBasicAuthHandler()
    opener = urllib.request.build_opener(proxy_support, authinfo, urllib.request.CacheFTPHandler)
    opener.addheaders = [('User-Agent','ua.random')]
    urllib.request.install_opener(opener)
    page_data = urllib.request.urlopen(gpu_list).read().decode("utf-8")
    soup = BeautifulSoup(page_data, 'html.parser')
    is_present = soup.find_all('div', attrs={'class': 'item-cell'})
    is_bot_found = soup.find('div', attrs={'class': 'lds-ripple'})        
    if is_bot_found != None:
        print("bot found")
    for n in is_present:
        item_data = soup.find('p', attrs={'class': 'item-promo'})
        if item_data == None:
            item_title = soup.find('a', attrs={'class': 'item-title'},href=True)['href']
            send_message(item_title)
            print("in stock")
        else:
            current_time = time.strftime("%H:%M:%S", time.localtime())
            print(f"still out of stock at {current_time}")

while True:
    get_latest_webdata(gpu_list)
    #time.sleep(5)
    time.sleep(randint(30,100))
