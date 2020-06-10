from app.init_app import db


class Entry(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), index=True, nullable=False)
    product_url = db.Column(db.String(128), index=True, nullable=False)

    def __repr__(self):     # This method defines how objects should be printed
        return '<Entry: user_email: {email} | product_url: {url}>'.format(email=self.user_email, url=self.product_url)


#class post(db.Model):