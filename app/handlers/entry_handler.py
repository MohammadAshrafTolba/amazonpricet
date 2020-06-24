from app.models import Entry, db
#from app.init_app import db
from app.crawler.amazon_crawler import AmazonCrawler


class EntryHandler:

    def get_product_data(self, product_url):
        crawler = AmazonCrawler(product_url)
        initial_price, product_title = crawler.get_product_data()
        return initial_price, product_title

    def check_if_exists(self, new_entry):
        exists = db.session.query(Entry.id).filter_by(user_email=new_entry.user_email, product_url=new_entry.product_url).scalar() is not None
        return exists

    def add_entry(self, user_email, product_url):
        product_initial_price, product_title = self.get_product_data(product_url)
        new_entry = Entry(user_email=user_email, product_url=product_url, product_title=product_title, product_initial_price=product_initial_price)
        already_exists = self.check_if_exists(new_entry)
        entry_added = False
        if already_exists:
            return entry_added
        entry_added = True
        db.session.add(new_entry)
        db.session.commit()
        return entry_added

    def delete_entry(self, entry):
        db.session.query(Entry).filter(Entry.id == entry.id).delete()
        db.session.commit()

    def get_all_entries(self):
        entries = Entry.query.all()
        return entries