import requests
from bs4 import BeautifulSoup
import time
import smtplib

def check_price(URL, header, initial_price, title):
    page = requests.get(URL, headers=header)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    new_price = soup2.find(id="priceblock_ourprice").get_text()
    new_price = float(new_price[1:])
    if new_price < initial_price:
        send_mail(URL, title, initial_price, new_price, user_email)

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


URL = input("Enter the product's URL: ")
user_email = input('Enter your E-mail to be notified: ')
header = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page = requests.get(URL, headers=header)

soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
title = (soup2.find(id="productTitle").get_text()).strip()
initial_price = soup2.find(id="priceblock_ourprice").get_text()
initial_price = float(initial_price[1: ])

while(True):
    check_price(URL, header, initial_price, title)
