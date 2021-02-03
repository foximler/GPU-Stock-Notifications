import urllib.request
from bs4 import BeautifulSoup
import smtplib, ssl
import time

urls_to_check = {"card_3070_xc3":"evga-geforce-rtx-3070-08g-p5-3755-kr/p/N82E16814487530", "card_3070_FTW":"evga-geforce-rtx-3070-08g-p5-3767-kr/p/N82E16814487532"}
def send_message(product):
    receiver_email = '' #yournumber@msg.telus.com
    password = ''

    # For SSL
    port = 465
    smtp_server = ''
    sender_email = ''

    msg = f"In stock here: https://www.newegg.ca/{urls_to_check[product]}"

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)
def get_latest_webdata(list):
    for i in list:
        page_location = f"https://www.newegg.ca/{urls_to_check[i]}"
        page_data = urllib.request.urlopen(page_location).read().decode("utf-8")
        soup = BeautifulSoup(page_data, 'html.parser')
        is_present = soup.find('i', attrs={'class': 'fa-exclamation-triangle'})
        if is_present == None:
            send_message(i)
        else:
            current_time = time.strftime("%H:%M:%S", time.localtime())
            print(f"still out of stock at {current_time}")
        time.sleep(30)
while True:
    get_latest_webdata(urls_to_check)