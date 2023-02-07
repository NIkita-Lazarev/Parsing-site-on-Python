import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":"Ly_oay;t x/8q 2424.wqe"}

def download(url):
    resp = requests.get(url, stream=True)
    r = open("C:\\Users\\user\\Desktop\\backand\\Parsing\\download\\" + url.split("/")[-1], "wb")

    for val in resp.iter_content(1024*1024):
        r.write(val)
    r.close    
def GetURl():
    for count in range(1, 8):
        
       
        
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
        response = requests.get(url, headers=headers)


        soup =BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")


        for i in data:  
            """
            name = i.find("h4", class_="card-title").text.replace("\n", "")
            price = i.find("h5").text
            url_img =  "https://scrapingclub.com" + i.find("img").get("src")

            print(name + "\n" + price + "\n" + url_img + "\n")
            """
            
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield card_url
def array():
    for  card_urls in GetURl():
            
        response = requests.get(card_urls, headers=headers)
        sleep(3)
        soup =BeautifulSoup(response.text, "lxml")

        
        
        data = soup.find("div", class_="card mt-4 my-4")
        name = data.find("h3", class_="card-title").text
        price = data.find("h4").text
        text = data.find("p", class_="card-text").text
        url_img = "https://scrapingclub.com"  + data.find("img", class_="card-img-top img-fluid").get("src")
           
        download(url_img)
        yield name  + price  + text  + url_img    