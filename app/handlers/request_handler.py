from app.validator import Validator
from app.handlers.entry_handler import EntryHandler
import html


class RequestHandler():

    def __init__(self, form_data):
        self.validator = Validator()
        self.form_data = html.unescape(form_data)

    def extract_user_data(self):
        data_list = self.form_data.split(' ')
        user_email = data_list[0]
        product_url = data_list[1]
        return user_email, product_url

    def handle_request(self):
        user_email, product_url = self.extract_user_data()
        input_valid, error_message = self.validator.validate_user_input(user_email, product_url)
        if input_valid == False:
            return False, error_message

        # if input is valid i.e: input_valid == True
        entry_handler = EntryHandler()
        entry_added = entry_handler.add_entry(user_email, product_url)
        if entry_added == False:
            error_message = '* This exact user email and product url have been registered before'
            return False, error_message

        # if input is valid and teh entry was successfully added to the db
        message = "* We will email you when the product's price fall"
        return True, message
