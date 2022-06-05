import requests
from bs4 import BeautifulSoup

url = "https://www.kurzy.cz/komodity/ethereum-graf-vyvoje-ceny/"
def aktualni_cena(url):
  html = requests.get(url).text
  soup = BeautifulSoup(html)
  price = soup.find("span").text
  url_adress = soup.find("div", {"class": "joinbox"})
  zdroj = url.split("/")[3]
  print(f"Aktualni cena {zdroj} {price} USD")

def konec():
  x = input("Zmackni ENTER pro ukonceni programu ")
  if not x:
    print("Ukoncuji.")
    exit()
  else:
    a = int(input("\nEnter a Number : "))
    b = int(input("Enter another Number : "))
    print("Sum of the two numbers : ", a + b)

if __name__ == '__main__':
    aktualni_cena(url="https://www.kurzy.cz/bitcoin/")
    konec()

