from app.init_app import app
from flask import render_template, request
from app.handlers.request_handler import RequestHandler


error_message_1 = error_message_2 = confirmation_message = ''

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def home_page():

    # globalize error/confirmation messages
    global error_message_1, error_message_2, confirmation_message

    if request.method == 'GET':
        return render_template('index.html', confirmation_message=confirmation_message, error_message_1=error_message_1, error_message_2=error_message_2)

    # if request.method == POST

    # initializing error/confirmation messages for each request as they are global variables
    error_message_1 = error_message_2 = confirmation_message = ''

    form_data = request.form['form_data']
    handler = RequestHandler(form_data)
    request_valid, status = handler.handle_request()
    if request_valid == True:
        confirmation_message = status
        return render_template('index.html')
    else:
        error_messages = status.split('\n')
        error_message_1 = error_messages[0]
        if len(error_messages) == 2:
            error_message_2 = error_messages[1]
        return render_template('index.html')


@app.route('/loading_page.html', methods=['POST'])
def loading_page():
    form_data = request.form['uEmail'] + ' ' + request.form['pURL']
    return render_template('loading_page.html', form_data=form_data)