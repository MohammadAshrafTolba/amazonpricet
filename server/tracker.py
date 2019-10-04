import requests
from bs4 import BeautifulSoup
import smtplib

def get_price(URL, header):
    page = requests.get(URL, headers=header)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = (soup2.find(id="productTitle").get_text()).strip()
    price = soup2.find(id="priceblock_ourprice").get_text()
    price = float(price[1:])
    return price

def get_title(URL, header):
    page = requests.get(URL, headers=header)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = (soup2.find(id="productTitle").get_text()).strip()
    return title

def send_mail(URL, title, initial_price, new_price, user_email):
    server = smtplib.SMTP('smtp.gmail.com', 587)    # Establishing a connection between client and the gmail server
    server.ehlo()
    server.starttls()   # Encrypting our connection
    server.ehlo()

    server.login('amazonpricet@gmail.com', 'arqdcapyimckuebi')

    subject = 'Price has fell down!'
    body = f'The product "{title}" price has fallen down from $ {initial_price} to $ {new_price}!\nOpen the products link now: {URL}'
    msg = f"Subject: {subject} \n\n{body}"
    server.sendmail(
        'amazonpricet.gmail.com',
        user_email,
        msg.encode('utf8')
    )
    server.quit()
    print("Email has been sent!")
