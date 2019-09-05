import tracker
import socket, pickle
import _thread as thread
import sys
import time


HOST = '127.0.0.1'  # (localhost)
PORT = 65432

user_list = []
initial_prices = []

header = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def client_thread(conn, user_list, initial_prices):
    conn.send('Connected to the server'.encode())
    while True:
        try:
            data = conn.recv(4096)
            print('Data received')

            new_user = pickle.loads(data)
            initial_price = tracker.get_price(new_user.product_link, header)

            user_list.append(new_user)
            initial_prices.append(initial_price)
        except:
            print('Client did not pass any data')
            break
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    try:
        s.bind((HOST, PORT))
        print('[Status] Socket is binded to port: ', PORT)
    except:
        print('[Status] Binding failed')
        sys.exit()

    s.listen(10)
    print('[Status] Socket is listening...\n')

    while True:

        conn, address = s.accept()
        thread.start_new_thread(client_thread, (conn, user_list, initial_prices))
        while True:
            for user , initial_price in zip(user_list, initial_prices):
                new_price = tracker.get_price(user.product_link, header)
                if new_price < initial_price:
                    title = tracker.get_title(user.product_link, header)
                    tracker.send_mail(user.product_link, title, initial_price, new_price, user.email)
                    user_list.remove(user)
                    initial_prices.remove(initial_price)
            time.sleep(86400)   # iterating through all users once every 24 hr





