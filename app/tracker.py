from app.handlers.entry_handler import EntryHandler, AmazonCrawler
#from app.crawler.amazon_crawler import AmazonCrawler
import smtplib
import time


class Tracker():

    def __init__(self):
        self.entry_handler = EntryHandler()

    def send_mail(self, URL, title, initial_price, new_price, user_email):
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Establishing a connection between client and the gmail server
        server.ehlo()
        server.starttls()  # Encrypting our connection
        server.ehlo()

        server.login('amazonpricet@gmail.com', 'arqdcapyimckuebi')

        subject = f'"{title}" Price has fell down!'
        body = f'The product "{title}" price has fallen down from $ {initial_price} to $ {new_price}!\nOpen the products link now: {URL}'
        msg = f"Subject: {subject} \n\n{body}"
        server.sendmail(
            'amazonpricet.gmail.com',
            user_email,
            msg.encode('utf8')
        )
        server.quit()
        print("Email has been sent!")

    def run(self):
        while True:
            all_entries = self.entry_handler.get_all_entries()
            for entry in all_entries:
                product_url = entry.product_url
                initial_price = entry.product_initial_price
                crawler = AmazonCrawler(product_url)
                current_price, _ = crawler.get_product_data()
                if current_price == initial_price:
                    title = entry.product_title
                    user_email = entry.user_email
                    self.send_mail(product_url, title, initial_price, current_price, user_email)
                    entry_handler = EntryHandler()
                    self.entry_handler.delete_entry(entry)
            time.sleep(86400)   # iterating through all users once every 24 hr



tracker = Tracker()
tracker.run()