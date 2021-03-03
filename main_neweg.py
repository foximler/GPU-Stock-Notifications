import urllib.request
from bs4 import BeautifulSoup
import smtplib, ssl
import time
from fp.fp import FreeProxy
urls_to_check = ["asus-geforce-rtx-3060-ti-tuf-rtx3060ti-o8g-gaming/p/N82E16814126471","msi-geforce-rtx-3090-rtx3090-suprim-x-24g/p/N82E16814137610","asus-geforce-rtx-3060-ti-rog-strix-rtx3060ti-o8g-gaming/p/N82E16814126470","zotac-geforce-rtx-3060-ti-zt-a30610h-10m/p/N82E16814500507","evga-geforce-rtx-3060-ti-08g-p5-3663-kr/p/N82E16814487535","asus-geforce-rtx-3060-ti-ko-rtx3060ti-o8g-gaming/p/N82E16814126474","gigabyte-geforce-rtx-3060-ti-gv-n306tgaming-oc-8gd/p/N82E16814932377","msi-geforce-rtx-3060-ti-rtx-3060-ti-gaming-x-trio/p/N82E16814137611","msi-geforce-rtx-3060-ti-rtx-3060-ti-ventus-2x-oc/p/N82E16814137612","asus-geforce-rtx-3060-ti-dual-rtx3060ti-o8g/p/N82E16814126468","msi-geforce-rtx-3090-rtx-3090-gaming-x-trio-24g/p/N82E16814137595","asus-geforce-rtx-3080-rog-strix-rtx3080-o10g-gaming/p/N82E16814126457","gigabyte-geforce-rtx-3060-ti-gv-n306taorus-m-8gd/p/N82E16814932375?Item=N82E16814932375","gigabyte-geforce-rtx-3060-ti-gv-n306tgamingoc-pro-8gd/p/N82E16814932376","gigabyte-geforce-rtx-3060-ti-gv-n306tgamingoc-pro-8gd/p/N82E16814932376","msi-geforce-rtx-3090-rtx-3090-ventus-3x-24g-oc/p/N82E16814137596","gigabyte-geforce-rtx-3080-gv-n3080aorus-x-10gd/p/N82E16814932345","asus-geforce-rtx-3080-tuf-rtx3080-o10g-gaming/p/N82E16814126452","gigabyte-geforce-rtx-3080-gv-n3080gaming-oc-10gd/p/N82E16814932329","gigabyte-geforce-rtx-3080-gv-n3080aorus-m-10gd/p/N82E16814932336","msi-geforce-rtx-3080-rtx-3080-ventus-3x-10g-oc/p/N82E16814137598","asus-geforce-rtx-3080-tuf-rtx3080-10g-gaming/p/N82E16814126453","asus-geforce-rtx-3090-rog-strix-rtx3090-o24g-white/p/N82E16814126482","asus-geforce-rtx-3090-rog-strix-rtx3090-o24g-gaming/p/N82E16814126456","gigabyte-geforce-rtx-3060-ti-gv-n306teagle-8gd/p/N82E16814932379","gigabyte-geforce-rtx-3060-ti-gv-n306teagle-oc-8gd/p/N82E16814932378","gigabyte-geforce-rtx-3080-gv-n3080vision-oc-10gd/p/N82E16814932337","evga-geforce-rtx-3080-10g-p5-3895-kr/p/N82E16814487519","evga-geforce-rtx-3080-10g-p5-3883-kr/p/N82E16814487521","gigabyte-geforce-rtx-3090-gv-n3090gaming-oc-24gd/p/N82E16814932327","asus-geforce-rtx-3090-tuf-rtx3090-24g-gaming/p/N82E16814126455","msi-geforce-rtx-3080-rtx-3080-gaming-x-trio-10g/p/N82E16814137597","evga-geforce-rtx-3080-10g-p5-3885-kr/p/N82E16814487520","evga-geforce-rtx-3090-24g-p5-3973-kr/p/N82E16814487523","gigabyte-geforce-rtx-3080-gv-n3080eagle-oc-10gd/p/N82E16814932330","gigabyte-geforce-rtx-3080-gv-n3080eagle-10gd/p/N82E16814932367","gigabyte-geforce-rtx-3090-gv-n3090vision-oc-24gd/p/N82E16814932365","asus-geforce-rtx-3080-rog-strix-rtx3080-10g-gaming/p/N82E16814126469","evga-geforce-rtx-3090-24g-p5-3975-kr/p/N82E16814487524","evga-geforce-rtx-3080-10g-p5-3881-kr/p/N82E16814487522","gigabyte-geforce-rtx-3090-gv-n3090eagle-oc-24gd/p/N82E16814932328","gigabyte-geforce-rtx-3090-gv-n3090aorus-m-24gd/p/N82E16814932341","msi-geforce-rtx-3090-rtx-3090-ventus-3x-24g/p/N82E16814137599","msi-geforce-rtx-3080-rtx-3080-ventus-3x-10g/p/N82E16814137600","evga-geforce-rtx-3090-24g-p5-3985-kr/p/N82E16814487525","evga-geforce-rtx-3090-24g-p5-3971-kr/p/N82E16814487527"]
def send_message(product):
    receiver_email = '' #yournumber@msg.telus.com
    password = ''

    # For SSL
    port = 465
    smtp_server = ''
    sender_email = ''

    msg = f"In stock here: https://www.newegg.ca/{product}"

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)
def get_latest_webdata(list):
    for i in list:
        proxy = FreeProxy(rand=True).get()
        authinfo = urllib.request.HTTPBasicAuthHandler()
        proxy_support = urllib.request.ProxyHandler({"http" : proxy})
        # build a new opener that adds authentication and caching FTP handlers
        opener = urllib.request.build_opener(proxy_support, authinfo,
                                       urllib.request.CacheFTPHandler)
        page_location = f"https://www.newegg.ca/{i}"
        page_data = urllib.request.urlopen(page_location).read().decode("utf-8")
        soup = BeautifulSoup(page_data, 'html.parser')
        is_present = soup.find('i', attrs={'class': 'fa-exclamation-triangle'})
        if is_present == None:
            send_message(i)
            # we save this data just so I can debug if a new exception occurs. 
            f = open("main.html", "a")
            f.write(page_data)
            f.close()
        else:
            current_time = time.strftime("%H:%M:%S", time.localtime())
            print(f"still out of stock at {current_time}")
        time.sleep(1)
while True:
    get_latest_webdata(urls_to_check)


