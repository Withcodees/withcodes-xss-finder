import requests


class XSSFinder:
  def __init__(self, url: str) -> None:
    self.page = url + "/index.php?q="
    self.banner = """
##   ##   ####    ######   ##   ##    ####    #####   #####    #######   #####            ##  ##    #####    #####
 ##   ##    ##     # ## #   ##   ##   ##  ##  ##   ##   ## ##    ##   #  ##   ##           ##  ##   ##   ##  ##   ##
 ##   ##    ##       ##     ##   ##  ##       ##   ##   ##  ##   ## #    #                  ####    #        #
 ## # ##    ##       ##     #######  ##       ##   ##   ##  ##   ####     #####   ######     ##      #####    #####
 #######    ##       ##     ##   ##  ##       ##   ##   ##  ##   ## #         ##            ####         ##       ##
 ### ###    ##       ##     ##   ##   ##  ##  ##   ##   ## ##    ##   #  ##   ##           ##  ##   ##   ##  ##   ##
 ##   ##   ####     ####    ##   ##    ####    #####   #####    #######   #####            ##  ##    #####    #####
"""

    with open("payload.txt", "r") as txt:
      self.payloads = [i for i in txt.readlines()]
    print(self.banner)
    print("Sekans Başlatıldı!...")
    self._make_request()
  def _make_request(self):
    for p in self.payloads:
      self.response = requests.post(self.page + p)
      if p in self.response.text:
        print("XSS açığı bulundu")
        print("İşlenen Payload:" + payloads)
        break
    print("XSS bulunamadı.")
finder = XSSFinder(input("Site URL:"))
