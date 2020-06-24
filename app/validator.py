from app.init_app import email_verifier
from urllib.parse import urlparse


class Validator:

    def validate_email(self, email):
        email_status = email_verifier.verify(email)
        email_valid_check = False
        if email_status is not None:
            if email_status.format_check == True \
                and email_status.smtp_check == True \
                and email_status.dns_check == True \
                and email_status.disposable_check == False:
                email_valid_check = True
        return email_valid_check

    def validate_url(self, url):
        domain = urlparse(url).netloc
        if domain == 'www.amazon.com':
            return True
        return False

    def validate_user_input(self, email, url):
        validator = Validator()
        email_valid = validator.validate_email(email)
        url_valid = validator.validate_url(url)
        message = ''
        input_valid = True

        if email_valid == False:
            message += '*  The email provided is invalid \n'
            input_valid = False
        if url_valid == False:
            message += '*  The URL provided is invalid'
            input_valid = False

        return input_valid, message