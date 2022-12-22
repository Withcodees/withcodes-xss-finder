

import requests

print(
    """
 ##   ##   ####    ######   ##   ##    ####    #####   #####    #######   #####            ##  ##    #####    #####  
 ##   ##    ##     # ## #   ##   ##   ##  ##  ##   ##   ## ##    ##   #  ##   ##           ##  ##   ##   ##  ##   ## 
 ##   ##    ##       ##     ##   ##  ##       ##   ##   ##  ##   ## #    #                  ####    #        #       
 ## # ##    ##       ##     #######  ##       ##   ##   ##  ##   ####     #####   ######     ##      #####    #####  
 #######    ##       ##     ##   ##  ##       ##   ##   ##  ##   ## #         ##            ####         ##       ## 
 ### ###    ##       ##     ##   ##   ##  ##  ##   ##   ## ##    ##   #  ##   ##           ##  ##   ##   ##  ##   ## 
 ##   ##   ####     ####    ##   ##    ####    #####   #####    #######   #####            ##  ##    #####    ##### 

    """
)


hedef_site = input("Hedef site giriniz:")
site = ("http://" + hedef_site + "/index.php?q=")
txt = open("payload.txt", "r")
pay = txt.read()
txt.close()
for payloads in pay.splitlines():
    istek = requests.post(site + payloads)

    if payloads in istek.text:
        print("XSS açığı bulundu")
        print("İşlenen Payload:" + payloads)
        break
    else:
        print("XSS bulunamadı.")
